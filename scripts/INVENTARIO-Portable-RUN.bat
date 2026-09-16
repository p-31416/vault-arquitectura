@echo off
:: Portable - doble-click genera .md + .txt al lado del script y abre Bloc de notas
set "PS1=%~dp0inventario-portable.ps1"
echo === Inventario portable ===
powershell -NoProfile -ExecutionPolicy Bypass -File "%PS1%"
pause
