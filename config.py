"""
Configuración y constantes para el juego de Sudoku
"""

# Colores
COLORS = {
    'bg': '#F0F0F0',
    'grid_bg': '#FFFFFF',
    'fixed_cell': '#E8E8E8',
    'selected': '#BBE5FF',
    'correct': '#C8E6C9',
    'incorrect': '#FFCDD2',
    'text_fixed': '#000000',
    'text_user': '#1976D2',
    'grid_line': '#BDBDBD',
    'grid_thick': '#424242',
    'button_bg': '#2196F3',
    'button_hover': '#1976D2',
    'button_text': '#FFFFFF',
    'title': '#1565C0',
    'stats_bg': '#E3F2FD'
}

# Dimensiones
CELL_SIZE = 60
GRID_SIZE = 9
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700

# Dificultades (celdas vacías)
DIFFICULTY_LEVELS = {
    'Fácil': 30,
    'Medio': 45,
    'Difícil': 55
}

# Puntuación
BASE_SCORE = 1000
TIME_BONUS_INTERVAL = 5  # segundos
TIME_BONUS_POINTS = 1
ERROR_PENALTY = 5
HINT_PENALTY = 10

# Límites de tiempo por dificultad (segundos)
TIME_LIMITS = {
    'Fácil': 1800,   # 30 minutos
    'Medio': 2400,   # 40 minutos
    'Difícil': 3600  # 60 minutos
}

# Archivo de estadísticas
STATS_FILE = 'sudoku_stats.json'
