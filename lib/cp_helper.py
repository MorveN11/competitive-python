"""Herramientas de debug para programación competitiva.

Todo se escribe en stderr (localmente: data/debug.txt) y se hace flush en cada llamada.

    dbg(x, y, label="paso 1")   cualquier valor, muestra el nombre de la variable
    dbg_mat(mat)                matriz 2D como tabla con índices
    dbg_grid(grid)              tablero de caracteres con reglas de coordenadas
    dbg_sep("fase 2")           línea separadora
    dbg_time("tras ordenar")    tiempo desde el inicio y desde la última llamada

Ajustes rápidos: ENABLED, LIMIT, LIMIT_ROWS, LIMIT_COLS, MAX_DEPTH.
"""
import ast
import linecache
import sys
import time
from collections import deque
from collections.abc import ItemsView, KeysView, ValuesView

__all__ = ["dbg", "dbg_mat", "dbg_grid", "dbg_sep", "dbg_time"]

ENABLED = True    # False = todas las funciones dejan de imprimir
LIMIT = 60        # máximo de elementos mostrados por lista/set/dict
LIMIT_ROWS = 60   # máximo de filas en tablas
LIMIT_COLS = 40   # máximo de columnas en tablas
LIMIT_STR = 300   # máximo de caracteres por string
MAX_DEPTH = 6     # profundidad máxima en estructuras anidadas
WIDE = 110        # un dict más largo que esto se imprime una entrada por línea

_SEQ = (list, tuple, deque)
_START = _last = time.perf_counter()


# ---------- salida ----------

def _emit(*lines):
    """Escribe líneas en stderr y fuerza flush."""
    print("\n".join(lines), file=sys.stderr)
    sys.stderr.flush()


def _is_literal(node):
    try:
        ast.literal_eval(node)
        return True
    except Exception:
        return False


def _names(func, count, depth=2):
    """Nombres de los argumentos tal como se escribieron en la llamada (None si no se puede)."""
    try:
        frame = sys._getframe(depth)
        line = linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip()
        calls = [
            n for n in ast.walk(ast.parse(line))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == func
        ]
        if len(calls) == 1 and len(calls[0].args) == count:  # ambiguo si hay varias en la línea
            return [None if _is_literal(a) else ast.unparse(a) for a in calls[0].args]
    except Exception:
        pass
    return [None] * count


# ---------- formato de valores ----------

def _sorted(items):
    try:
        return sorted(items)
    except TypeError:
        return sorted(items, key=repr)


def _cut(items):
    """Recorta a LIMIT elementos y devuelve (visibles, cuántos faltan)."""
    items = list(items)
    return items[:LIMIT], max(0, len(items) - LIMIT)


def _inline(x, depth=0, seen=()):
    """Representación en una sola línea de cualquier valor."""
    if id(x) in seen or depth > MAX_DEPTH:
        return "..."
    seen += (id(x),)
    if isinstance(x, (str, bytes)):
        r = repr(x)
        return r if len(r) <= LIMIT_STR else r[:LIMIT_STR] + f"... (+{len(r) - LIMIT_STR})"
    if isinstance(x, (KeysView, ValuesView, ItemsView)):
        x = list(x)
    if isinstance(x, dict):
        shown, more = _cut(x.items())
        body = [f"{_inline(k, depth + 1, seen)}: {_inline(v, depth + 1, seen)}" for k, v in shown]
        open_, close = "{", "}"
    elif isinstance(x, (set, frozenset)):
        shown, more = _cut(_sorted(x))
        body = [_inline(v, depth + 1, seen) for v in shown]
        open_, close = "{", "}"
    elif isinstance(x, tuple) and not hasattr(x, "_fields"):
        shown, more = _cut(x)
        body = [_inline(v, depth + 1, seen) for v in shown]
        open_, close = "(", ",)" if len(x) == 1 else ")"
    elif isinstance(x, (list, deque, bytearray)) or type(x).__name__ == "array":
        shown, more = _cut(x)
        body = [_inline(v, depth + 1, seen) for v in shown]
        open_, close = "[", "]"
    elif hasattr(x, "__dict__") and type(x).__repr__ is object.__repr__:
        shown, more = _cut(vars(x).items())
        body = [f"{k}={_inline(v, depth + 1, seen)}" for k, v in shown]
        open_, close = type(x).__name__ + "(", ")"
    else:
        return repr(x)
    if more:
        body.append(f"... +{more}")
    return open_ + ", ".join(body) + close


def _cell(v):
    """Texto de una celda de tabla: los strings van sin comillas."""
    if isinstance(v, str):
        return v if len(v) <= 12 else v[:9] + "..."
    return _inline(v, depth=MAX_DEPTH - 1)


