# ⚾ Baseball Scoreboard Overlay

A fast, lightweight and customizable **baseball scoreboard overlay** designed for live streaming (OBS, Streamlabs, etc.).

Built to provide **real-time game visualization**, animations (Hit, Error, Walk, Strikeout) and a clean broadcast-style UI.

---

## 🚀 Features

* ⚡ **Live Scoreboard Control Panel**
* 🎬 **Triggerable Animations**

  * Hit
  * Error
  * Walk (Base on Balls)
  * Strikeout
* 🖥️ **OBS Browser Source Ready**
* 🎨 **Customizable UI (colors, layout, animations)**
* 🔄 **Real-time updates**
* 🧩 **Lightweight & easy to integrate**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ParzivalSan/Baseball-Scoreboard.git
cd Baseball-Scoreboard
```

### 2. Open the control panel

Execute start.bat or uvicorn server:app --host 0.0.0.0 --port 8000

---

## 🎮 Usage

### OBS Setup

1. Open OBS
2. Add a **Browser Source**
3. Point it to:

   ```
   http://localhost:3000/overlay
   http://localhost:3000/scoreboard
   ```
4. Set resolution (recommended):

   ```
   1920x1080
   ```

---

### Control Panel

From the control interface you can:

* Update score
* Change inning
* Manage bases
* Trigger animations:

  * `HIT`
  * `ERROR`
  * `WALK`
  * `STRIKEOUT`

---

## 🤝 Contributing

Pull requests are welcome.

For major changes:

1. Open an issue
2. Discuss your idea
3. Submit PR

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share it
* Use it in your streams

---

[1]: https://github.com/FC-softwares/baseball-scoreboard?utm_source=chatgpt.com "GitHub - FC-softwares/baseball-scoreboard: Baseball Scoreboard for youtube LIVE. You can use this tool as overlay for your baseball live-stream. In the last version we have integrated Animations, new professional looking graphic, MyBallClub overriding and more..."
