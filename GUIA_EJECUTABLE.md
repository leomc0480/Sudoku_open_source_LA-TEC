# Guía Completa: Crear Ejecutable del Juego Sudoku

## ¿Qué es un Ejecutable?

Un **ejecutable** (.exe en Windows, .app en Mac, o archivo binario en Linux) es un programa que puedes correr **sin necesidad de tener Python instalado**. Es como los juegos que descargas de Steam o cualquier aplicación que instalas en tu computadora.

### Ventajas de un Ejecutable

 **No necesita Python**: Funciona en cualquier PC, aunque no tenga Python
 **Fácil de compartir**: Solo envías un archivo
 **Doble click y listo**: Se ejecuta como cualquier programa

---

## Método 1: Automático (MÁS FÁCIL) - Windows

### Paso 1: Doble Click en `build_exe.bat`

1. Ve a la carpeta del proyecto
2. Busca el archivo **build_exe.bat**
3. **Doble click** en él
4. Se abrirá una ventana negra que hará todo automáticamente

### Paso 2: Esperar (1-2 minutos)

Verás algo como esto:
```
====================================
  GENERADOR DE EJECUTABLE SUDOKU
====================================

[PASO 1] Instalando PyInstaller...
[PASO 2] Creando ejecutable...
...procesando...
```

### Paso 3: ¡Listo!

El ejecutable estará en:
```
Proyect_Sudoku/
└── dist/
    └── Sudoku.exe  ← ¡AQUÍ ESTÁ!
```

**¡Ya puedes jugar!** Solo haz doble click en `Sudoku.exe`

---

## Método 1: Automático - Linux/Mac

### Paso 1: Abrir Terminal

1. Abre la Terminal
2. Navega a la carpeta del proyecto:
   ```bash
   cd /ruta/a/Proyect_Sudoku
   ```

### Paso 2: Dar Permisos y Ejecutar

```bash
# Dar permisos de ejecución
chmod +x build_exe.sh

# Ejecutar el script
./build_exe.sh
```

### Paso 3: ¡Listo!

El ejecutable estará en:
```
Proyect_Sudoku/
└── dist/
    └── Sudoku  ← ¡AQUÍ ESTÁ!
```

Para ejecutarlo:
```bash
./dist/Sudoku
```

---

## Método 2: Manual (Más Control)

### Paso 1: Instalar PyInstaller

PyInstaller es la herramienta que convierte tu código Python en ejecutable.

**Windows:**
```bash
pip install pyinstaller
```

**Linux/Mac:**
```bash
pip3 install pyinstaller
```

### Paso 2: Verificar Instalación

```bash
pyinstaller --version
```

Deberías ver algo como: `5.13.0` o similar

### Paso 3: Crear el Ejecutable

Navega a la carpeta del proyecto y ejecuta:

**Comando Básico (Un solo archivo):**
```bash
pyinstaller --onefile --windowed --name "Sudoku" main.py
```

**Explicación de cada parámetro:**

| Parámetro | Significado | ¿Por qué lo usamos? |
|-----------|-------------|---------------------|
| `--onefile` | Todo en un solo archivo | Más fácil de compartir |
| `--windowed` | Sin consola | Solo la ventana del juego (sin terminal negra) |
| `--name "Sudoku"` | Nombre del ejecutable | Se llamará `Sudoku.exe` |
| `main.py` | Archivo principal | El que inicia el juego |

**Comando Avanzado (Con ícono):**
```bash
pyinstaller --onefile --windowed --name "Sudoku" --icon=icono.ico main.py
```

### Paso 4: Esperar

Verás mucha información en la terminal. **No te preocupes**, es normal. El proceso tarda:
- 30-60 segundos en computadoras rápidas
- 1-3 minutos en computadoras lentas

### Paso 5: Ubicar el Ejecutable

Después del proceso, se crearán estas carpetas:

```
Proyect_Sudoku/
├── build/          ← Archivos temporales (puedes borrar)
├── dist/           ← ¡AQUÍ ESTÁ TU EJECUTABLE!
│   └── Sudoku.exe  (o Sudoku en Linux/Mac)
└── Sudoku.spec     ← Configuración de PyInstaller (puedes borrar)
```