def _table(rows, indent="  "):
    """Tabla alineada con índices de fila y columna. Filas desiguales se rellenan."""
    total_rows = len(rows)
    rows = [list(r) for r in rows[:LIMIT_ROWS]]
    ncols = min(max((len(r) for r in rows), default=0), LIMIT_COLS)
    cells = [[_cell(v) for v in r[:ncols]] + [""] * (ncols - len(r)) for r in rows]
    widths = [max([len(str(j))] + [len(row[j]) for row in cells]) for j in range(ncols)]
    rw = len(str(max(total_rows - 1, 0)))
    head = indent + " " * rw + "   " + " ".join(str(j).rjust(widths[j]) for j in range(ncols))
    out = [head, indent + "-" * (len(head) - len(indent))]
    for i, row in enumerate(cells):
        out.append(indent + f"{i:>{rw}} | " + " ".join(c.rjust(widths[j]) for j, c in enumerate(row)))
    if total_rows > LIMIT_ROWS:
        out.append(indent + f"... +{total_rows - LIMIT_ROWS} filas")
    return out


def _is_matrix(x):
    return (
        isinstance(x, _SEQ) and len(x) > 0
        and all(isinstance(r, _SEQ) for r in list(x)[:LIMIT_ROWS])
    )


def _render(x):
    """Texto completo de un valor, con tipo y tamaño. Puede ocupar varias líneas."""
    kind = type(x).__name__
    if _is_matrix(x):
        cols = max(len(r) for r in x)
        return "\n".join([f"{kind}[{len(x)}x{cols}]"] + _table(list(x)))
    if isinstance(x, dict):
        text = _inline(x)
        if len(text) > WIDE and len(x) > 1:
            shown, more = _cut(x.items())
            lines = [f"  {_inline(k)}: {_inline(v)}" for k, v in shown]
            if more:
                lines.append(f"  ... +{more}")
            return "\n".join([f"{kind}[{len(x)}]"] + lines)
        return f"{kind}[{len(x)}] {text}"
    if isinstance(x, (KeysView, ValuesView, ItemsView)):
        return f"{kind}[{len(x)}] {_inline(x)}"
    if isinstance(x, (list, tuple, deque, set, frozenset, bytearray)) and not hasattr(x, "_fields"):
        return f"{kind}[{len(x)}] {_inline(x)}"
    return _inline(x)


# ---------- API pública ----------

def dbg(*args, label=""):
    """Imprime cualquier valor (int, str, list, matriz, dict, set, objeto...) con su nombre."""
    if not ENABLED:
        return
    names = _names("dbg", len(args))
    head = f"[DEBUG] {label}:" if label else "[DEBUG]"
    parts = [(f"{n} = " if n else "") + _render(a) for n, a in zip(names, args)]
    if any("\n" in p for p in parts):
        _emit(*[f"{head} {p}" for p in parts])
    else:
        _emit(f"{head} " + " | ".join(parts) if parts else head)


def dbg_mat(matrix, name=None):
    """Imprime una matriz 2D como tabla con índices de fila y columna."""
    if not ENABLED:
        return
    name = name or _names("dbg_mat", 1)[0] or "Matriz"
    rows = [r if isinstance(r, _SEQ) else [r] for r in matrix]
    cols = max((len(r) for r in rows), default=0)
    _emit(f"[DEBUG] {name} ({len(rows)}x{cols}):", *_table(rows))


def dbg_grid(grid, name=None, sep=""):
    """Imprime un tablero de caracteres con reglas de coordenadas (fila y columna)."""
    if not ENABLED:
        return
    name = name or _names("dbg_grid", 1)[0] or "Grid"
    rows = [sep.join(map(str, r)) if not isinstance(r, str) else r for r in grid]
    ncols = max((len(r) for r in rows), default=0)
    rw = len(str(max(len(rows) - 1, 0)))
    ruler = " " * (rw + 3) + sep.join(str(j % 10) for j in range(ncols))
    lines = [f"[DEBUG] {name} ({len(rows)}x{ncols}):", "  " + ruler]
    lines += [f"  {i:>{rw}} | {r}" for i, r in enumerate(rows)]
    _emit(*lines)


def dbg_sep(title=""):
    """Línea separadora para dividir fases o casos de prueba."""
    if not ENABLED:
        return
    _emit(f"[DEBUG] ----- {title} -----" if title else "[DEBUG] " + "-" * 30)


def dbg_time(label=""):
    """Milisegundos desde el inicio y desde la última llamada."""
    global _last
    if not ENABLED:
        return
    now = time.perf_counter()
    _emit(f"[DEBUG] tiempo {label}: +{(now - _last) * 1000:.1f} ms (total {(now - _START) * 1000:.1f} ms)")
    _last = now
