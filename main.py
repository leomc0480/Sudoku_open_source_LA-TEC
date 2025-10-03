"""
Sudoku - Juego de Lógica y Memoria

Este programa permite al usuario resolver tableros de Sudoku de diferentes
dificultades (Fácil, Medio, Difícil) con una interfaz gráfica interactiva.

Características:
- Interfaz gráfica con tkinter (clickeable)
- 3 niveles de dificultad
- Sistema de puntuación basado en tiempo, precisión y ayudas
- Modo ayuda para validar movimientos
- Sistema de pistas
- Estadísticas guardadas en JSON
- Retroalimentación visual (celdas correctas/incorrectas)

Autor: Sistema de Sudoku
Fecha: 2025
"""

from sudoku_gui import SudokuGUI


def main():
    """Punto de entrada principal del programa"""
    try:
        # Crear e iniciar la interfaz gráfica
        app = SudokuGUI()
        app.run()
    except Exception as e:
        print(f"Error al iniciar el juego: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
