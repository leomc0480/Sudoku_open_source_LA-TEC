#!/bin/bash

# ====================================================
# Script para crear ejecutable de Sudoku en Linux/Mac
# ====================================================

echo ""
echo "===================================="
echo "  GENERADOR DE EJECUTABLE SUDOKU"
echo "===================================="
echo ""

# Verificar si PyInstaller está instalado
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "[PASO 1] Instalando PyInstaller..."
    pip3 install pyinstaller
else
    echo "[PASO 1] PyInstaller ya está instalado"
fi

echo ""
echo "[PASO 2] Creando ejecutable..."
echo ""

# Crear ejecutable con PyInstaller
# --onefile: Todo en un solo archivo ejecutable
# --windowed: Sin terminal (solo ventana del juego)
# --name: Nombre del ejecutable

pyinstaller --onefile --windowed --name "Sudoku" main.py

echo ""
echo "===================================="
echo "  EJECUTABLE CREADO EXITOSAMENTE"
echo "===================================="
echo ""
echo "El ejecutable se encuentra en:"
echo "  $(pwd)/dist/Sudoku"
echo ""
echo "Para ejecutarlo:"
echo "  ./dist/Sudoku"
echo ""
