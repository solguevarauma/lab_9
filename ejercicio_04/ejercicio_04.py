"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    """Busca un código en la lista ordenada usando búsqueda binaria recursiva."""
    # Caso base: si el rango es inválido, devolvemos -1
    if izquierda > derecha:
        return -1

    # Calculamos el índice medio
    medio = (izquierda + derecha) // 2

    # Comparamos el valor medio con el objetivo
    if codigos[medio] == objetivo:
        return medio  # Código encontrado
    elif codigos[medio] < objetivo:
        # Buscamos en la mitad derecha
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)
    else:
        # Buscamos en la mitad izquierda
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
# # La búsqueda termina cuando se encuentra el código (devuelve el índice) o cuando el rango de búsqueda es inválido (izquierda > derecha), devolviendo -1.
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
# # Porque ya hemos comparado el valor en la posición central con el objetivo, y si no es igual, sabemos que el objetivo no puede estar en esa posición. Por lo tanto, podemos descartar esa posición y continuar la búsqueda en la mitad correspondiente.
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |     0      |     6    |  3     |300 < 415, buscar en la izquierda
#       2    |    0       |    2     |  1     |300 > 205, buscar en la derecha
#       3    |      2     |      2   |  1     |300 > 205, buscar en la derecha
#       4    |     2      |       1  |  -     |izquierda > derecha, retorna -1
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
# # La diferencia principal es que buscar_codigo() reduce el rango de búsqueda a la mitad en cada llamada recursiva, mientras que contar_desde_limite() procesa un elemento a la vez y avanza secuencialmente a través de la lista. En otras palabras, buscar_codigo() utiliza una estrategia de "divide y vencerás", mientras que contar_desde_limite() sigue un enfoque lineal.
#


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