**El archivo que te interesa es:** `dist/Sudoku.exe`

---

## Cómo Compartir el Ejecutable

### Opción 1: Copiar el Archivo

1. Ve a `dist/Sudoku.exe`
2. Copia el archivo
3. Pégalo donde quieras (USB, OneDrive, Google Drive, etc.)
4. Compártelo

### Opción 2: Comprimir en ZIP

Si el archivo es muy pesado:

**Windows:**
1. Click derecho en `Sudoku.exe`
2. "Enviar a" → "Carpeta comprimida"
3. Se crea `Sudoku.zip` (más pequeño para enviar)

**Linux/Mac:**
```bash
zip Sudoku.zip dist/Sudoku
```

### Opción 3: Subir a la Nube

- **Google Drive**: Arrastra el archivo
- **OneDrive**: Sube el archivo
- **Dropbox**: Sube y comparte el link

---

## Solución de Problemas

### Problema 1: "No se encuentra PyInstaller"

**Síntoma:**
```
'pyinstaller' no se reconoce como un comando interno o externo
```

**Solución:**
```bash
# Instalar PyInstaller
pip install pyinstaller

# Si no funciona, usa:
python -m pip install pyinstaller
```

### Problema 2: El .exe es Muy Grande (50+ MB)

**¿Por qué?**
PyInstaller incluye Python completo y todas las librerías. Es normal.

**Soluciones:**
1. **Comprimir con ZIP**: Reduce ~50%
2. **Aceptarlo**: Es el precio de no necesitar Python

### Problema 3: Windows Defender Bloquea el .exe

**Síntoma:**
"Windows protegió tu PC" o "Archivo bloqueado"

**¿Por qué?**
Windows no reconoce el ejecutable porque no está "firmado" (no pagaste por un certificado).

**Solución:**
1. Click en "Más información"
2. Click en "Ejecutar de todas formas"
3. El juego funcionará normal

**Es seguro** porque TÚ lo creaste.

### Problema 4: El Ejecutable No Inicia

**Posibles causas:**

1. **Falta tkinter:** (Raro, pero puede pasar)
   - **Solución:** Reinstala Python con "tcl/tk" activado

2. **Archivos corruptos:**
   ```bash
   # Borrar carpetas y volver a crear
   rmdir /s build dist
   del Sudoku.spec
   pyinstaller --onefile --windowed --name "Sudoku" main.py
   ```

3. **Antivirus bloqueó archivos:**
   - Desactiva el antivirus temporalmente
   - Vuelve a crear el ejecutable
   - Agrega la carpeta a excepciones del antivirus

### Problema 5: "Error al importar módulo"

**Síntoma:**
```
ModuleNotFoundError: No module named 'config'
```

**Solución:**
```bash
# Asegúrate de estar en la carpeta correcta
cd Proyect_Sudoku

# Verifica que todos los archivos .py estén ahí
dir  # Windows
ls   # Linux/Mac

# Vuelve a crear el ejecutable
pyinstaller --onefile --windowed main.py
```

---

## Crear Ejecutable con Ícono Personalizado

### Paso 1: Conseguir un Ícono

Necesitas un archivo `.ico` (Windows) o `.icns` (Mac)

