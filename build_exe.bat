@echo off
REM ====================================================
REM Script para crear ejecutable de Sudoku en Windows
REM ====================================================

echo.
echo ====================================
echo   GENERADOR DE EJECUTABLE SUDOKU
echo ====================================
echo.

REM Verificar si PyInstaller está instalado
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [PASO 1] Instalando PyInstaller...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: No se pudo instalar PyInstaller
        echo Intenta ejecutar manualmente: pip install pyinstaller
        pause
        exit /b 1
    )
) else (
    echo [PASO 1] PyInstaller ya esta instalado
)

echo.
echo [PASO 2] Creando ejecutable...
echo.

REM Crear ejecutable con PyInstaller usando python -m
REM --onefile: Todo en un solo archivo .exe
REM --windowed: Sin consola (solo ventana del juego)
REM --name: Nombre del ejecutable

python -m PyInstaller --onefile --windowed --name "Sudoku" main.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo crear el ejecutable
    echo.
    echo Intenta estos comandos manualmente:
    echo   pip install pyinstaller
    echo   pyinstaller --onefile --windowed --name "Sudoku" main.py
    echo.
    pause
    exit /b 1
)

echo.
echo ====================================
echo   EJECUTABLE CREADO EXITOSAMENTE
echo ====================================
echo.
echo El ejecutable se encuentra en:
echo   %cd%\dist\Sudoku.exe
echo.
echo Puedes copiar este archivo a cualquier computadora
echo Windows y ejecutarlo sin necesidad de tener Python instalado
echo.
pause
