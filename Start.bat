@echo off
title Cargando Servidor Baseball Scoreboard...

:: 1. Abrir el navegador en la URL de control
:: Usamos 'start' para que se ejecute en paralelo al servidor
echo Abriendo panel de control...
start http://localhost:8000/control
start http://localhost:8000/overlay

:: 2. Ejecutar uvicorn
:: Si usas un entorno virtual, descomenta la siguiente linea:
:: call .venv\Scripts\activate

echo Iniciando servidor Uvicorn...
uvicorn server:app --host 0.0.0.0 --port 8000

pause