**Opciones:**
- Descargar de [IconArchive](https://iconarchive.com)
- Convertir una imagen con [ConvertICO](https://convertico.com)
- Usar un ícono gratuito de [FlatIcon](https://flaticon.com)

### Paso 2: Guardar el Ícono

Coloca el archivo `icono.ico` en la carpeta del proyecto:
```
Proyect_Sudoku/
├── icono.ico  ← AQUÍ
├── main.py
├── ...
```

### Paso 3: Crear Ejecutable con Ícono

```bash
pyinstaller --onefile --windowed --name "Sudoku" --icon=icono.ico main.py
```

**¡Listo!** Ahora tu ejecutable tiene un ícono bonito.

---

## Comparación de Métodos

| Método | Dificultad | Tiempo | Control | Recomendado Para |
|--------|------------|--------|---------|------------------|
| **Script Automático (.bat/.sh)** | ⭐ Fácil | 2 min | Bajo | Principiantes |
| **PyInstaller Manual** | ⭐⭐ Media | 5 min | Alto | Usuarios avanzados |
| **Con Ícono** | ⭐⭐⭐ Media | 7 min | Alto | Distribución profesional |

---

## ¿Cómo Funciona PyInstaller?

### Proceso Interno

1. **Analiza tu código**: Lee `main.py` y todos los imports
2. **Encuentra dependencias**: Detecta qué librerías usa (tkinter, json, etc.)
3. **Empaqueta todo**: Junta Python + librerías + tu código
4. **Crea ejecutable**: Genera un solo archivo .exe

### Archivos Generados

```
build/          # Archivos intermedios (se pueden borrar)
├── Sudoku/
│   ├── base_library.zip
│   ├── PKG-00.toc
│   └── ...

dist/           # EJECUTABLE FINAL (ESTE ES EL IMPORTANTE)
└── Sudoku.exe

Sudoku.spec     # Configuración (se puede borrar o guardar para rebuild)
```

**Solo necesitas:** `dist/Sudoku.exe`

---

## Consejos Pro

### 1. Nombre Descriptivo
```bash
pyinstaller --onefile --windowed --name "Sudoku_v1.0_Windows" main.py
```

### 2. Agregar Versión
Edita `Sudoku.spec` después de la primera compilación:
```python
# Agregar información de versión
version='1.0.0',
description='Juego de Sudoku',
```

Luego recompila con:
```bash
pyinstaller Sudoku.spec
```

### 3. Reducir Tamaño (Avanzado)
```bash
pyinstaller --onefile --windowed --name "Sudoku" --exclude-module matplotlib --exclude-module numpy main.py
```

### 4. Modo Debug (Si hay errores)
```bash
# Quita --windowed para ver errores
pyinstaller --onefile --name "Sudoku" main.py
```

---

## Checklist Final

Antes de compartir tu ejecutable:

- [ ] Probé el .exe en mi computadora
- [ ] Probé el .exe en otra computadora sin Python
- [ ] El juego inicia correctamente
- [ ] Todas las funciones funcionan (pistas, verificar, estadísticas)
- [ ] Las estadísticas se guardan (se crea sudoku_stats.json)
- [ ] Comprimí el .exe en ZIP si es muy grande
- [ ] Agregué instrucciones de instalación si es necesario

---

## Resumen: 3 Formas de Crear Ejecutable

### Rápida (Principiantes)
```bash
# Doble click en build_exe.bat (Windows)
# o
./build_exe.sh (Linux/Mac)
```

### Manual (Control Total)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Sudoku" main.py
```

### Profesional (Con Ícono)
```bash
pyinstaller --onefile --windowed --name "Sudoku" --icon=icono.ico main.py
```

---

## FAQ - Preguntas Frecuentes

**P: ¿El ejecutable funciona en cualquier Windows?**
R: Sí, en Windows 7, 8, 10, 11 (64-bit)

**P: ¿Puedo crear un .exe en Linux?**
R: No, solo crea ejecutables para Linux. Necesitas Windows para crear .exe

**P: ¿Por qué es tan grande el .exe?**
R: Incluye Python completo (20-30 MB) + tus archivos

**P: ¿Es legal distribuir el ejecutable?**
R: Sí, Python y PyInstaller son de código abierto

**P: ¿Puedo vender el ejecutable?**
R: Sí, es tu código, puedes hacer lo que quieras

**P: ¿Los antivirus lo detectan como virus?**
R: A veces sí (falso positivo). Es normal con ejecutables no firmados.

---

## Recursos Adicionales

- [Documentación PyInstaller](https://pyinstaller.org/en/stable/)
- [Tutorial PyInstaller Video](https://www.youtube.com/results?search_query=pyinstaller+tutorial)
- [Convertir Imágenes a .ico](https://convertico.com)
- [Íconos Gratuitos](https://www.flaticon.com)

---

## Ayuda

Si tienes problemas:

1. Lee la sección "Solución de Problemas"
2. Busca el error en Google: "pyinstaller [tu error]"
3. Consulta con tu instructor

---

**¡Felicidades! Ahora sabes crear ejecutables profesionales de tus juegos en Python.** 

---

**Autores:**
Leonardo Montoya Chavarría - A01613677
Alonso Osuna Maruri - A01613556
