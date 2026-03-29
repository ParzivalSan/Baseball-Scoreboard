from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

# Servir GIFs estáticos desde la carpeta gif/
GIF_DIR = Path("gif")
GIF_DIR.mkdir(exist_ok=True)
app.mount("/gif", StaticFiles(directory="gif"), name="gif")

clients: list[WebSocket] = []
MAX_INNINGS = 9

state = {
    "awayName":"VISITANTE","homeName":"LOCAL",
    "awayColor":"#02437d","homeColor":"#a40133",
    "brand":"BASEBALL",
    "awayScore":0,"homeScore":0,
    "awayHits":0,"homeHits":0,
    "awayErrors":0,"homeErrors":0,
    "inningScores":[[None,None]]*MAX_INNINGS,
    "inning":1,"isTop":True,
    "balls":0,"strikes":0,"outs":0,
    "bases":{"1st":False,"2nd":False,"3rd":False},
    # Lineup: dos equipos, 10 slots de jugador + coach + equipo visible en overlay
    "lineup": {
        "showing": "away",   # "away" | "home"
        "away": {
            "coach": "",
            "players": [{"order": i+1, "name": "", "position": "", "number": ""} for i in range(10)]
        },
        "home": {
            "coach": "",
            "players": [{"order": i+1, "name": "", "position": "", "number": ""} for i in range(10)]
        }
    },
}

def _inning_idx():
    return min(state["inning"]-1, MAX_INNINGS-1)

def _mark_inning_played():
    idx=_inning_idx()
    scores=list(state["inningScores"])
    row=list(scores[idx]) if scores[idx] else [None,None]
    changed=False
    if row[0] is None: row[0]=0; changed=True
    if row[1] is None: row[1]=0; changed=True
    if changed: scores[idx]=row; state["inningScores"]=scores

def _add_inning_run(is_top, runs=1):
    idx=_inning_idx()
    scores=list(state["inningScores"])
    row=list(scores[idx]) if scores[idx] else [None,None]
    col=0 if is_top else 1
    row[col]=(row[col] or 0)+runs
    scores[idx]=row; state["inningScores"]=scores

def _add_out():
    state["outs"]+=1
    if state["outs"]>=3:
        _mark_inning_played()
        state["outs"]=0; state["balls"]=0; state["strikes"]=0
        state["bases"]={"1st":False,"2nd":False,"3rd":False}
        if state["isTop"]: state["isTop"]=False
        else: state["isTop"]=True; state["inning"]+=1; _mark_inning_played()

def _walk():
    b=state["bases"]; is_top=state["isTop"]
    team_key="awayScore" if is_top else "homeScore"
    if b["1st"] and b["2nd"] and b["3rd"]:
        state[team_key]+=1; _add_inning_run(is_top)
    if b["2nd"]: b["3rd"]=True
    if b["1st"]: b["2nd"]=True
    b["1st"]=True; state["balls"]=0; state["strikes"]=0

