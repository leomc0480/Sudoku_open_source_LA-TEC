# Sudoku - Juego de Lógica y Memoria

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Características](#-características)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Explicación Detallada del Código](#-explicación-detallada-del-código)
  - [1. config.py](#1-configpy---configuración-global)
  - [2. sudoku_generator.py](#2-sudoku_generatorpy---generador-de-tableros)
  - [3. sudoku_game.py](#3-sudoku_gamepy---lógica-del-juego)
  - [4. statistics.py](#4-statisticspy---gestión-de-estadísticas)
  - [5. sudoku_gui.py](#5-sudoku_guipy---interfaz-gráfica)
  - [6. main.py](#6-mainpy---punto-de-entrada)
- [Cómo Funciona el Código](#-cómo-funciona-el-código-paso-a-paso)
- [Conceptos de Programación Utilizados](#-conceptos-de-programación-utilizados)
- [Sistema de Puntuación](#-sistema-de-puntuación)
- [Reglas del Sudoku](#-reglas-del-sudoku)
- [Solución de Problemas](#-solución-de-problemas)
- [Créditos](#-créditos)

---

## Descripción del Proyecto

Este proyecto es un **juego completo de Sudoku** implementado en Python con interfaz gráfica usando **Tkinter**. El juego permite a los usuarios resolver tableros de Sudoku de diferentes niveles de dificultad mientras entrena sus habilidades cognitivas como la memoria de trabajo, razonamiento lógico y toma de decisiones.

### ¿Qué es Sudoku?

Sudoku es un juego de lógica que consiste en completar una cuadrícula de 9×9 celdas dividida en subcuadrículas de 3×3, con números del 1 al 9. El objetivo es llenar la cuadrícula de manera que:
- Cada fila contenga los números del 1 al 9 sin repetir
- Cada columna contenga los números del 1 al 9 sin repetir
- Cada subcuadrícula de 3×3 contenga los números del 1 al 9 sin repetir

---
### Funcionalidades del Juego

-  **Interfaz gráfica moderna**: Ventana bonita y colorida con tkinter (no es consola)
-  **3 niveles de dificultad**: Fácil, Medio y Difícil
-  **Completamente interactivo**: Click para seleccionar celdas y números
-  **Generación automática de tableros**: Cada partida es única
-  **Validación en tiempo real**: Verifica que las reglas se cumplan
-  **Modo ayuda**: Valida si tu movimiento es correcto
-  **Sistema de pistas**: Revela el número correcto en una celda
-  **Cronómetro**: Mide tu tiempo de resolución
-  **Sistema de puntuación**: Basado en tiempo, errores y pistas usadas
-  **Retroalimentación visual**: Celdas correctas (verde) e incorrectas (rojo)
-  **Estadísticas persistentes**: Se guardan automáticamente en JSON
-  **Historial de partidas**: Guarda las últimas 50 partidas

###  Características Técnicas

- Arquitectura modular con separación de responsabilidades
- Algoritmo de backtracking para generar tableros válidos
- Persistencia de datos con JSON
- Interfaz responsive con eventos de click y hover
- Manejo de errores robusto
- Código documentado y comentado

---

### Software Necesario

- **Python 3.7 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **Tkinter**: Viene incluido con Python (no requiere instalación adicional)

### Sistemas Operativos Compatibles

-  Windows 7/8/10/11
-  macOS 10.12+
-  Linux (Ubuntu, Debian, Fedora, etc.)

### Verificar Instalación de Python

```bash
python --version
# O en algunos sistemas:
python3 --version
```

---

### Paso 1: Descargar el Proyecto

Descarga todos los archivos del proyecto en una carpeta:

```
Proyect_Sudoku/
├── main.py
├── config.py
├── sudoku_generator.py
├── sudoku_game.py
├── sudoku_gui.py
├── statistics.py
└── README.md
```

### Paso 2: Navegar a la Carpeta del Proyecto

Abre una terminal o línea de comandos y navega hasta la carpeta del proyecto:

```bash
cd "ruta/a/tu/carpeta/Proyect_Sudoku"
```

### Paso 3: Ejecutar el Juego

```bash
python main.py
```

O en algunos sistemas:

```bash
python3 main.py
```

### ¡Listo! 

El juego se abrirá en una ventana nueva. Selecciona la dificultad y comienza a jugar.

---

## Crear Ejecutable (EXE/APP)

### ¿Qué es un Ejecutable?

Un **ejecutable** es un archivo que puede correr directamente sin necesidad de tener Python instalado. Es perfecto para:
-  Compartir el juego con amigos o familiares
-  Ejecutar en computadoras sin Python
-  Distribución fácil (solo un archivo .exe)

### Opción 1: Usando el Script Automático (Windows)

**Paso 1**: Doble click en el archivo `build_exe.bat`

**Paso 2**: Espera a que termine (puede tardar 1-2 minutos)

**Paso 3**: El ejecutable estará en la carpeta `dist/Sudoku.exe`

### Opción 2: Usando el Script Automático (Linux/Mac)

```bash
# Dar permisos de ejecución
chmod +x build_exe.sh

# Ejecutar el script
./build_exe.sh
```

El ejecutable estará en `dist/Sudoku`

### Opción 3: Manual con PyInstaller

**Paso 1**: Instalar PyInstaller
```bash
pip install pyinstaller
```

**Paso 2**: Generar el ejecutable
```bash
# Windows - Crear Sudoku.exe
pyinstaller --onefile --windowed --name "Sudoku" main.py

# Linux/Mac - Crear ejecutable Sudoku
pyinstaller --onefile --windowed --name "Sudoku" main.py
```

**Paso 3**: Encuentra tu ejecutable
```
dist/
└── Sudoku.exe    # Windows
    o
└── Sudoku        # Linux/Mac
```

### ¿Qué significan los parámetros?

- `--onefile`: Crea un solo archivo ejecutable (todo incluido)
- `--windowed`: No muestra la consola negra, solo la ventana del juego
- `--name "Sudoku"`: Nombre del archivo ejecutable

### Distribución del Ejecutable

Una vez creado, puedes:

1. **Copiar el archivo** `Sudoku.exe` a cualquier carpeta
2. **Compartirlo** con USB, correo, etc.
3. **Ejecutarlo** haciendo doble click (no necesita Python)

⚠️ **Importante**:
- El archivo es grande (20-40 MB) porque incluye Python y todas las librerías
- Windows puede mostrar advertencia de seguridad (es normal, tu lo creaste)
- El primer inicio puede tardar unos segundos

### Crear con Ícono Personalizado (Opcional)

Si tienes un archivo de ícono (.ico):

```bash
pyinstaller --onefile --windowed --name "Sudoku" --icon=sudoku_icon.ico main.py
```

---

## Estructura del Proyecto

```
Proyect_Sudoku/
│
├── main.py                 # Punto de entrada principal
├── config.py               # Configuración global (colores, constantes)
├── sudoku_generator.py     # Generador de tableros Sudoku
├── sudoku_game.py          # Lógica del juego
├── sudoku_gui.py           # Interfaz gráfica con Tkinter
├── statistics.py           # Gestión de estadísticas
├── sudoku_stats.json       # Archivo de estadísticas (se crea automáticamente)
└── README.md               # Este archivo
```

---

## Explicación Detallada del Código

### 1. config.py - Configuración Global

**Propósito**: Almacenar todas las constantes del juego en un solo lugar.

#### Variables Principales

```python
# Colores del juego
COLORS = {
    'bg': '#F0F0F0',           # Fondo general
    'grid_bg': '#FFFFFF',       # Fondo de celdas
    'fixed_cell': '#E8E8E8',   # Celdas fijas (iniciales)
    'selected': '#BBE5FF',      # Celda seleccionada
    'correct': '#C8E6C9',       # Celda correcta (verde)
    'incorrect': '#FFCDD2',     # Celda incorrecta (rojo)
    # ... más colores
}

# Dimensiones
CELL_SIZE = 60            # Tamaño de cada celda en píxeles
GRID_SIZE = 9             # Tamaño del tablero (9x9)
WINDOW_WIDTH = 800        # Ancho de la ventana
WINDOW_HEIGHT = 700       # Alto de la ventana

# Dificultades (cantidad de celdas vacías)
DIFFICULTY_LEVELS = {
    'Fácil': 30,          # 30 celdas vacías
    'Medio': 45,          # 45 celdas vacías
    'Difícil': 55         # 55 celdas vacías
}

# Sistema de puntuación
BASE_SCORE = 1000           # Puntuación base
TIME_BONUS_POINTS = 1       # +1 punto cada 5 segundos restantes
ERROR_PENALTY = 5           # -5 puntos por error
HINT_PENALTY = 10           # -10 puntos por pista usada
```

**¿Por qué usar un archivo de configuración?**

-  **Mantenibilidad**: Cambiar colores o valores en un solo lugar
-  **Legibilidad**: Valores con nombres descriptivos
-  **Reutilización**: Importar desde cualquier módulo

---

### 2. sudoku_generator.py - Generador de Tableros

**Propósito**: Generar tableros válidos de Sudoku con solución única.

#### Clase Principal: `SudokuGenerator`

##### Función: `generate(empty_cells)`

**¿Qué hace?**
Genera un tablero de Sudoku completo y luego remueve celdas para crear el puzzle.

**Parámetros**:
- `empty_cells` (int): Cantidad de celdas vacías (define dificultad)

**Retorna**:
- Tupla con dos matrices 9x9:
  1. `puzzle`: Tablero con celdas vacías para jugar
  2. `solution`: Tablero completo con la solución

**Algoritmo**:

1. **Crear tablero vacío**: Matriz 9x9 con ceros
   ```python
   self.grid = [[0 for _ in range(9)] for _ in range(9)]
   ```

2. **Llenar tablero usando backtracking** (método `_fill_grid()`):
   - Para cada celda vacía:
     - Probar números del 1-9 en orden aleatorio
     - Verificar si el número es válido (no se repite en fila/columna/subcuadro)
     - Si es válido, colocarlo y continuar recursivamente
     - Si no hay solución, retroceder (backtrack) y probar otro número

3. **Copiar solución**:
   ```python
   solution = [row[:] for row in self.grid]
   ```

4. **Remover celdas aleatoriamente**:
   - Crear lista de todas las posiciones (81 celdas)
   - Mezclar aleatoriamente
   - Poner 0 en las primeras N posiciones

**Ejemplo de uso**:
```python
generator = SudokuGenerator()
puzzle, solution = generator.generate(30)  # Genera puzzle fácil
```

##### Función: `_is_valid(row, col, num)`

**¿Qué hace?**
Verifica si un número puede colocarse en una posición según las reglas del Sudoku.

**Parámetros**:
- `row` (int): Fila (0-8)
- `col` (int): Columna (0-8)
- `num` (int): Número a validar (1-9)

**Retorna**:
- `True` si es válido, `False` si no lo es

**Verifica**:
1. **Fila**: El número no existe en la fila
   ```python
   if num in self.grid[row]:
       return False
   ```

2. **Columna**: El número no existe en la columna
   ```python
   if num in [self.grid[i][col] for i in range(9)]:
       return False
   ```

3. **Subcuadro 3x3**: El número no existe en el subcuadro
   ```python
   box_row, box_col = 3 * (row // 3), 3 * (col // 3)
   for i in range(box_row, box_row + 3):
       for j in range(box_col, box_col + 3):
           if self.grid[i][j] == num:
               return False
   ```

#### Funciones Auxiliares Globales

##### Función: `validate_move(grid, row, col, num, solution)`

Valida si un movimiento del jugador es correcto.

**Dos modos de validación**:
1. **Con solución**: Compara directamente con la solución correcta
2. **Sin solución**: Solo verifica que no rompa las reglas básicas

##### Función: `check_complete(grid, solution)`

Verifica si el tablero está completo y cuenta errores.

**Retorna**: `(está_completo, cantidad_de_errores)`

---

### 3. sudoku_game.py - Lógica del Juego

**Propósito**: Manejar el estado del juego, movimientos y puntuación.

#### Clase Principal: `SudokuGame`

##### Constructor: `__init__(difficulty)`

**Inicializa una nueva partida**:

```python
def __init__(self, difficulty: str):
    self.difficulty = difficulty       # 'Fácil', 'Medio', o 'Difícil'
    self.grid = []                     # Tablero actual
    self.solution = []                 # Solución correcta
    self.initial_grid = []             # Tablero inicial (celdas fijas)
    self.start_time = time.time()     # Tiempo de inicio
    self.hints_used = 0                # Contador de pistas
    self.game_over = False             # ¿Juego terminado?
    self.won = False                   # ¿Ganó el juego?
```

##### Función: `make_move(row, col, num)`

**¿Qué hace?**
Intenta colocar un número en una celda.

**Validaciones**:
1. Juego no terminado
2. Celda no es fija
3. Número válido (0 para borrar, 1-9 para colocar)

**Proceso**:
```python
if num == 0:  # Borrar celda
    self.grid[row][col] = 0
else:  # Colocar número
    self.grid[row][col] = num
```

**Retorna**: `(éxito, mensaje)`

##### Función: `use_hint(row, col)`

**¿Qué hace?**
Revela el número correcto de una celda.

**Proceso**:
1. Verificar que la celda no sea fija
2. Incrementar contador de pistas
3. Retornar el número correcto de la solución

```python
def use_hint(self, row: int, col: int) -> Optional[int]:
    if self.is_fixed_cell(row, col):
        return None
    self.hints_used += 1
    return self.solution[row][col]
```

##### Función: `calculate_score()`

**¿Qué hace?**
Calcula la puntuación final del juego.

**Fórmula**:
```
Puntuación = BASE_SCORE (1000)
           + Bonificación de tiempo
           - Penalización por pistas

Bonificación de tiempo = (tiempo_restante // 5) * 1
Penalización por pistas = hints_used * 10
```

**Ejemplo**:
```
Dificultad: Medio (límite 40 minutos = 2400 segundos)
Tiempo usado: 1200 segundos (20 minutos)
Tiempo restante: 1200 segundos
Pistas usadas: 3

Cálculo:
  Base: 1000
  + Bonificación: (1200 // 5) * 1 = 240
  - Pistas: 3 * 10 = 30
  = 1000 + 240 - 30 = 1210 puntos
```

##### Función: `get_cell_state(row, col)`

**¿Qué hace?**
Determina el estado visual de una celda.

**Estados posibles**:
- `'fixed'`: Celda fija (del tablero inicial)
- `'empty'`: Celda vacía
- `'user'`: Celda llenada por el usuario
- `'correct'`: Celda correcta (al terminar)
- `'incorrect'`: Celda incorrecta (al terminar)

---

### 4. statistics.py - Gestión de Estadísticas

**Propósito**: Guardar y cargar estadísticas del juego en formato JSON.

#### Clase Principal: `StatisticsManager`

##### Estructura de Datos

```python
{
    "games_played": 10,           # Total partidas jugadas
    "games_won": 7,               # Total partidas ganadas
    "total_score": 7500,          # Suma de puntuaciones
    "best_score": 1250,           # Mejor puntuación
    "best_time": 456,             # Mejor tiempo (segundos)

    "by_difficulty": {
        "Fácil": {
            "played": 5,
            "won": 4,
            "best_score": 1100,
            "best_time": 300,
            "avg_time": 350.5
        },
        # ... Medio, Difícil
    },

    "history": [
        {
            "date": "2025-01-15 14:30:00",
            "difficulty": "Medio",
            "won": true,
            "score": 1150,
            "time": 1200,
            "hints_used": 2
        },
        # ... más partidas (máx 50)
    ]
}
```

##### Función: `record_game(difficulty, won, score, time_seconds, hints_used)`

**¿Qué hace?**
Registra una partida completada y actualiza todas las estadísticas.

**Proceso paso a paso**:

1. **Actualizar estadísticas generales**:
   ```python
   self.stats['games_played'] += 1
   if won:
       self.stats['games_won'] += 1
       self.stats['total_score'] += score
   ```

2. **Actualizar mejor puntuación**:
   ```python
   if score > self.stats['best_score']:
       self.stats['best_score'] = score
   ```

3. **Actualizar mejor tiempo**:
   ```python
   if self.stats['best_time'] is None or time_seconds < self.stats['best_time']:
       self.stats['best_time'] = time_seconds
   ```

4. **Actualizar estadísticas por dificultad**:
   ```python
   diff_stats = self.stats['by_difficulty'][difficulty]
   diff_stats['played'] += 1
   if won:
       diff_stats['won'] += 1
   ```

5. **Calcular tiempo promedio** (fórmula de promedio ponderado):
   ```python
   # Fórmula: nuevo_promedio = (promedio_anterior * (n-1) + nuevo_valor) / n
   total_won = diff_stats['won']
   current_avg = diff_stats['avg_time']
   diff_stats['avg_time'] = ((current_avg * (total_won - 1)) + time_seconds) / total_won
   ```

6. **Agregar al historial**:
   ```python
   game_record = {
       'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
       'difficulty': difficulty,
       'won': won,
       'score': score,
       'time': time_seconds,
       'hints_used': hints_used
   }
   self.stats['history'].append(game_record)
   ```

7. **Limitar historial a 50 partidas**:
   ```python
   if len(self.stats['history']) > 50:
       self.stats['history'] = self.stats['history'][-50:]
   ```

8. **Guardar en archivo JSON**:
   ```python
   self._save_stats()
   ```

##### Función: `get_win_rate()`

Calcula el porcentaje de victorias:
```python
if self.stats['games_played'] == 0:
    return 0.0
return (self.stats['games_won'] / self.stats['games_played']) * 100
```

##### Función: `format_time(seconds)`

Convierte segundos a formato MM:SS:
```python
if seconds is None:
    return "--:--"
minutes = seconds // 60
secs = seconds % 60
return f"{minutes:02d}:{secs:02d}"
```

---

### 5. sudoku_gui.py - Interfaz Gráfica

**Propósito**: Crear la interfaz visual del juego con Tkinter.

#### Clase Principal: `SudokuGUI`

##### Constructor: `__init__()`

```python
def __init__(self):
    self.root = tk.Tk()                          # Ventana principal
    self.root.title("🎮 Sudoku - Juego de Lógica")
    self.game = None                              # Instancia del juego
    self.stats_manager = StatisticsManager()      # Gestor de estadísticas
    self.selected_cell = None                     # Celda seleccionada
    self.cells = [[None for _ in range(9)] for _ in range(9)]  # Referencias a celdas
```

##### Función: `show_start_screen()`

**¿Qué hace?**
Muestra la pantalla inicial con los botones de dificultad.

**Estructura visual**:
```
╔════════════════════════════╗
║          SUDOKU           ║
║  Entrena tu mente...      ║
║                            ║
║  Selecciona dificultad:   ║
║                            ║
║  [🟢 Fácil              ]  ║
║   Para principiantes       ║
║                            ║
║  [🟡 Medio              ]  ║
║   Desafío moderado         ║
║                            ║
║  [🔴 Difícil            ]  ║
║   Para expertos            ║
║                            ║
║  [📊 Ver Estadísticas]    ║
╚════════════════════════════╝
```

**Código clave**:
```python
for diff, emoji, desc in difficulties:
    btn = tk.Button(
        ...,
        text=f"{emoji} {diff}",
        command=lambda d=diff: self.start_game(d, start_frame)
    )
```

##### Función: `create_board(parent)`

**¿Qué hace?**
Crea el tablero visual de 9x9 con celdas clickeables.

**Proceso**:
1. Crear un Frame con borde grueso
2. Para cada celda (i, j):
   - Crear Frame individual
   - Aplicar bordes más gruesos cada 3 celdas (subcuadros 3x3)
   - Crear Label con el número
   - Asignar color según estado de la celda
   - Vincular evento de click

**Código clave**:
```python
for i in range(9):
    for j in range(9):
        # Bordes más gruesos para subcuadros
        padx = (3 if j % 3 == 0 else 1, 3 if j == 8 else 1)
        pady = (3 if i % 3 == 0 else 1, 3 if i == 8 else 1)

        cell = tk.Label(...)
        cell.bind('<Button-1>', lambda e, row=i, col=j: self.select_cell(row, col))
        self.cells[i][j] = cell
```

##### Función: `create_control_panel(parent)`

**¿Qué hace?**
Crea el teclado numérico y botones de acción.

**Botones**:
- **Números 1-9**: Para colocar en la celda seleccionada
- **Borrar**: Limpia la celda seleccionada
- **Pista**: Revela el número correcto
- **Verificar**: Revisa si el tablero es correcto
- **Reiniciar**: Reinicia el juego actual
- **Menú**: Vuelve al menú principal

##### Función: `select_cell(row, col)`

**¿Qué hace?**
Selecciona una celda al hacer click.

**Proceso**:
1. Deseleccionar celda anterior (restaurar color)
2. Seleccionar nueva celda (color azul)
3. Guardar posición seleccionada

```python
# Deseleccionar anterior
if self.selected_cell:
    old_row, old_col = self.selected_cell
    self.cells[old_row][old_col]['bg'] = self.get_cell_color(old_row, old_col)

# Seleccionar nueva
self.selected_cell = (row, col)
self.cells[row][col]['bg'] = COLORS['selected']
```

##### Función: `place_number(num)`

**¿Qué hace?**
Coloca un número en la celda seleccionada.

**Proceso**:
1. Verificar que hay celda seleccionada
2. Si modo ayuda activo, validar el número
3. Colocar número en el juego
4. Actualizar visualización

```python
if self.help_var.get():  # Modo ayuda activo
    is_valid, message = self.game.validate_current_move(row, col, num)
    if not is_valid:
        messagebox.showwarning("Movimiento Incorrecto", message)
        return

success, message = self.game.make_move(row, col, num)
if success:
    self.cells[row][col]['text'] = str(num)
```

##### Función: `check_solution()`

**¿Qué hace?**
Verifica si el tablero está completo y correcto.

**Proceso**:
1. Llamar a `game.check_victory()`
2. Si ganó:
   - Calcular puntuación
   - Guardar estadísticas
   - Mostrar mensaje de victoria
   - Ofrecer jugar otra partida
3. Si hay errores:
   - Actualizar colores (rojo para incorrectas)
   - Mostrar cantidad de errores
4. Si incompleto:
   - Informar al usuario

**Mensaje de victoria**:
```python
message = f"🎉 ¡FELICITACIONES! 🎉\n\n"
message += f"Has completado el Sudoku de nivel {self.game.difficulty}\n\n"
message += f"⏱️ Tiempo: {time_str}\n"
message += f"💡 Pistas usadas: {self.game.hints_used}\n"
message += f"🏆 Puntuación: {score} puntos\n\n"
```

##### Función: `update_time()`

**¿Qué hace?**
Actualiza el cronómetro cada segundo.

**Proceso**:
1. Obtener tiempo transcurrido
2. Formatear como MM:SS
3. Actualizar etiqueta
4. Programar siguiente actualización (recursión con after)

```python
def update_time(self):
    if self.game and not self.game.game_over:
        elapsed = self.game.get_elapsed_time()
        minutes = elapsed // 60
        seconds = elapsed % 60
        self.time_label['text'] = f"{minutes:02d}:{seconds:02d}"
        self.root.after(1000, self.update_time)  # Llamar de nuevo en 1 segundo
```

---

### 6. main.py - Punto de Entrada

**Propósito**: Iniciar la aplicación.

```python
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
```

**¿Qué hace `if __name__ == "__main__"`?**
- Verifica que el archivo se está ejecutando directamente (no importado)
- Permite que los módulos se importen sin ejecutar código automáticamente

---

## Cómo Funciona el Código Paso a Paso

### Flujo Completo del Programa

```
1. Usuario ejecuta: python main.py
   ↓
2. main.py crea instancia de SudokuGUI()
   ↓
3. SudokuGUI muestra pantalla de inicio
   ↓
4. Usuario selecciona dificultad (ej: "Medio")
   ↓
5. Se llama a start_game("Medio")
   ↓
6. SudokuGame genera tablero:
   - SudokuGenerator crea tablero completo
   - Remueve 45 celdas (dificultad Medio)
   ↓
7. Se muestra el tablero en la interfaz
   ↓
8. Usuario juega (ciclo):
   │
   ├─ Click en celda → select_cell()
   │   └─ Celda se marca con color azul
   │
   ├─ Click en número → place_number()
   │   ├─ Si modo ayuda: valida contra solución
   │   └─ Coloca número en grid
   │
   ├─ Click en pista → use_hint()
   │   ├─ Incrementa contador de pistas
   │   └─ Muestra número correcto
   │
   └─ Click en verificar → check_solution()
       │
       ├─ Si está completo y correcto:
       │   ├─ Calcular puntuación
       │   ├─ Guardar estadísticas en JSON
       │   ├─ Mostrar mensaje de victoria
       │   └─ Ofrecer jugar otra partida
       │
       ├─ Si tiene errores:
       │   ├─ Marcar celdas incorrectas en rojo
       │   └─ Mostrar cantidad de errores
       │
       └─ Si está incompleto:
           └─ Informar al usuario

9. Usuario decide:
   ├─ Jugar otra → Vuelve a paso 3
   └─ Salir → Cierra ventana
```

---

## Conceptos de Programación Utilizados

### 1. **Estructuras de Datos**

#### Matrices (Listas de Listas)
```python
# Tablero de Sudoku 9x9
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    # ... 7 filas más
]

# Acceso a elementos
valor = grid[2][4]  # Fila 2, Columna 4
grid[2][4] = 7      # Asignar valor
```

#### Diccionarios
```python
# Configuración con clave-valor
COLORS = {
    'bg': '#F0F0F0',
    'selected': '#BBE5FF'
}

# Acceso
color_fondo = COLORS['bg']
```

#### Listas
```python
# Historial de partidas
history = [
    {'date': '2025-01-15', 'score': 1100},
    {'date': '2025-01-16', 'score': 1200}
]

# Agregar elemento
history.append(nueva_partida)

# Últimos N elementos
ultimas_10 = history[-10:]
```

### 2. **Decisiones (if/elif/else)**

```python
# Ejemplo 1: Validación de rango
if num < 1 or num > 9:
    return False, "Número inválido"

# Ejemplo 2: Estado de celda
if self.is_fixed_cell(row, col):
    return 'fixed'
elif self.grid[row][col] == 0:
    return 'empty'
else:
    return 'user'

# Ejemplo 3: Verificación de victoria
if complete and errors == 0:
    self.won = True
elif errors > 0:
    self.show_errors()
else:
    self.show_incomplete_message()
```

### 3. **Repeticiones (Bucles)**

#### For Loop
```python
# Recorrer matriz
for i in range(9):
    for j in range(9):
        print(grid[i][j])

# Recorrer lista
for difficulty in ['Fácil', 'Medio', 'Difícil']:
    print(difficulty)

# Con índice
for index, item in enumerate(lista):
    print(f"Elemento {index}: {item}")
```

#### While Loop
```python
# Juego principal (mientras no termine)
while not game_over:
    esperar_movimiento()
    if movimiento_valido:
        aplicar_movimiento()
```

### 4. **Funciones**

```python
# Función simple
def saludar(nombre):
    return f"Hola, {nombre}"

# Función con tipo de retorno
def sumar(a: int, b: int) -> int:
    return a + b

# Función con valores por defecto
def crear_usuario(nombre, edad=18):
    return {'nombre': nombre, 'edad': edad}

# Función con múltiples retornos
def dividir(a, b):
    if b == 0:
        return False, "Error: división por cero"
    return True, a / b
```

### 5. **Recursión (Backtracking)**

```python
def _fill_grid(self):
    """Llena el tablero usando recursión"""
    for i in range(9):
        for j in range(9):
            if self.grid[i][j] == 0:  # Celda vacía
                for num in range(1, 10):  # Probar 1-9
                    if self._is_valid(i, j, num):
                        self.grid[i][j] = num

                        # Llamada recursiva
                        if self._fill_grid():
                            return True  # Solución encontrada

                        # Backtrack: deshacer y probar otro
                        self.grid[i][j] = 0

                return False  # No hay solución
    return True  # Tablero completo
```

**Cómo funciona el backtracking**:
1. Intentar colocar un número
2. Si funciona, continuar con la siguiente celda (recursión)
3. Si no funciona, retroceder y probar otro número
4. Repetir hasta encontrar solución

### 6. **Programación Orientada a Objetos (POO)**

#### Clases y Objetos
```python
class SudokuGame:
    """Clase que representa un juego"""

    def __init__(self, difficulty):
        """Constructor: inicializa atributos"""
        self.difficulty = difficulty
        self.grid = []
        self.score = 0

    def make_move(self, row, col, num):
        """Método: realizar un movimiento"""
        self.grid[row][col] = num

# Crear objeto (instancia)
juego = SudokuGame("Fácil")
juego.make_move(0, 0, 5)
```

#### Encapsulación
```python
class StatisticsManager:
    def __init__(self):
        self.stats = {}  # Atributo privado (convención con _)

    def _load_stats(self):  # Método privado
        """Solo usado internamente"""
        pass

    def get_stats(self):  # Método público
        """Acceso controlado a datos"""
        return self.stats
```

### 7. **Manejo de Archivos (JSON)**

```python
import json

# Guardar datos
datos = {'nombre': 'Juan', 'puntos': 100}
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2)

# Cargar datos
with open('datos.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)
```

### 8. **Eventos y Callbacks (Tkinter)**

```python
# Vincular evento de click
button = tk.Button(text="Click me", command=self.on_click)

# Evento con parámetros
button.bind('<Button-1>', lambda e: self.on_click(param))

# Hover effects
def on_enter(event):
    button['background'] = 'blue'

button.bind("<Enter>", on_enter)
```

### 9. **Manejo de Tiempo**

```python
import time
from datetime import datetime

# Medir tiempo transcurrido
start_time = time.time()
# ... hacer algo ...
elapsed = time.time() - start_time

# Fecha y hora actual
now = datetime.now()
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
# Resultado: "2025-01-15 14:30:00"
```

---

##  Sistema de Puntuación

### Fórmula Completa

```
Puntuación Final = BASE_SCORE + Bonificación de Tiempo - Penalizaciones

Donde:
  BASE_SCORE = 1000 puntos

  Bonificación de Tiempo:
    tiempo_restante = límite_de_tiempo - tiempo_usado
    bonificación = (tiempo_restante // 5) * 1

  Penalizaciones:
    - Por cada pista usada: -10 puntos
    - Por cada celda incorrecta al finalizar: -5 puntos
```

### Límites de Tiempo por Dificultad

| Dificultad | Tiempo Límite | Celdas Vacías |
|------------|---------------|---------------|
| **Fácil**  | 30 minutos    | 30 celdas     |
| **Medio**  | 40 minutos    | 45 celdas     |
| **Difícil**| 60 minutos    | 55 celdas     |

### Ejemplos de Puntuación

#### Ejemplo 1: Partida Perfecta
```
Dificultad: Fácil
Tiempo usado: 10 minutos (600 segundos)
Tiempo restante: 20 minutos (1200 segundos)
Pistas usadas: 0
Errores: 0

Cálculo:
  Base: 1000
  + Bonificación: (1200 // 5) * 1 = 240
  - Pistas: 0 * 10 = 0
  - Errores: 0 * 5 = 0
  = 1000 + 240 = 1240 puntos ⭐⭐⭐
```

#### Ejemplo 2: Con Ayudas
```
Dificultad: Medio
Tiempo usado: 25 minutos (1500 segundos)
Tiempo restante: 15 minutos (900 segundos)
Pistas usadas: 5
Errores: 0

Cálculo:
  Base: 1000
  + Bonificación: (900 // 5) * 1 = 180
  - Pistas: 5 * 10 = 50
  - Errores: 0 * 5 = 0
  = 1000 + 180 - 50 = 1130 puntos ⭐⭐
```

#### Ejemplo 3: Con Errores
```
Dificultad: Difícil
Tiempo usado: 55 minutos (3300 segundos)
Tiempo restante: 5 minutos (300 segundos)
Pistas usadas: 8
Errores al finalizar: 3

Cálculo:
  Base: 1000
  + Bonificación: (300 // 5) * 1 = 60
  - Pistas: 8 * 10 = 80
  - Errores: 3 * 5 = 15
  = 1000 + 60 - 80 - 15 = 965 puntos ⭐
```

---

## Reglas del Sudoku

### Regla Principal

Completar la cuadrícula 9×9 con dígitos del **1 al 9** cumpliendo:

1. **Cada fila** debe contener los números 1-9 sin repetir
2. **Cada columna** debe contener los números 1-9 sin repetir
3. **Cada subcuadro 3×3** debe contener los números 1-9 sin repetir

### Ejemplo Visual

```
┌───────┬───────┬───────┐
│ 5 3 . │ . 7 . │ . . . │ ← Fila: no repetir 1-9
│ 6 . . │ 1 9 5 │ . . . │
│ . 9 8 │ . . . │ . 6 . │
├───────┼───────┼───────┤
│ 8 . . │ . 6 . │ . . 3 │
│ 4 . . │ 8 . 3 │ . . 1 │
│ 7 . . │ . 2 . │ . . 6 │
├───────┼───────┼───────┤
│ . 6 . │ . . . │ 2 8 . │
│ . . . │ 4 1 9 │ . . 5 │
│ . . . │ . 8 . │ . 7 9 │
└───────┴───────┴───────┘
  ↑         ↑         ↑
Columna  Subcuadro  Subcuadro
no       3x3: no    3x3: no
repetir  repetir    repetir
1-9      1-9        1-9
```

### Estrategias para Resolver

1. **Eliminación**: Si un número ya está en fila/columna/subcuadro, no puede ir ahí
2. **Únicos**: Si solo queda una opción para una celda, esa es la respuesta
3. **Pares/Tripletas**: Técnicas avanzadas de eliminación
4. **Modo ayuda**: Activa el modo ayuda del juego para validar movimientos

---

### El juego no inicia

**Problema**: Al ejecutar `python main.py` no pasa nada o hay error.

**Soluciones**:
1. Verificar versión de Python:
   ```bash
   python --version
   # Debe ser 3.7 o superior
   ```

2. Intentar con `python3`:
   ```bash
   python3 main.py
   ```

3. Verificar que tkinter está instalado:
   ```bash
   python -m tkinter
   # Debe abrir una ventana de prueba
   ```

4. En Linux, instalar tkinter si falta:
   ```bash
   sudo apt-get install python3-tk
   ```

### Error: "No module named 'config'"

**Problema**: Python no encuentra los módulos.

**Solución**:
- Asegúrate de estar en la carpeta correcta:
  ```bash
  cd "ruta/a/Proyect_Sudoku"
  python main.py
  ```

### El juego es muy lento

**Problema**: La generación de tableros tarda mucho.

**Solución**:
- Esto es normal para nivel Difícil (puede tardar 2-5 segundos)
- Si tarda más de 10 segundos, verifica que no haya otros programas consumiendo CPU

### Las estadísticas no se guardan

**Problema**: Al cerrar y abrir, las estadísticas se perdieron.

**Soluciones**:
1. Verificar que el archivo `sudoku_stats.json` se creó en la carpeta del juego
2. Verificar permisos de escritura en la carpeta
3. En Windows, ejecutar como administrador si es necesario

### La ventana no se ve completa

**Problema**: La ventana está cortada o muy grande.

**Solución**:
- Ajustar constantes en `config.py`:
  ```python
  CELL_SIZE = 50  # Reducir tamaño de celdas
  WINDOW_WIDTH = 700  # Ajustar ancho
  WINDOW_HEIGHT = 600  # Ajustar alto
  ```

---

## Conceptos Educativos

### ¿Qué aprenderás con este proyecto?

1. **Estructuras de Datos**:
   - Matrices (listas de listas)
   - Diccionarios
   - Listas

2. **Control de Flujo**:
   - Condicionales (if/elif/else)
   - Bucles (for/while)
   - Recursión (backtracking)

3. **Funciones**:
   - Parámetros y retornos
   - Funciones con múltiples retornos
   - Type hints

4. **Programación Orientada a Objetos**:
   - Clases y objetos
   - Atributos y métodos
   - Encapsulación

5. **Interfaz Gráfica (GUI)**:
   - Tkinter básico
   - Eventos y callbacks
   - Layout management

6. **Persistencia de Datos**:
   - Lectura/escritura de archivos
   - Formato JSON
   - Manejo de errores

7. **Algoritmos**:
   - Backtracking
   - Validación
   - Búsqueda

---

**Proyecto desarrollado como parte del curso**:
- Pensamiento Computacional para Ingeniería (Gpo 401)
- TEC 1ER AÑO DE PROFE
- 2025

**Tecnologías utilizadas**:
- Python 3.7+
- Tkinter (GUI)
- JSON (persistencia)

**Autor**: Sistema de Sudoku

Leonardo Montoya Chavarría - A01613677
Alonso Osuna Maruri - A01613556

##  ¡A Jugar!

Para iniciar el juego, simplemente ejecuta:

```bash
python main.py
```

¡Disfruta entrenando tu mente con Sudoku!!!!!

---