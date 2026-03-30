# ⚾ Baseball Scoreboard Overlay

A fast, lightweight and customizable **baseball scoreboard overlay** designed for live streaming (OBS, Streamlabs, etc.).

Built to provide **real-time game visualization**, animations (Hit, Error, Walk, Strikeout) and a clean broadcast-style UI.

<img width="416" height="128" alt="image" src="https://github.com/user-attachments/assets/7feb4904-85a6-435e-924a-6f51578d98db" />

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
   http://localhost:3000/lineup
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
* Manage the line-up
* Trigger animations:

  * `HIT`
  * `ERROR`
  * `WALK`
  * `STRIKEOUT`

<img width="811" height="920" alt="image" src="https://github.com/user-attachments/assets/af0a5550-fe74-435e-829c-66a97f72de33" />

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


