# CP Python

Entorno para resolver problemas de programación competitiva en Python con VS Code. Rápido, visual y pensado también para enseñar. Solo usa la librería estándar de Python 3.

La raíz del proyecto es solo para tus ejercicios. Todo lo demás está en carpetas.

## Estructura

```
cp-python/
├── ej_suma.py          ← ejemplo resuelto (tus ejercicios van aquí, en la raíz)
├── course/             ← curso introductorio (14 cuadernos .ipynb)
├── study/              ← material de estudio del Nivel 2 (7 cuadernos + hoja de trucos)
├── problems/           ← problemas de años anteriores, con grader local
├── data/
│   ├── input.txt       ← entrada de prueba (tú la escribes)
│   ├── output.txt      ← SOLO la respuesta del programa (se regenera)
│   └── debug.txt       ← todos los logs de dbg() (se regenera)
├── lib/
│   ├── template.py     ← plantilla base
│   └── cp_helper.py    ← funciones de debug
└── .vscode/            ← snippet, tarea de ejecución, depuración, ajustes
```

## Curso introductorio

La carpeta [`course/`](course/README.md) tiene un curso de 14 cuadernos para principiantes: Python básico, introducción a la programación competitiva, problemas sencillos y el uso de este template. Empieza por `course/01_primer_programa.ipynb`. Para abrirlos hace falta la extensión Jupyter y `python -m pip install ipykernel` (detalles en `course/README.md`).

## Material de estudio y problemas del Nivel 2

- [`study/`](study/README.md): un cuaderno por cada tópico del temario del Nivel 2 (control y arreglos, números, cadenas, prefijos/dos punteros/ventana, simulación y búsqueda completa, búsqueda binaria/golosos/pilas/colas/sets/mapas), más una [hoja de trucos](study/hoja_de_trucos.md).
- [`problems/`](problems/README.md): espacio para resolver problemas de años anteriores. Los problemas son **con grader** (se implementa una función). `python problems/nuevo.py 2023 nombre` crea la carpeta de un problema.

## Requisitos

- Python 3.9 o superior (el debugger usa `ast.unparse`; sin él funciona, solo sin nombres de variables).
- VS Code con la extensión **Python** (VS Code la recomienda al abrir la carpeta).
- Abre `cp-python` como **carpeta raíz** (File → Open Folder). Si no, `.vscode/` no se carga.

## Flujo de trabajo

1. Crea un archivo `.py` en la raíz (ej. `a_suma.py`).
2. Escribe `cp` y presiona **Tab** para insertar la plantilla.
3. Pega la entrada de prueba en `data/input.txt`.
4. Presiona **Ctrl+Shift+B** (Cmd+Shift+B en Mac) para ejecutar el archivo activo.
5. Abre `data/output.txt` (respuesta) y `data/debug.txt` (logs).

`input.txt`, `output.txt` y `debug.txt` son compartidos por todos los ejercicios: cada ejecución los sobrescribe.

## Cómo funciona la entrada y salida

La plantilla revisa si existe `data/input.txt`:

| Situación | stdin | stdout (`print`) | stderr (`dbg`) |
|---|---|---|---|
| Local (existe `data/input.txt`) | `data/input.txt` | `data/output.txt` | `data/debug.txt` |
| Juez online (no existe) | consola | consola | consola |

- Las rutas dependen de la ubicación del script, no de la carpeta de trabajo. Funciona desde cualquier terminal.
- Para enviar al juez, copia el archivo tal cual. Si falta `cp_helper.py`, las llamadas a `dbg` no hacen nada ni fallan.
- Para probar con la consola en local, renombra o borra `data/input.txt`.

## Debugger: `lib/cp_helper.py`

Todo se escribe en `data/debug.txt` con flush inmediato, así puedes ver el archivo actualizarse en vivo. Cada función muestra el nombre de la variable tal como la escribiste.

```python
dbg(n, arr)                    # [DEBUG] n = 5 | arr = list[5] [1, 2, 3, 5, 10]
dbg(x, label="tras el while")  # etiqueta opcional
dbg_mat(dp)                    # matriz como tabla con índices
dbg_grid(grid)                 # tablero de caracteres con coordenadas
dbg_sep("caso 2")              # separador
dbg_time("tras ordenar")       # ms desde el inicio y desde la última llamada
```

### Qué soporta `dbg`

| Tipo | Cómo se ve |
|---|---|
| int, float, str, bool, None | valor tal cual (`str` con comillas) |
| list, tuple, deque | `list[5] [1, 2, 3, 4, 5]` |
| matriz (lista de listas) | tabla con índices de fila y columna |
| set, frozenset | ordenado cuando se puede: `set[3] {1, 3, 5}` |
| dict | `dict[3] {0: 0, 1: 1, 2: 4}`; si es largo, una entrada por línea |
| keys, values, items | `dict_keys[3] [0, 1, 2]` |
| namedtuple, dataclass, objetos | `Node(v=1, nxt=None)` |
| estructuras anidadas | recursivas, hasta `MAX_DEPTH` niveles |
| referencias circulares | se cortan con `...` |
| generadores | no se consumen, se muestra su `repr` |

