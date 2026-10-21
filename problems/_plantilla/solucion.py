# Solución del problema. Describe el problema en enunciado.md.
try:
    dbg
except NameError:  # en el juez dbg no existe: no hace nada
    def dbg(*args, **kwargs): pass


def resolver(n):
    # Cambia el nombre y los parámetros por los que pida el enunciado.
    # Ejemplo de la plantilla: suma de 1 a n.
    ans = n * (n + 1) // 2
    dbg(n, ans)
    return ans
