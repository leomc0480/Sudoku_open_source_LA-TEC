"""
Generador de tableros de Sudoku con solución única
"""
import random
from typing import List, Tuple, Optional


class SudokuGenerator:
    """Genera tableros de Sudoku válidos con solución única"""

    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def generate(self, empty_cells: int) -> Tuple[List[List[int]], List[List[int]]]:
        """
        Genera un tablero de Sudoku con la cantidad especificada de celdas vacías

        Args:
            empty_cells: Número de celdas vacías en el tablero

        Returns:
            Tupla (tablero_con_vacios, solucion_completa)
        """
        # Generar un tablero completo válido
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self._fill_grid()

        # Copiar la solución
        solution = [row[:] for row in self.grid]

        # Crear el tablero de juego removiendo celdas
        puzzle = [row[:] for row in self.grid]
        self._remove_cells(puzzle, empty_cells)

        return puzzle, solution

    def _fill_grid(self) -> bool:
        """Llena el tablero con una solución válida usando backtracking"""
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)

                    for num in numbers:
                        if self._is_valid(i, j, num):
                            self.grid[i][j] = num

                            if self._fill_grid():
                                return True

                            self.grid[i][j] = 0

                    return False
        return True

    def _is_valid(self, row: int, col: int, num: int) -> bool:
        """Verifica si un número es válido en la posición dada"""
        # Verificar fila
        if num in self.grid[row]:
            return False

        # Verificar columna
        if num in [self.grid[i][col] for i in range(9)]:
            return False

        # Verificar subcuadro 3x3
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def _remove_cells(self, grid: List[List[int]], count: int):
        """Remueve celdas del tablero de forma aleatoria"""
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)

        for i in range(min(count, 81)):
            row, col = cells[i]
            grid[row][col] = 0


def validate_move(grid: List[List[int]], row: int, col: int, num: int,
                  solution: List[List[int]] = None) -> Tuple[bool, str]:
    """
    Valida si un movimiento es válido según las reglas del Sudoku

    Args:
        grid: Tablero actual
        row: Fila (0-8)
        col: Columna (0-8)
        num: Número a colocar (1-9)
        solution: Solución del tablero (opcional, para verificación exacta)

    Returns:
        Tupla (es_valido, mensaje)
    """
    if num < 1 or num > 9:
        return False, "El número debe estar entre 1 y 9"

    # Si tenemos la solución, verificar si es correcto
    if solution:
        if solution[row][col] != num:
            return False, "Número incorrecto"
        return True, "¡Correcto!"

    # Verificar reglas básicas del Sudoku
    # Verificar fila
    for j in range(9):
        if j != col and grid[row][j] == num:
            return False, "Número repetido en la fila"

    # Verificar columna
    for i in range(9):
        if i != row and grid[i][col] == num:
            return False, "Número repetido en la columna"

    # Verificar subcuadro 3x3
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if (i != row or j != col) and grid[i][j] == num:
                return False, "Número repetido en el subcuadro"

    return True, "Válido según las reglas"  


def check_complete(grid: List[List[int]], solution: List[List[int]]) -> Tuple[bool, int]:
    """
    Verifica si el tablero está completo y cuenta errores

    Returns:
        Tupla (esta_completo, cantidad_errores)
    """
    errors = 0
    complete = True

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                complete = False
            elif grid[i][j] != solution[i][j]:
                errors += 1

    return complete, errors