Las colecciones largas se recortan (`... +440`). Cambia los límites al inicio de `lib/cp_helper.py`:

| Ajuste | Por defecto | Para qué |
|---|---|---|
| `ENABLED` | `True` | `False` apaga todo el debug |
| `LIMIT` | 60 | elementos por lista/set/dict |
| `LIMIT_ROWS` / `LIMIT_COLS` | 60 / 40 | tamaño máximo de tablas |
| `LIMIT_STR` | 300 | caracteres por string |
| `MAX_DEPTH` | 6 | niveles de anidación |

Ejemplo de tabla:

```
[DEBUG] dp (3x4):
      0 1 2 3
  -----------
  0 | 0 0 0 0
  1 | 0 1 2 3
  2 | 0 2 4 6
```

Límites conocidos: el nombre de la variable no se detecta si llamas a `dbg` en varias líneas, o si hay dos llamadas a la misma función en una línea. En esos casos se muestra solo el valor.

## Ejecutar y depurar

| Acción | Cómo |
|---|---|
| Ejecutar el archivo activo | **Ctrl+Shift+B** (tarea por defecto) |
| Depurar con breakpoints | **F5** (configuración "Debug active file") |
| Code Runner (opcional) | **Ctrl+Alt+N**; el panel queda vacío porque la salida va a `data/` |

El depurador de VS Code (F5) también guarda la salida en `data/`. Mira `data/debug.txt` para los logs.

Desde la terminal, en cualquier carpeta:

```
python ej_suma.py
```

## Snippet

Escribe `cp` o `template` en un `.py` y presiona **Tab**. Se define en `.vscode/python.code-snippets` y es una copia de `lib/template.py`.

Si el Tab no inserta la plantilla:
1. Abre la carpeta como raíz (ver Requisitos).
2. Verifica que el archivo esté guardado como `.py`.
3. `Ctrl+Shift+P` → `Snippets: Insert Snippet` → "CP template". Si aparece, el snippet carga bien.
4. `.vscode/settings.json` ya ajusta el Tab para Python. Un perfil de VS Code o ajustes de usuario muy específicos pueden interferir.

Si cambias `lib/template.py`, regenera el snippet para que coincida:

```
python -c "import json;b=open('lib/template.py',encoding='utf-8').read().rstrip('\n').split('\n');json.dump({'CP template':{'prefix':['cp','template'],'scope':'python','description':'Plantilla de programación competitiva','body':b}},open('.vscode/python.code-snippets','w',encoding='utf-8',newline='\n'),indent=2,ensure_ascii=False)"
```

## Lectura rápida (referencia)

```python
n = int(input())                                              # un entero
a, b = map(int, input().split())                              # varios en una línea
arr = [int(x) for x in input().split()]                       # lista 1D
s = input().strip()                                           # un string
mat = [[int(x) for x in input().split()] for _ in range(n)]   # matriz de n filas
grid = [input().strip() for _ in range(n)]                    # tablero de caracteres
```

Varios casos de prueba: lee `t = int(input())` y llama `solve()` dentro de `for _ in range(t)`.

## Git

| Archivo | Para qué |
|---|---|
| `.gitignore` | ignora `data/output.txt`, `data/debug.txt`, `__pycache__`, entornos virtuales y archivos de editor |
| `.gitattributes` | finales de línea LF en todo, para evitar diferencias entre Windows, Mac y Linux |
| `.editorconfig` | UTF-8, LF, 4 espacios; lo respetan VS Code y la mayoría de editores |

`data/input.txt` sí se versiona, como muestra del formato.

## Enseñar con este entorno

1. Abre `ej_suma.py` y ejecútalo con Ctrl+Shift+B.
2. Cambia los números de `data/input.txt` y vuelve a ejecutar.
3. Agrega un `dbg(...)` en el código y mira cómo aparece en `data/debug.txt`.
4. Crea un ejercicio nuevo con `cp` + Tab y descomenta las líneas de lectura que necesites.

## Problemas comunes

| Síntoma | Causa y solución |
|---|---|
| `output.txt` vacío | El programa falló: revisa el error en la terminal de VS Code. |
| `EOFError` o `ValueError` al leer | `data/input.txt` no tiene el formato que espera el código. |
| El programa lee de la consola en vez del archivo | `data/input.txt` no existe o el script está fuera de la raíz del proyecto. |
| `dbg` no muestra nombres | La llamada ocupa varias líneas, o ver "Límites conocidos". |
| Falla `ast.unparse` | Python menor a 3.9: el debug sigue funcionando, solo sin nombres. |
