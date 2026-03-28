from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

clients: list[WebSocket] = []

# ─── ESTADO ───────────────────────────────────────────────────────────────────

state = {
    "awayName":  "VISITANTE",
    "homeName":  "LOCAL",
    "awayColor": "#e85252",
    "homeColor": "#4bc8e8",
    "brand":     "BASEBALL",
    "awayScore": 0,
    "homeScore": 0,
    "inning":    1,
    "isTop":     True,
    "balls":     0,
    "strikes":   0,
    "outs":      0,
    "bases":     {"1st": False, "2nd": False, "3rd": False},
    # event: solo se pone en trigger_anim. NUNCA se persiste entre acciones.
    # Se envía como campo separado solo cuando hay un evento explícito.
}

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def _add_out() -> None:
    """Suma un out. Al 3er out: cambia half/inning y limpia bases y conteo."""
    state["outs"] += 1
    if state["outs"] >= 3:
        state["outs"]    = 0
        state["balls"]   = 0
        state["strikes"] = 0
        state["bases"]   = {"1st": False, "2nd": False, "3rd": False}
        if state["isTop"]:
            state["isTop"] = False
        else:
            state["isTop"]   = True
            state["inning"] += 1


def _walk() -> None:
    """Base por bolas: avanza corredores en cadena. Bases llenas → carrera."""
    b = state["bases"]
    team_key = "awayScore" if state["isTop"] else "homeScore"
    if b["1st"] and b["2nd"] and b["3rd"]:
        state[team_key] += 1          # corredor de 3ª anota
    if b["2nd"]:
        b["3rd"] = True
    if b["1st"]:
        b["2nd"] = True
    b["1st"] = True
    state["balls"]   = 0
    state["strikes"] = 0

# ─── LÓGICA ───────────────────────────────────────────────────────────────────

def handle_action(action: str, payload: dict) -> dict | None:
    """
    Modifica `state` y devuelve un dict de evento {event, label} si corresponde,
    o None si no hay evento especial.
    Las animaciones SOLO se disparan desde trigger_anim — nunca automáticamente.
    """

    # ── Equipos ───────────────────────────────────────────────────────────────
    if action == "set_away_name":
        state["awayName"] = payload.get("value", state["awayName"])
    elif action == "set_home_name":
        state["homeName"] = payload.get("value", state["homeName"])
    elif action == "set_away_color":
        state["awayColor"] = payload.get("value", state["awayColor"])
    elif action == "set_home_color":
        state["homeColor"] = payload.get("value", state["homeColor"])
    elif action == "set_brand":
        state["brand"] = payload.get("value", state["brand"])

    # ── Marcador ──────────────────────────────────────────────────────────────
    elif action == "score":
        team  = payload.get("team")
        delta = payload.get("delta", 0)
        key   = "awayScore" if team == "away" else "homeScore"
        state[key] = max(0, state[key] + delta)

    # ── Inning ────────────────────────────────────────────────────────────────
    elif action == "inning":
        state["inning"] = max(1, min(15, state["inning"] + payload.get("delta", 0)))
    elif action == "toggle_half":
        state["isTop"] = not state["isTop"]

    # ── Conteo ────────────────────────────────────────────────────────────────
    # Los botones + en strikes/balls preguntan confirmación en el JS cuando llegan
    # al límite. El servidor recibe strike_confirm / walk_confirm tras el OK.

    elif action == "ball":
        # Bola normal (1, 2 o 3) — solo actualiza contador
        state["balls"] = min(3, state["balls"] + 1)

    elif action == "walk_confirm":
        # 4ª bola confirmada por el usuario → base por bolas con lógica de corredores
        _walk()

    elif action == "strike":
        # Strike normal (1 o 2) — solo actualiza contador
        state["strikes"] = min(2, state["strikes"] + 1)

    elif action == "strikeout_confirm":
        # 3er strike confirmado por el usuario → out automático + reset conteo
        state["balls"]   = 0
        state["strikes"] = 0
        _add_out()

    elif action == "ball_minus":
        state["balls"]   = max(0, state["balls"] - 1)
    elif action == "strike_minus":
        state["strikes"] = max(0, state["strikes"] - 1)
    elif action == "out_minus":
        state["outs"]    = max(0, state["outs"] - 1)

    elif action == "reset_count":
        state["balls"]   = 0
        state["strikes"] = 0

    elif action == "out":
        _add_out()

    # ── Bases ─────────────────────────────────────────────────────────────────
    elif action == "toggle_base":
        base = payload.get("base")
        if base in state["bases"]:
            state["bases"][base] = not state["bases"][base]
    elif action == "clear_bases":
        state["bases"] = {"1st": False, "2nd": False, "3rd": False}

    # ── Reset ─────────────────────────────────────────────────────────────────
    elif action == "reset_all":
        state.update({
            "awayScore": 0, "homeScore": 0,
            "inning": 1, "isTop": True,
            "balls": 0, "strikes": 0, "outs": 0,
            "bases": {"1st": False, "2nd": False, "3rd": False},
        })

    # ── Animaciones — SOLO desde aquí, NUNCA automáticas ──────────────────────
    elif action == "trigger_anim":
        event_type = payload.get("type", "")
        # Para CARRERA: el servidor deduce el equipo a partir de isTop
        if event_type == "RUN":
            team_name  = state["awayName"]  if state["isTop"] else state["homeName"]
            team_color = state["awayColor"] if state["isTop"] else state["homeColor"]
        else:
            team_name  = payload.get("team_name", "")
            team_color = payload.get("team_color", "")
        return {"event": event_type, "eventTeam": team_name, "eventTeamColor": team_color}

    return None  # sin evento

# ─── BROADCAST ────────────────────────────────────────────────────────────────

async def broadcast_all(extra: dict | None = None) -> None:
    """Envía el estado a todos los clientes, con campos extra opcionales (evento)."""
    payload = dict(state)
    if extra:
        payload.update(extra)
    dead = []
    for client in clients:
        try:
            await client.send_json(payload)
        except Exception:
            dead.append(client)
    for d in dead:
        clients.remove(d)

# ─── RUTAS HTTP ───────────────────────────────────────────────────────────────

@app.get("/")
@app.get("/control")
def serve_control():
    return FileResponse("static/baseball-control.html")

@app.get("/overlay")
def serve_overlay():
    return FileResponse("static/baseball-overlay.html")

# ─── WEBSOCKET ────────────────────────────────────────────────────────────────

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    try:
        await ws.send_json(state)   # estado inicial sin evento
    except Exception:
        clients.remove(ws)
        return

    try:
        while True:
            msg     = await ws.receive_json()
            action  = msg.get("action", "")
            payload = msg.get("payload", {})
            extra   = handle_action(action, payload)
            await broadcast_all(extra)  # extra solo existe en trigger_anim

    except WebSocketDisconnect:
        if ws in clients:
            clients.remove(ws)
    except Exception:
        if ws in clients:
            clients.remove(ws)
