# Ejemplo resuelto: suma de n números. Entrada en data/input.txt.
import os
import sys

# --- Entrada/salida: local vs. juez online ---
# Local: si existe data/input.txt, stdin/stdout/stderr van a archivos dentro de data/.
# Juez online: esos archivos no existen y se usa la consola normal.
HERE = os.path.dirname(os.path.abspath(globals().get("__file__", "")))
DATA = os.path.join(HERE, "data")
if os.path.exists(os.path.join(DATA, "input.txt")):
    sys.stdin = open(os.path.join(DATA, "input.txt"), "r", encoding="utf-8")
    sys.stdout = open(os.path.join(DATA, "output.txt"), "w", encoding="utf-8")  # solo la respuesta
    sys.stderr = open(os.path.join(DATA, "debug.txt"), "w", encoding="utf-8")   # todos los logs

input = sys.stdin.readline  # lectura rápida (incluye el salto de línea)

# --- Debugger: solo existe en local. En el juez las llamadas a dbg no hacen nada. ---
sys.path.insert(0, os.path.join(HERE, "lib"))
try:
    from cp_helper import dbg, dbg_mat, dbg_grid, dbg_sep, dbg_time
except ImportError:
    def dbg(*args, **kwargs): pass
    dbg_mat = dbg_grid = dbg_sep = dbg_time = dbg

# sys.setrecursionlimit(10**6)  # descomenta para recursión profunda (DFS)
# MOD = 10**9 + 7
# INF = float("inf")


def solve():
    # --- Lectura (descomenta lo que necesites) ---
    n = int(input())                                                # un entero
    # a, b = map(int, input().split())                              # varios en una línea
    arr = [int(x) for x in input().split()]                         # lista 1D
    # s = input().strip()                                           # un string
    # mat = [[int(x) for x in input().split()] for _ in range(n)]   # matriz de n filas
    # grid = [input().strip() for _ in range(n)]                    # tablero de caracteres

    # --- Depuración (se ve en data/debug.txt) ---
    dbg(n, arr)            # imprime nombre y valor de cualquier variable
    # dbg_mat(mat)         # matriz como tabla
    # dbg_grid(grid)       # tablero con coordenadas

    # --- Solución ---
    ans = sum(arr)

    # --- Respuesta ---
    print(ans)             # va a data/output.txt


if __name__ == '__main__':
    solve()
    # Varios casos de prueba: t = int(input()) y luego "for _ in range(t): solve()"
