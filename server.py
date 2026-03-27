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
}

# ─── LÓGICA DEL JUEGO ─────────────────────────────────────────────────────────

def _add_out() -> None:
    """Suma un out. Al 3er out: cambia de half/inning y limpia bases y conteo."""
    state["outs"] += 1
    if state["outs"] >= 3:
        state["outs"]    = 0
        state["balls"]   = 0
        state["strikes"] = 0
        state["bases"]   = {"1st": False, "2nd": False, "3rd": False}
        if state["isTop"]:
            state["isTop"] = False          # top -> bot, mismo inning
        else:
            state["isTop"]   = True         # bot -> top del siguiente inning
            state["inning"] += 1


def handle_action(action: str, payload: dict) -> None:
    """Modifica `state` en función de la acción recibida desde el control."""

    # ── Datos de equipos ──────────────────────────────────────────────────────
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
        team  = payload.get("team")   # "away" | "home"
        delta = payload.get("delta", 0)
        key   = "awayScore" if team == "away" else "homeScore"
        state[key] = max(0, state[key] + delta)

    # ── Inning ────────────────────────────────────────────────────────────────
    elif action == "inning":
        delta = payload.get("delta", 0)
        state["inning"] = max(1, min(15, state["inning"] + delta))

    elif action == "toggle_half":
        state["isTop"] = not state["isTop"]

    # ── Conteo — wrap-around al sumar ─────────────────────────────────────────
    elif action == "ball":
        state["balls"] = (state["balls"] + 1) % 4     # 0→1→2→3→0

    elif action == "strike":
        state["strikes"] = (state["strikes"] + 1) % 3  # 0→1→2→0
        if state["strikes"] == 0:
            # 3er strike: out automatico + reset conteo
            state["balls"] = 0
            _add_out()

    elif action == "out":
        _add_out()

    elif action == "ball_minus":
        state["balls"] = max(0, state["balls"] - 1)

    elif action == "strike_minus":
        state["strikes"] = max(0, state["strikes"] - 1)

    elif action == "out_minus":
        state["outs"] = max(0, state["outs"] - 1)

    elif action == "reset_count":
        state["balls"]   = 0
        state["strikes"] = 0

    # ── Bases ─────────────────────────────────────────────────────────────────
    elif action == "toggle_base":
        base = payload.get("base")  # "1st" | "2nd" | "3rd"
        if base in state["bases"]:
            state["bases"][base] = not state["bases"][base]

    elif action == "clear_bases":
        state["bases"] = {"1st": False, "2nd": False, "3rd": False}

    # ── Reset completo ────────────────────────────────────────────────────────
    elif action == "reset_all":
        state.update({
            "awayScore": 0, "homeScore": 0,
            "inning":    1, "isTop":     True,
            "balls":     0, "strikes":   0, "outs": 0,
            "bases":     {"1st": False, "2nd": False, "3rd": False},
        })
# ── Animaciones ───────────────────────────────────────────────────────────
    elif action == "trigger_anim":
        state["event"] = payload.get("type") # "HIT" o "ERROR"
        # Opcional: podrías limpiar el evento después de un segundo, 
        # pero el overlay se encargará de quitar la clase.


# ─── BROADCAST ────────────────────────────────────────────────────────────────

async def broadcast_all() -> None:
    """Envía el estado actual a TODOS los clientes conectados."""
    dead = []
    for client in clients:
        try:
            await client.send_json(state)
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

    # Enviar estado actual al nuevo cliente al conectarse
    try:
        await ws.send_json(state)
    except Exception:
        clients.remove(ws)
        return

    try:
        while True:
            msg = await ws.receive_json()
            # msg esperado: {"action": "ball"} o {"action": "score", "payload": {"team": "away", "delta": 1}}
            action  = msg.get("action", "")
            payload = msg.get("payload", {})
            handle_action(action, payload)
            # Retransmitir estado actualizado a TODOS (incluido el control,
            # para que su UI refleje el estado canónico del servidor)
            await broadcast_all()

    except WebSocketDisconnect:
        if ws in clients:
            clients.remove(ws)
    except Exception:
        if ws in clients:
            clients.remove(ws)
