@echo off
title Loading Baseball Scoreboard Server...

:: 1. Abrir el navegador en la URL de control
:: Usamos 'start' para que se ejecute en paralelo al servidor
echo Opening control panel...
start http://localhost:8000/control
start http://localhost:8000/overlay
start http://localhost:8000/scoreboard
start http://localhost:8000/lineup
start http://localhost:8000/atbat

:: 2. Ejecutar uvicorn
:: Si usas un entorno virtual, descomenta la siguiente linea:
:: call .venv\Scripts\activate

echo Starting Uvicorn server...
uvicorn server:app --host 0.0.0.0 --port 8000

pause