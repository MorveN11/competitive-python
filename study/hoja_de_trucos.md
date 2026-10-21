# Hoja de trucos: Nivel 2 con Python 3.11

Resumen de una página. Detalles y ejemplos ejecutables en los cuadernos `00` a `06`.

## Reglas del grader
- Nombre y parámetros **exactos**. `return`, no `print`.
- Sin `input()`. Sin `print` de depuración (usa `dbg`).
- No modifiques los argumentos sin querer (`sorted(a)` o `a[:]`).
- Sin estado global entre llamadas.

## Velocidad
- Python: ~10^7 vueltas de bucle por segundo.
- `N ≤ 20` → `2^n`. `N ≤ 9` → `n!`. `N ≤ 3000` → `n²`. `N ≤ 10^5..10^6` → `n log n` / `n`. `N ≥ 10^9` → `log n` / fórmula.

## Python vs C++
```python
-7 // 2 == -4      -7 % 3 == 2        # redondea hacia abajo, residuo >= 0
2 ** 100                              # sin desbordamiento
[[0] * m for _ in range(n)]           # matriz (NUNCA [[0]*m]*n)
b = a[:]                              # copia (b = a es un alias)
"".join(partes)                       # armar strings (no s += en bucle)
```

## 01 Arreglos y matrices
```python
DIR4 = [(-1,0),(1,0),(0,-1),(0,1)]
DIR8 = DIR4 + [(-1,-1),(-1,1),(1,-1),(1,1)]
0 <= ni < filas and 0 <= nj < cols         # validar bordes
list(zip(*m))                              # transpuesta
[list(f) for f in zip(*m[::-1])]           # giro 90° horario
[sum(f) for f in m]                        # suma por fila
```

## 02 Números
```python
import math
math.gcd(a, b)   math.lcm(a, b)   math.isqrt(n)
pow(a, b, m)     pow(a, -1, m)            # potencia e inverso modular
n // k                                    # múltiplos de k en 1..n
b // k - (a - 1) // k                     # múltiplos de k en a..b
# divisores: d en 1..√n, pares (d, n//d)
# primo: probar d*d <= n
# criba: para i primo, marcar i*i, i*i+i, ...
# mod: reducir con % m en CADA suma/resta/producto
```

## 03 Cadenas
```python
s[::-1]   s.find(t)   s.count(t)           # count NO cuenta solapados
ord(c) - ord("a")     chr(ord("a") + k)
Counter(s)            sorted(a) == sorted(b)   # anagramas
c == s[::-1]                               # palíndromo
# expandir desde cada centro (impar y par) para palíndromos
# posiciones de un patrón: for i in range(n - m + 1): s[i:i+m] == p
```

## 04 Técnicas sobre arreglos
```python
pref = [0] + list(accumulate(a))           # suma a[l..r] = pref[r+1] - pref[l]
# dos punteros: i=0, j=n-1 en arreglo ORDENADO; mover según la suma
# ventana fija:  v += a[i] - a[i-k]
# ventana variable:  expandir der; while no cumple: quitar izq
# rango +v: d[l] += v; d[r+1] -= v; luego accumulate
```

## 05 Simulación y búsqueda completa
```python
for mask in range(1 << n):                 # subconjuntos
    [a[i] for i in range(n) if mask >> i & 1]
combinations(a, k)   permutations(a)   product(x, repeat=k)
# recursión: tomar / no tomar; deshacer al volver (backtracking)
# simulación: estado + una regla por vuelta; tablero nuevo en cada paso
```

## 06 Estructuras y algoritmos
```python
sorted(a, key=lambda x: (x[1], -x[0]))     # por varios criterios
bisect_left(a, x)  bisect_right(a, x)      # a ordenado
# búsqueda binaria: primer índice que cumple (False..False True..True)
# sobre la respuesta: izq/der; medio = (izq+der+1)//2 si izq = medio
# goloso: ordenar y elegir (actividades: ordenar por FIN)
pila = []; pila.append(x); pila.pop()      # pila
q = deque(); q.append(x); q.popleft()      # cola (BFS)
x in s        # set O(1)         d.get(k, 0) + 1     Counter    defaultdict(list)
```

## Antes de enviar
- [ ] Probé ejemplos, mínimo, máximo, un elemento, vacío, todo igual.
- [ ] Función con el nombre exacto y sin `print` sueltos.
- [ ] El tiempo alcanza para el `N` máximo.
