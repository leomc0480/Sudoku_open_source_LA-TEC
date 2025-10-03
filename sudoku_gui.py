"""
Interfaz gráfica del juego de Sudoku usando tkinter
"""
import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional, Tuple
from sudoku_game import SudokuGame
from stats_manager import StatisticsManager
from config import *


class SudokuGUI:
    """Interfaz gráfica principal del juego"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(" Sudoku - Juego de Lógica")
        self.root.configure(bg=COLORS['bg'])
        self.root.resizable(False, False)

        self.game: Optional[SudokuGame] = None
        self.stats_manager = StatisticsManager()
        self.selected_cell: Optional[Tuple[int, int]] = None
        self.help_mode = False

        # Variables de UI
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.time_label = None
        self.score_label = None
        self.hints_label = None

        # Mostrar pantalla de inicio
        self.show_start_screen()

    def show_start_screen(self):
        """Muestra la pantalla de inicio con selección de dificultad"""
        start_frame = tk.Frame(self.root, bg=COLORS['bg'])
        start_frame.pack(padx=40, pady=40)

        # Título
        title = tk.Label(
            start_frame,
            text="🧩 SUDOKU",
            font=('Arial', 48, 'bold'),
            fg=COLORS['title'],
            bg=COLORS['bg']
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            start_frame,
            text="Entrena tu mente con el juego de lógica",
            font=('Arial', 14),
            fg='#666',
            bg=COLORS['bg']
        )
        subtitle.pack(pady=5)

        # Selección de dificultad
        diff_label = tk.Label(
            start_frame,
            text="Selecciona la dificultad:",
            font=('Arial', 16, 'bold'),
            bg=COLORS['bg']
        )
        diff_label.pack(pady=(30, 15))

        # Botones de dificultad
        difficulties = [
            ('Fácil', '🟢', 'Para principiantes'),
            ('Medio', '🟡', 'Desafío moderado'),
            ('Difícil', '🔴', 'Para expertos')
        ]

        for diff, emoji, desc in difficulties:
            btn_frame = tk.Frame(start_frame, bg=COLORS['bg'])
            btn_frame.pack(pady=8)

            btn = tk.Button(
                btn_frame,
                text=f"{emoji} {diff}",
                font=('Arial', 18, 'bold'),
                bg=COLORS['button_bg'],
                fg=COLORS['button_text'],
                activebackground=COLORS['button_hover'],
                activeforeground=COLORS['button_text'],
                width=20,
                height=2,
                cursor='hand2',
                relief=tk.RAISED,
                bd=3,
                command=lambda d=diff: self.start_game(d, start_frame)
            )
            btn.pack()

            desc_label = tk.Label(
                btn_frame,
                text=desc,
                font=('Arial', 10),
                fg='#888',
                bg=COLORS['bg']
            )
            desc_label.pack()

            # Hover effects
            def on_enter(e, button=btn):
                button['background'] = COLORS['button_hover']

            def on_leave(e, button=btn):
                button['background'] = COLORS['button_bg']

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

        # Botón de estadísticas
        stats_btn = tk.Button(
            start_frame,
            text="📊 Ver Estadísticas",
            font=('Arial', 12),
            bg='#4CAF50',
            fg='white',
            cursor='hand2',
            command=self.show_statistics
        )
        stats_btn.pack(pady=(30, 10))

    def start_game(self, difficulty: str, start_frame: tk.Frame):
        """Inicia un nuevo juego con la dificultad seleccionada"""
        start_frame.destroy()
        self.game = SudokuGame(difficulty)
        self.create_game_ui()

    def create_game_ui(self):
        """Crea la interfaz principal del juego"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=COLORS['bg'])
        main_frame.pack(padx=20, pady=20)

        # Encabezado
        self.create_header(main_frame)

        # Panel de información
        self.create_info_panel(main_frame)

        # Tablero de Sudoku
        self.create_board(main_frame)

        # Panel de controles
        self.create_control_panel(main_frame)

        # Iniciar actualización de tiempo
        self.update_time()

    def create_header(self, parent):
        """Crea el encabezado con título y dificultad"""
        header_frame = tk.Frame(parent, bg=COLORS['bg'])
        header_frame.pack(pady=(0, 10))

        title = tk.Label(
            header_frame,
            text="🧩 SUDOKU",
            font=('Arial', 24, 'bold'),
            fg=COLORS['title'],
            bg=COLORS['bg']
        )
        title.pack()

        diff_label = tk.Label(
            header_frame,
            text=f"Dificultad: {self.game.difficulty}",
            font=('Arial', 14),
            fg='#666',
            bg=COLORS['bg']
        )
        diff_label.pack()

    def create_info_panel(self, parent):
        """Crea el panel de información (tiempo, pistas, etc.)"""
        info_frame = tk.Frame(parent, bg=COLORS['stats_bg'], relief=tk.RIDGE, bd=2)
        info_frame.pack(pady=10, fill=tk.X)

        # Tiempo
        time_frame = tk.Frame(info_frame, bg=COLORS['stats_bg'])
        time_frame.pack(side=tk.LEFT, padx=20, pady=10)
        tk.Label(time_frame, text="⏱️ Tiempo:", font=('Arial', 11), bg=COLORS['stats_bg']).pack()
        self.time_label = tk.Label(
            time_frame,
            text="00:00",
            font=('Arial', 16, 'bold'),
            fg=COLORS['title'],
            bg=COLORS['stats_bg']
        )
        self.time_label.pack()

        # Pistas usadas
        hints_frame = tk.Frame(info_frame, bg=COLORS['stats_bg'])
        hints_frame.pack(side=tk.LEFT, padx=20, pady=10)
        tk.Label(hints_frame, text="💡 Pistas:", font=('Arial', 11), bg=COLORS['stats_bg']).pack()
        self.hints_label = tk.Label(
            hints_frame,
            text="0",
            font=('Arial', 16, 'bold'),
            fg=COLORS['title'],
            bg=COLORS['stats_bg']
        )
        self.hints_label.pack()

        # Modo ayuda
        help_frame = tk.Frame(info_frame, bg=COLORS['stats_bg'])
        help_frame.pack(side=tk.LEFT, padx=20, pady=10)
        self.help_var = tk.BooleanVar()
        help_check = tk.Checkbutton(
            help_frame,
            text="🔍 Modo Ayuda",
            variable=self.help_var,
            font=('Arial', 11),
            bg=COLORS['stats_bg'],
            command=self.toggle_help_mode
        )
        help_check.pack()

    def create_board(self, parent):
        """Crea el tablero de Sudoku con celdas clickeables"""
        board_frame = tk.Frame(parent, bg=COLORS['grid_thick'], relief=tk.RAISED, bd=4)
        board_frame.pack(pady=10)

        for i in range(9):
            for j in range(9):
                # Frame para cada celda con borde
                cell_frame = tk.Frame(
                    board_frame,
                    bg=COLORS['grid_line'],
                    width=CELL_SIZE,
                    height=CELL_SIZE
                )

                # Bordes más gruesos para separar subcuadros 3x3
                padx = (3 if j % 3 == 0 else 1, 3 if j == 8 else 1)
                pady = (3 if i % 3 == 0 else 1, 3 if i == 8 else 1)

                cell_frame.grid(row=i, column=j, padx=padx, pady=pady)
                cell_frame.grid_propagate(False)

                # Etiqueta de la celda
                value = self.game.grid[i][j]
                text = str(value) if value != 0 else ""

                cell = tk.Label(
                    cell_frame,
                    text=text,
                    font=('Arial', 20, 'bold'),
                    bg=self.get_cell_color(i, j),
                    fg=self.get_cell_text_color(i, j),
                    cursor='hand2' if not self.game.is_fixed_cell(i, j) else 'arrow'
                )
                cell.pack(fill=tk.BOTH, expand=True)

                # Evento de click
                if not self.game.is_fixed_cell(i, j):
                    cell.bind('<Button-1>', lambda e, row=i, col=j: self.select_cell(row, col))

                self.cells[i][j] = cell

    def create_control_panel(self, parent):
        """Crea el panel de controles y teclado numérico"""
        control_frame = tk.Frame(parent, bg=COLORS['bg'])
        control_frame.pack(pady=10)

        # Teclado numérico
        num_frame = tk.Frame(control_frame, bg=COLORS['bg'])
        num_frame.pack(pady=10)

        tk.Label(
            num_frame,
            text="Selecciona un número:",
            font=('Arial', 12),
            bg=COLORS['bg']
        ).pack()

        num_buttons_frame = tk.Frame(num_frame, bg=COLORS['bg'])
        num_buttons_frame.pack(pady=5)

        for num in range(1, 10):
            btn = tk.Button(
                num_buttons_frame,
                text=str(num),
                font=('Arial', 16, 'bold'),
                width=3,
                height=1,
                bg='white',
                fg=COLORS['text_user'],
                cursor='hand2',
                relief=tk.RAISED,
                bd=2,
                command=lambda n=num: self.place_number(n)
            )
            btn.grid(row=(num - 1) // 3, column=(num - 1) % 3, padx=3, pady=3)

        # Botones de acción
        action_frame = tk.Frame(control_frame, bg=COLORS['bg'])
        action_frame.pack(pady=10)

        buttons = [
            ("🗑️ Borrar", self.clear_cell, '#FF9800'),
            ("💡 Pista", self.use_hint, '#4CAF50'),
            ("✅ Verificar", self.check_solution, '#2196F3'),
            ("🔄 Reiniciar", self.restart_game, '#9C27B0'),
            ("🏠 Menú", self.back_to_menu, '#757575')
        ]

        for text, command, color in buttons:
            btn = tk.Button(
                action_frame,
                text=text,
                font=('Arial', 11),
                bg=color,
                fg='white',
                cursor='hand2',
                width=12,
                command=command
            )
            btn.pack(side=tk.LEFT, padx=5)

    def get_cell_color(self, row: int, col: int) -> str:
        """Retorna el color de fondo de una celda según su estado"""
        state = self.game.get_cell_state(row, col)

        if self.selected_cell == (row, col):
            return COLORS['selected']
        elif state == 'fixed':
            return COLORS['fixed_cell']
        elif state == 'correct':
            return COLORS['correct']
        elif state == 'incorrect':
            return COLORS['incorrect']
        else:
            return COLORS['grid_bg']

    def get_cell_text_color(self, row: int, col: int) -> str:
        """Retorna el color del texto de una celda"""
        if self.game.is_fixed_cell(row, col):
            return COLORS['text_fixed']
        return COLORS['text_user']

    def select_cell(self, row: int, col: int):
        """Selecciona una celda"""
        if self.game.game_over:
            return

        # Deseleccionar anterior
        if self.selected_cell:
            old_row, old_col = self.selected_cell
            self.cells[old_row][old_col]['bg'] = self.get_cell_color(old_row, old_col)

        # Seleccionar nueva
        self.selected_cell = (row, col)
        self.cells[row][col]['bg'] = COLORS['selected']

    def place_number(self, num: int):
        """Coloca un número en la celda seleccionada"""
        if not self.selected_cell or self.game.game_over:
            return

        row, col = self.selected_cell

        # Verificar con modo ayuda si está activado
        if self.help_var.get():
            is_valid, message = self.game.validate_current_move(row, col, num)
            if not is_valid:
                messagebox.showwarning("Movimiento Incorrecto", message)
                return

        # Colocar número
        success, message = self.game.make_move(row, col, num)
        if success:
            self.cells[row][col]['text'] = str(num)
            self.update_board()

    def clear_cell(self):
        """Borra el contenido de la celda seleccionada"""
        if not self.selected_cell or self.game.game_over:
            return

        row, col = self.selected_cell
        if not self.game.is_fixed_cell(row, col):
            self.game.make_move(row, col, 0)
            self.cells[row][col]['text'] = ""
            self.update_board()

    def use_hint(self):
        """Usa una pista en la celda seleccionada"""
        if not self.selected_cell or self.game.game_over:
            messagebox.showinfo("Pista", "Selecciona una celda primero")
            return

        row, col = self.selected_cell
        hint = self.game.use_hint(row, col)

        if hint is None:
            messagebox.showinfo("Pista", "No puedes usar pistas en celdas fijas")
        else:
            self.game.make_move(row, col, hint)
            self.cells[row][col]['text'] = str(hint)
            self.hints_label['text'] = str(self.game.hints_used)
            self.update_board()
            messagebox.showinfo("Pista", f"El número correcto es: {hint}")

    def check_solution(self):
        """Verifica si el tablero está completo y correcto"""
        is_complete, errors = self.game.check_victory()

        if is_complete:
            score = self.game.calculate_score()
            time_seconds = self.game.get_elapsed_time()

            # Guardar estadísticas
            self.stats_manager.record_game(
                self.game.difficulty,
                True,
                score,
                time_seconds,
                self.game.hints_used
            )

            # Actualizar colores
            self.update_board()

            # Mensaje de victoria
            time_str = self.stats_manager.format_time(time_seconds)
            message = f"🎉 ¡FELICITACIONES! 🎉\n\n"
            message += f"Has completado el Sudoku de nivel {self.game.difficulty}\n\n"
            message += f"⏱️ Tiempo: {time_str}\n"
            message += f"💡 Pistas usadas: {self.game.hints_used}\n"
            message += f"🏆 Puntuación: {score} puntos\n\n"
            message += "¿Quieres jugar otra partida?"

            response = messagebox.askyesno("¡Victoria!", message)
            if response:
                self.back_to_menu()
        else:
            if errors > 0:
                # Marcar errores
                self.update_board()
                messagebox.showerror(
                    "Errores encontrados",
                    f"Hay {errors} celda(s) incorrecta(s).\nEstán marcadas en rojo."
                )
            else:
                messagebox.showinfo(
                    "Incompleto",
                    "El tablero aún no está completo.\n¡Sigue adelante!"
                )

    def restart_game(self):
        """Reinicia el juego actual"""
        if messagebox.askyesno("Reiniciar", "¿Seguro que quieres reiniciar el juego?"):
            self.game.restart_game()
            self.selected_cell = None
            self.hints_label['text'] = "0"
            self.update_board()

    def back_to_menu(self):
        """Vuelve al menú principal"""
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Mostrar pantalla de inicio
        self.game = None
        self.selected_cell = None
        self.show_start_screen()

    def toggle_help_mode(self):
        """Activa/desactiva el modo ayuda"""
        self.help_mode = self.help_var.get()

    def update_board(self):
        """Actualiza la visualización del tablero"""
        for i in range(9):
            for j in range(9):
                value = self.game.grid[i][j]
                self.cells[i][j]['text'] = str(value) if value != 0 else ""
                self.cells[i][j]['bg'] = self.get_cell_color(i, j)
                self.cells[i][j]['fg'] = self.get_cell_text_color(i, j)

    def update_time(self):
        """Actualiza el contador de tiempo"""
        if self.game and not self.game.game_over:
            elapsed = self.game.get_elapsed_time()
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.time_label['text'] = f"{minutes:02d}:{seconds:02d}"
            self.root.after(1000, self.update_time)

    def show_statistics(self):
        """Muestra una ventana con las estadísticas"""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Estadísticas")
        stats_window.configure(bg=COLORS['bg'])
        stats_window.geometry("500x600")
        stats_window.resizable(False, False)

        # Texto de estadísticas
        stats_text = tk.Text(
            stats_window,
            font=('Courier New', 11),
            bg='white',
            fg='black',
            wrap=tk.WORD,
            padx=20,
            pady=20
        )
        stats_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        stats_summary = self.stats_manager.get_stats_summary()
        stats_text.insert('1.0', stats_summary)
        stats_text.config(state=tk.DISABLED)

        # Botón cerrar
        close_btn = tk.Button(
            stats_window,
            text="Cerrar",
            font=('Arial', 12),
            bg=COLORS['button_bg'],
            fg='white',
            cursor='hand2',
            command=stats_window.destroy
        )
        close_btn.pack(pady=10)

    def run(self):
        """Inicia el loop principal de la aplicación"""
        # Centrar ventana
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

        self.root.mainloop()
