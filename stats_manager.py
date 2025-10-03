"""
Sistema de gestión de estadísticas del juego

Este módulo maneja todo lo relacionado con guardar, cargar y calcular
las estadísticas del juego de Sudoku. Las estadísticas se guardan en
un archivo JSON para persistencia entre sesiones.

NOTA: Este archivo se llama 'stats_manager.py' para evitar conflictos
con el módulo built-in 'statistics' de Python.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from config import STATS_FILE


class StatisticsManager:
    """
    Clase que maneja el guardado y carga de estadísticas del juego

    Atributos:
        stats_file (str): Ruta al archivo JSON de estadísticas
        stats (Dict): Diccionario con todas las estadísticas del juego
    """

    def __init__(self):
        """Inicializa el gestor de estadísticas y carga datos existentes"""
        self.stats_file = STATS_FILE  # Nombre del archivo JSON
        self.stats = self._load_stats()  # Cargar estadísticas desde archivo

    def _load_stats(self) -> Dict:
        """
        Carga las estadísticas desde el archivo JSON

        Si el archivo no existe o está corrupto, crea una nueva estructura vacía.

        Returns:
            Dict: Diccionario con todas las estadísticas
        """
        # Verificar si el archivo existe
        if os.path.exists(self.stats_file):
            try:
                # Intentar cargar el archivo JSON
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                # Si hay error al leer, crear estadísticas vacías
                return self._create_empty_stats()
        # Si no existe el archivo, crear estadísticas vacías
        return self._create_empty_stats()

    def _create_empty_stats(self) -> Dict:
        """
        Crea una estructura vacía de estadísticas

        La estructura incluye:
        - Estadísticas generales (partidas jugadas/ganadas, puntuaciones)
        - Estadísticas por dificultad (Fácil, Medio, Difícil)
        - Historial de partidas recientes (máximo 50)

        Returns:
            Dict: Diccionario con estructura vacía de estadísticas
        """
        return {
            # === Estadísticas generales ===
            'games_played': 0,      # Total de partidas jugadas
            'games_won': 0,         # Total de partidas ganadas
            'total_score': 0,       # Suma de todas las puntuaciones
            'best_score': 0,        # Mejor puntuación general
            'best_time': None,      # Mejor tiempo general (en segundos)

            # === Estadísticas por nivel de dificultad ===
            'by_difficulty': {
                'Fácil': {
                    'played': 0,        # Partidas jugadas en este nivel
                    'won': 0,           # Partidas ganadas en este nivel
                    'best_score': 0,    # Mejor puntuación en este nivel
                    'best_time': None,  # Mejor tiempo en este nivel (segundos)
                    'avg_time': 0       # Tiempo promedio en este nivel (segundos)
                },
                'Medio': {
                    'played': 0,
                    'won': 0,
                    'best_score': 0,
                    'best_time': None,
                    'avg_time': 0
                },
                'Difícil': {
                    'played': 0,
                    'won': 0,
                    'best_score': 0,
                    'best_time': None,
                    'avg_time': 0
                }
            },

            # === Historial de partidas (máximo 50 últimas) ===
            'history': []
        }

    def _save_stats(self):
        """
        Guarda las estadísticas en el archivo JSON

        El archivo se guarda con formato legible (indentado) y
        codificación UTF-8 para soportar caracteres especiales como
        acentos y la ñ.
        """
        try:
            # Abrir archivo en modo escritura con codificación UTF-8
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                # Guardar JSON con indentación de 2 espacios
                # ensure_ascii=False permite guardar caracteres especiales
                json.dump(self.stats, f, indent=2, ensure_ascii=False)
        except IOError as e:
            # Mostrar error si no se puede guardar el archivo
            print(f"Error al guardar estadísticas: {e}")

    def record_game(self, difficulty: str, won: bool, score: int,
                   time_seconds: int, hints_used: int):
        """
        Registra una partida completada y actualiza todas las estadísticas

        Esta función realiza las siguientes operaciones:
        1. Actualiza estadísticas generales (partidas, victorias, puntuaciones)
        2. Actualiza estadísticas específicas por dificultad
        3. Agrega la partida al historial
        4. Guarda todo en el archivo JSON

        Args:
            difficulty (str): Nivel de dificultad ('Fácil', 'Medio', 'Difícil')
            won (bool): True si el jugador ganó la partida
            score (int): Puntuación obtenida en la partida
            time_seconds (int): Tiempo transcurrido en segundos
            hints_used (int): Cantidad de pistas usadas durante la partida
        """
        # --- PASO 1: Actualizar estadísticas generales ---
        self.stats['games_played'] += 1  # Incrementar contador de partidas

        # Solo actualizar estas estadísticas si ganó
        if won:
            self.stats['games_won'] += 1  # Incrementar contador de victorias
            self.stats['total_score'] += score  # Sumar puntuación al total

            # Actualizar mejor puntuación si la actual es mayor
            if score > self.stats['best_score']:
                self.stats['best_score'] = score

            # Actualizar mejor tiempo si la actual es menor
            # (None significa que es la primera victoria registrada)
            if self.stats['best_time'] is None or time_seconds < self.stats['best_time']:
                self.stats['best_time'] = time_seconds

        # --- PASO 2: Actualizar estadísticas por dificultad ---
        # Obtener el diccionario de estadísticas para esta dificultad específica
        diff_stats = self.stats['by_difficulty'][difficulty]
        diff_stats['played'] += 1  # Incrementar partidas jugadas en este nivel

        # Solo actualizar estadísticas de victoria si ganó
        if won:
            diff_stats['won'] += 1  # Incrementar victorias en este nivel

            # Actualizar mejor puntuación de esta dificultad
            if score > diff_stats['best_score']:
                diff_stats['best_score'] = score

            # Actualizar mejor tiempo de esta dificultad
            if diff_stats['best_time'] is None or time_seconds < diff_stats['best_time']:
                diff_stats['best_time'] = time_seconds

            # Calcular nuevo tiempo promedio usando fórmula de promedio ponderado
            # Fórmula: nuevo_promedio = (promedio_anterior * (n-1) + nuevo_valor) / n
            total_won = diff_stats['won']  # n = número total de victorias
            current_avg = diff_stats['avg_time']  # promedio anterior
            diff_stats['avg_time'] = ((current_avg * (total_won - 1)) + time_seconds) / total_won

        # --- PASO 3: Agregar partida al historial ---
        # Crear un registro de la partida con todos los datos
        game_record = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Fecha y hora actual
            'difficulty': difficulty,  # Dificultad jugada
            'won': won,  # Si ganó o no
            'score': score,  # Puntuación obtenida
            'time': time_seconds,  # Tiempo en segundos
            'hints_used': hints_used  # Pistas usadas
        }
        self.stats['history'].append(game_record)  # Agregar al historial

        # Mantener solo las últimas 50 partidas (eliminar las más antiguas)
        if len(self.stats['history']) > 50:
            self.stats['history'] = self.stats['history'][-50:]

        # --- PASO 4: Guardar todos los cambios ---
        self._save_stats()  # Escribir el archivo JSON actualizado

    def get_stats(self) -> Dict:
        """
        Retorna todas las estadísticas del juego

        Returns:
            Dict: Diccionario completo con todas las estadísticas
        """
        return self.stats

    def get_win_rate(self) -> float:
        """
        Calcula el porcentaje de victorias

        Formula: (partidas_ganadas / partidas_jugadas) * 100

        Returns:
            float: Porcentaje de victorias (0.0 a 100.0)
        """
        # Verificar división por cero
        if self.stats['games_played'] == 0:
            return 0.0
        # Calcular porcentaje
        return (self.stats['games_won'] / self.stats['games_played']) * 100

    def get_average_score(self) -> float:
        """
        Calcula la puntuación promedio de las partidas ganadas

        Formula: suma_total_puntuaciones / partidas_ganadas

        Returns:
            float: Puntuación promedio
        """
        # Verificar división por cero
        if self.stats['games_won'] == 0:
            return 0.0
        # Calcular promedio
        return self.stats['total_score'] / self.stats['games_won']

    def get_recent_games(self, count: int = 10) -> List[Dict]:
        """
        Retorna las últimas N partidas del historial

        Args:
            count (int): Cantidad de partidas a retornar (default: 10)

        Returns:
            List[Dict]: Lista de las últimas N partidas
        """
        # Usar notación de slice [-count:] para obtener los últimos N elementos
        return self.stats['history'][-count:]

    def reset_stats(self):
        """
        Reinicia todas las estadísticas a cero

        Esta función borra todas las estadísticas guardadas y
        crea una estructura vacía nueva.
        """
        self.stats = self._create_empty_stats()  # Crear estadísticas vacías
        self._save_stats()  # Guardar el archivo JSON vacío

    def format_time(self, seconds: Optional[int]) -> str:
        """
        Formatea tiempo en segundos al formato MM:SS

        Args:
            seconds (Optional[int]): Tiempo en segundos (puede ser None)

        Returns:
            str: Tiempo formateado como "MM:SS" o "--:--" si es None

        Ejemplos:
            format_time(125) -> "02:05"
            format_time(3661) -> "61:01"
            format_time(None) -> "--:--"
        """
        # Si es None, retornar formato vacío
        if seconds is None:
            return "--:--"

        # Calcular minutos y segundos usando división y módulo
        minutes = seconds // 60  # División entera
        secs = seconds % 60      # Resto de la división

        # Formatear con 2 dígitos (padding con ceros)
        return f"{minutes:02d}:{secs:02d}"

    def get_stats_summary(self) -> str:
        """
        Genera un resumen textual de todas las estadísticas

        Este método crea un texto formateado con bordes decorativos
        que muestra todas las estadísticas del juego.

        Returns:
            str: Texto formateado con el resumen de estadísticas
        """
        summary = []  # Lista para construir el texto línea por línea

        # Encabezado con bordes
        summary.append("═══════════════════════════════════════")
        summary.append("           ESTADÍSTICAS")
        summary.append("═══════════════════════════════════════")

        # Estadísticas generales
        summary.append(f"Partidas jugadas: {self.stats['games_played']}")
        summary.append(f"Partidas ganadas: {self.stats['games_won']}")
        summary.append(f"Tasa de victoria: {self.get_win_rate():.1f}%")
        summary.append(f"Mejor puntuación: {self.stats['best_score']}")
        summary.append(f"Mejor tiempo: {self.format_time(self.stats['best_time'])}")
        summary.append(f"Puntuación promedio: {self.get_average_score():.0f}")

        # Separador
        summary.append("")
        summary.append("Por dificultad:")

        # Iterar sobre cada nivel de dificultad
        for difficulty in ['Fácil', 'Medio', 'Difícil']:
            # Obtener estadísticas de esta dificultad
            diff_stats = self.stats['by_difficulty'][difficulty]

            # Agregar información formateada
            summary.append(f"\n  {difficulty}:")
            summary.append(f"    Jugadas: {diff_stats['played']} | Ganadas: {diff_stats['won']}")
            summary.append(f"    Mejor puntuación: {diff_stats['best_score']}")
            summary.append(f"    Mejor tiempo: {self.format_time(diff_stats['best_time'])}")

        # Pie con borde
        summary.append("═══════════════════════════════════════")

        # Unir todas las líneas con saltos de línea
        return "\n".join(summary)
