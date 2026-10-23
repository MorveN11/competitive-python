from bisect import bisect_left, insort


def portales_magicos(N, P):
    vistos_ordenados = []
    respuesta = []

    for Pi in P:
        idx_pi = bisect_left(vistos_ordenados, Pi)

        if idx_pi == 0:
            respuesta.append(-1)
        else:
            respuesta.append(vistos_ordenados[idx_pi - 1])

        insort(vistos_ordenados, Pi)

    return respuesta

def __main__():
    print("Hola")
    result = portales_magicos(5, [3, 1, 4, 2, 5])
    print(result)

__main__()