def handle_action(action, payload):
    if   action=="set_away_name":  state["awayName"] =payload.get("value",state["awayName"])
    elif action=="set_home_name":  state["homeName"] =payload.get("value",state["homeName"])
    elif action=="set_away_color": state["awayColor"]=payload.get("value",state["awayColor"])
    elif action=="set_home_color": state["homeColor"]=payload.get("value",state["homeColor"])
    elif action=="set_brand":      state["brand"]    =payload.get("value",state["brand"])
    elif action=="score":
        team=payload.get("team"); delta=payload.get("delta",0)
        key="awayScore" if team=="away" else "homeScore"
        state[key]=max(0,state[key]+delta)
        if delta>0: _add_inning_run(team=="away",delta); _mark_inning_played()
    elif action=="hit":
        team=payload.get("team"); delta=payload.get("delta",0)
        key="awayHits" if team=="away" else "homeHits"
        state[key]=max(0,state[key]+delta)
    elif action=="error":
        team=payload.get("team"); delta=payload.get("delta",0)
        key="awayErrors" if team=="away" else "homeErrors"
        state[key]=max(0,state[key]+delta)
    elif action=="inning":
        state["inning"]=max(1,min(15,state["inning"]+payload.get("delta",0)))
    elif action=="toggle_half": state["isTop"]=not state["isTop"]
    elif action=="ball":    state["balls"]=min(3,state["balls"]+1)
    elif action=="walk_confirm": _walk()
    elif action=="strike":  state["strikes"]=min(2,state["strikes"]+1)
    elif action=="strikeout_confirm":
        state["balls"]=0; state["strikes"]=0; _add_out()
    elif action=="out": _add_out()
    elif action=="out_confirm": _add_out()
    elif action=="ball_minus":   state["balls"]  =max(0,state["balls"]-1)
    elif action=="strike_minus": state["strikes"]=max(0,state["strikes"]-1)
    elif action=="out_minus":    state["outs"]   =max(0,state["outs"]-1)
    elif action=="reset_count":  state["balls"]=0; state["strikes"]=0
    elif action=="toggle_base":
        base=payload.get("base")
        if base in state["bases"]: state["bases"][base]=not state["bases"][base]
    elif action=="clear_bases": state["bases"]={"1st":False,"2nd":False,"3rd":False}
    elif action=="set_inning_score":
        idx=payload.get("inning",1)-1; team=payload.get("team"); val=payload.get("value")
        if 0<=idx<MAX_INNINGS:
            scores=list(state["inningScores"])
            row=list(scores[idx]) if scores[idx] else [None,None]
            col=0 if team=="away" else 1; row[col]=val; scores[idx]=row
            state["inningScores"]=scores
            state["awayScore"]=sum(r[0] for r in state["inningScores"] if r and r[0] is not None)
            state["homeScore"]=sum(r[1] for r in state["inningScores"] if r and r[1] is not None)
    elif action=="reset_all":
        state.update({"awayScore":0,"homeScore":0,"awayHits":0,"homeHits":0,
            "awayErrors":0,"homeErrors":0,"inningScores":[[None,None]]*MAX_INNINGS,
            "inning":1,"isTop":True,"balls":0,"strikes":0,"outs":0,
            "bases":{"1st":False,"2nd":False,"3rd":False}})
    elif action=="trigger_anim":
        evt=payload.get("type","")
        if evt=="RUN":
            tn=state["awayName"] if state["isTop"] else state["homeName"]
            tc=state["awayColor"] if state["isTop"] else state["homeColor"]
        else:
            tn=payload.get("team_name",""); tc=payload.get("team_color","")
        return {"event":evt,"eventTeam":tn,"eventTeamColor":tc}
    elif action=="trigger_gif":
        filename=payload.get("filename","")
        return {"gif":filename}
    elif action=="set_lineup_player":
        team  = payload.get("team")          # "away" | "home"
        slot  = payload.get("slot", 0)       # 0-9
        field = payload.get("field")         # "name" | "position" | "number" | "order"
        val   = payload.get("value", "")
        if team in ("away","home") and 0 <= slot < 10 and field in ("name","position","number","order"):
            state["lineup"][team]["players"][slot][field] = val
    elif action=="set_lineup_coach":
        team = payload.get("team")
        if team in ("away","home"):
            state["lineup"][team]["coach"] = payload.get("value","")
    elif action=="set_lineup_showing":
        team = payload.get("team")
        if team in ("away","home"):
            state["lineup"]["showing"] = team
    return None

async def broadcast_all(extra=None):
    payload=dict(state)
    if extra: payload.update(extra)
    dead=[]
    for c in clients:
        try: await c.send_json(payload)
        except: dead.append(c)
    for d in dead: clients.remove(d)

@app.get("/")
@app.get("/control")
def serve_control(): return FileResponse("static/baseball-control.html")

@app.get("/overlay")
def serve_overlay(): return FileResponse("static/baseball-overlay.html")

@app.get("/scoreboard")
def serve_scoreboard(): return FileResponse("static/baseball-scoreboard.html")

@app.get("/lineup")
def serve_lineup(): return FileResponse("static/baseball-lineup.html")

@app.get("/api/gifs")
def list_gifs():
    """Devuelve la lista de archivos GIF en la carpeta gif/."""
    if not GIF_DIR.exists():
        return JSONResponse([])
    files = sorted(
        f.name for f in GIF_DIR.iterdir()
        if f.suffix.lower() in (".gif", ".webp", ".apng", ".png", ".jpg", ".jpeg")
    )
    return JSONResponse(files)

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept(); clients.append(ws)
    try: await ws.send_json(state)
    except: clients.remove(ws); return
    try:
        while True:
            msg=await ws.receive_json()
            extra=handle_action(msg.get("action",""),msg.get("payload",{}))
            await broadcast_all(extra)
    except WebSocketDisconnect:
        if ws in clients: clients.remove(ws)
    except:
        if ws in clients: clients.remove(ws)
