"""
Lógica principal del juego de Sudoku
"""
import time
from typing import List, Optional, Tuple
from sudoku_generator import SudokuGenerator, validate_move, check_complete
from config import BASE_SCORE, TIME_BONUS_INTERVAL, TIME_BONUS_POINTS, ERROR_PENALTY, HINT_PENALTY, TIME_LIMITS


class SudokuGame:
    """Maneja la lógica del juego de Sudoku"""

    def __init__(self, difficulty: str):
        """
        Inicializa un nuevo juego

        Args:
            difficulty: Nivel de dificultad ('Fácil', 'Medio', 'Difícil')
        """
        self.difficulty = difficulty
        self.grid: List[List[int]] = []
        self.solution: List[List[int]] = []
        self.initial_grid: List[List[int]] = []
        self.start_time = time.time()
        self.hints_used = 0
        self.game_over = False
        self.won = False

        # Generar el tablero
        self._generate_board()

    def _generate_board(self):
        """Genera un nuevo tablero según la dificultad"""
        from config import DIFFICULTY_LEVELS

        generator = SudokuGenerator()
        empty_cells = DIFFICULTY_LEVELS[self.difficulty]
        self.grid, self.solution = generator.generate(empty_cells)
        self.initial_grid = [row[:] for row in self.grid]

    def is_fixed_cell(self, row: int, col: int) -> bool:
        """Verifica si una celda es fija (parte del tablero inicial)"""
        return self.initial_grid[row][col] != 0

    def make_move(self, row: int, col: int, num: int) -> Tuple[bool, str]:
        """
        Intenta colocar un número en el tablero

        Returns:
            Tupla (exito, mensaje)
        """
        if self.game_over:
            return False, "El juego ha terminado"

        if self.is_fixed_cell(row, col):
            return False, "No puedes modificar celdas fijas"

        if num == 0:  # Borrar celda
            self.grid[row][col] = 0
            return True, "Celda borrada"

        # Colocar número
        self.grid[row][col] = num
        return True, "Número colocado"

    def validate_current_move(self, row: int, col: int, num: int) -> Tuple[bool, str]:
        """
        Valida un movimiento contra la solución (modo ayuda)

        Returns:
            Tupla (es_correcto, mensaje)
        """
        if num == 0:
            return True, ""

        is_valid, message = validate_move(self.grid, row, col, num, self.solution)
        return is_valid, message

    def use_hint(self, row: int, col: int) -> Optional[int]:
        """
        Usa una pista para revelar el número correcto en una celda

        Returns:
            Número correcto o None si la celda es fija
        """
        if self.is_fixed_cell(row, col):
            return None

        self.hints_used += 1
        return self.solution[row][col]

    def check_victory(self) -> Tuple[bool, int]:
        """
        Verifica si el tablero está completo y correcto

        Returns:
            Tupla (victoria, cantidad_errores)
        """
        complete, errors = check_complete(self.grid, self.solution)

        if complete and errors == 0:
            self.game_over = True
            self.won = True
            return True, 0

        return False, errors

    def calculate_score(self) -> int:
        """
        Calcula la puntuación final del juego

        Returns:
            Puntuación total
        """
        if not self.won:
            return 0

        score = BASE_SCORE

        # Bonificación por tiempo
        elapsed_time = int(time.time() - self.start_time)
        time_limit = TIME_LIMITS[self.difficulty]
        time_remaining = max(0, time_limit - elapsed_time)
        time_bonus = (time_remaining // TIME_BONUS_INTERVAL) * TIME_BONUS_POINTS
        score += time_bonus

        # Penalización por pistas
        hint_penalty = self.hints_used * HINT_PENALTY
        score -= hint_penalty

        # La puntuación no puede ser negativa
        return max(0, score)

    def get_elapsed_time(self) -> int:
        """Retorna el tiempo transcurrido en segundos"""
        if self.game_over:
            return int(self.start_time - self.start_time)  # Congelado al finalizar
        return int(time.time() - self.start_time)

    def get_cell_state(self, row: int, col: int) -> str:
        """
        Retorna el estado de una celda para colorearla

        Returns:
            'fixed', 'empty', 'user', 'correct', 'incorrect'
        """
        if self.is_fixed_cell(row, col):
            return 'fixed'

        if self.grid[row][col] == 0:
            return 'empty'

        # Si el juego terminó, mostrar si es correcto o incorrecto
        if self.game_over:
            if self.grid[row][col] == self.solution[row][col]:
                return 'correct'
            else:
                return 'incorrect'

        return 'user'

    def restart_game(self):
        """Reinicia el juego con el mismo tablero"""
        self.grid = [row[:] for row in self.initial_grid]
        self.start_time = time.time()
        self.hints_used = 0
        self.game_over = False
        self.won = False

    def new_game(self, difficulty: Optional[str] = None):
        """Inicia un nuevo juego con opción de cambiar dificultad"""
        if difficulty:
            self.difficulty = difficulty

        self._generate_board()
        self.start_time = time.time()
        self.hints_used = 0
        self.game_over = False
        self.won = False
