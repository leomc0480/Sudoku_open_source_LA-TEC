"""
Sistema de gestión de estadísticas del juego

Este módulo maneja todo lo relacionado con guardar, cargar y calcular
las estadísticas del juego de Sudoku. Las estadísticas se guardan en
un archivo JSON para persistencia entre sesiones.
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
        stats (Dict): Diccionario con todas las estadísticas
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
                # Si hay error, crear estadísticas vacías
                return self._create_empty_stats()
        # Si no existe el archivo, crear estadísticas vacías
        return self._create_empty_stats()

    def _create_empty_stats(self) -> Dict:
        """
        Crea una estructura vacía de estadísticas

        La estructura incluye:
        - Estadísticas generales (partidas jugadas/ganadas, puntuaciones)
        - Estadísticas por dificultad (Fácil, Medio, Difícil)
        - Historial de partidas recientes

        Returns:
            Dict: Diccionario con estructura vacía de estadísticas
        """
        return {
            # Estadísticas generales
            'games_played': 0,      # Total de partidas jugadas
            'games_won': 0,         # Total de partidas ganadas
            'total_score': 0,       # Suma de todas las puntuaciones
            'best_score': 0,        # Mejor puntuación general
            'best_time': None,      # Mejor tiempo general (en segundos)

            # Estadísticas por nivel de dificultad
            'by_difficulty': {
                'Fácil': {
                    'played': 0,        # Partidas jugadas en este nivel
                    'won': 0,           # Partidas ganadas en este nivel
                    'best_score': 0,    # Mejor puntuación en este nivel
                    'best_time': None,  # Mejor tiempo en este nivel
                    'avg_time': 0       # Tiempo promedio en este nivel
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

            # Historial de partidas (máximo 50 últimas)
            'history': []
        }

    def _save_stats(self):
        """
        Guarda las estadísticas en el archivo JSON

        El archivo se guarda con formato legible (indentado) y
        codificación UTF-8 para soportar caracteres especiales.
        """
        try:
            # Abrir archivo en modo escritura con codificación UTF-8
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                # Guardar JSON con indentación y caracteres especiales
                json.dump(self.stats, f, indent=2, ensure_ascii=False)
        except IOError as e:
            # Mostrar error si no se puede guardar
            print(f"Error al guardar estadísticas: {e}")

    def record_game(self, difficulty: str, won: bool, score: int, time_seconds: int, hints_used: int):
        """
        Registra una partida completada

        Args:
            difficulty: Nivel de dificultad
            won: Si se ganó el juego
            score: Puntuación obtenida
            time_seconds: Tiempo en segundos
            hints_used: Cantidad de pistas usadas
        """
        # Actualizar estadísticas generales
        self.stats['games_played'] += 1 
        if won:
            self.stats['games_won'] += 1
            self.stats['total_score'] += score

            # Actualizar mejor puntuación
            if score > self.stats['best_score']:
                self.stats['best_score'] = score

            # Actualizar mejor tiempo
            if self.stats['best_time'] is None or time_seconds < self.stats['best_time']:
                self.stats['best_time'] = time_seconds

        # Actualizar estadísticas por dificultad
        diff_stats = self.stats['by_difficulty'][difficulty]
        diff_stats['played'] += 1

        if won:
            diff_stats['won'] += 1

            # Mejor puntuación de la dificultad
            if score > diff_stats['best_score']:
                diff_stats['best_score'] = score

            # Mejor tiempo de la dificultad
            if diff_stats['best_time'] is None or time_seconds < diff_stats['best_time']:
                diff_stats['best_time'] = time_seconds

            # Calcular tiempo promedio
            total_won = diff_stats['won']
            current_avg = diff_stats['avg_time']
            diff_stats['avg_time'] = ((current_avg * (total_won - 1)) + time_seconds) / total_won

        # Agregar a historial
        game_record = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'difficulty': difficulty,
            'won': won,
            'score': score,
            'time': time_seconds,
            'hints_used': hints_used
        }
        self.stats['history'].append(game_record)

        # Mantener solo los últimos 50 juegos en el historial
        if len(self.stats['history']) > 50:
            self.stats['history'] = self.stats['history'][-50:]

        # Guardar cambios
        self._save_stats()

    def get_stats(self) -> Dict:
        """Retorna todas las estadísticas"""
        return self.stats

    def get_win_rate(self) -> float:
        """Calcula el porcentaje de victorias"""
        if self.stats['games_played'] == 0:
            return 0.0
        return (self.stats['games_won'] / self.stats['games_played']) * 100

    def get_average_score(self) -> float:
        """Calcula la puntuación promedio"""
        if self.stats['games_won'] == 0:
            return 0.0
        return self.stats['total_score'] / self.stats['games_won']

    def get_recent_games(self, count: int = 10) -> List[Dict]:
        """Retorna los últimos N juegos"""
        return self.stats['history'][-count:]

    def reset_stats(self):
        """Reinicia todas las estadísticas"""
        self.stats = self._create_empty_stats()
        self._save_stats()

    def format_time(self, seconds: int) -> str:
        """Formatea segundos en formato MM:SS"""
        if seconds is None:
            return "--:--"
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    def get_stats_summary(self) -> str:
        """Genera un resumen de estadísticas en texto"""
        summary = []
        summary.append("═══════════════════════════════════════")
        summary.append("           ESTADÍSTICAS")
        summary.append("═══════════════════════════════════════")
        summary.append(f"Partidas jugadas: {self.stats['games_played']}")
        summary.append(f"Partidas ganadas: {self.stats['games_won']}")
        summary.append(f"Tasa de victoria: {self.get_win_rate():.1f}%")
        summary.append(f"Mejor puntuación: {self.stats['best_score']}")
        summary.append(f"Mejor tiempo: {self.format_time(self.stats['best_time'])}")
        summary.append(f"Puntuación promedio: {self.get_average_score():.0f}")
        summary.append("")
        summary.append("Por dificultad:")

        for difficulty in ['Fácil', 'Medio', 'Difícil']:
            diff_stats = self.stats['by_difficulty'][difficulty]
            summary.append(f"\n  {difficulty}:")
            summary.append(f"    Jugadas: {diff_stats['played']} | Ganadas: {diff_stats['won']}")
            summary.append(f"    Mejor puntuación: {diff_stats['best_score']}")
            summary.append(f"    Mejor tiempo: {self.format_time(diff_stats['best_time'])}")

        summary.append("═══════════════════════════════════════")
        return "\n".join(summary)
