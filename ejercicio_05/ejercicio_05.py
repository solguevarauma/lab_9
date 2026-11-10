"""
Ejercicio 5. Extraer valores de una estructura anidada

Un sistema recibe mediciones agrupadas en listas que pueden contener otras
listas, con distintos niveles de profundidad.

    def extraer_valores(datos):
        pass

La función devuelve una nueva lista plana con todos los números, en el orden en
que aparecen de izquierda a derecha. Las entradas contienen únicamente números
y listas, y no tienen referencias cíclicas.

Ejemplos

    extraer_valores([10, [20, 30], 40])     # [10, 20, 30, 40]
    extraer_valores([1, [2, [], [3]], 4])   # [1, 2, 3, 4]
    extraer_valores([[], [[], []]])         # []
    extraer_valores([])                     # []

Requisitos

- Utiliza un ciclo para recorrer los elementos del nivel actual.
- Si encuentras un número, incorpóralo al resultado.
- Si encuentras una lista, procésala mediante una llamada recursiva.
- Puedes utilizar append() y extend().
- No utilices cortes.
- No modifiques la estructura original.
- No dejes sublistas dentro del resultado.
"""


def extraer_valores(datos):
    """Extrae todos los valores de una estructura anidada y devuelve una lista plana."""
    resultado = []
    for elemento in datos:
        if isinstance(elemento, list):
            # Si el elemento es una lista, hacemos una llamada recursiva y extendemos el resultado
            resultado.extend(extraer_valores(elemento))
        else:
            # Si el elemento es un número, lo añadimos al resultado
            resultado.append(elemento)
    return resultado


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué devuelve la función cuando recibe una lista vacía?
# Devuelve una lista vacía, ya que no hay elementos que procesar.
#
# 2. ¿Qué diferencia hay entre incorporar un número e incorporar el
#    resultado de una llamada recursiva?
# Incorporar un número se hace mediante append(), que añade un solo elemento a la lista. Incorporar el resultado de una llamada recursiva se hace mediante extend(), que añade todos los elementos de la lista devuelta por la llamada recursiva a la lista resultado.
#
# 3. Dibuja únicamente las llamadas a extraer_valores() para
#    [1, [2, [], [1]], 4]. ¿Cuántas llamadas se realizan, incluyendo las
#    de listas vacías?
#   #   Llamada 1: extraer_valores([1, [2, [], [1]], 4])
#   #   Llamada 2: extraer_valores([2, [], [1]])
#   #   Llamada 3: extraer_valores([])
#   #   Llamada 4: extraer_valores([1])
#
# 4. ¿Por qué cada llamada necesita su propia lista de resultados?
#  Cada llamada necesita su propia lista de resultados porque cada nivel de la estructura anidada puede contener diferentes elementos y sublistas. Si todas las llamadas compartieran la misma lista de resultados, se mezclarían los valores de diferentes niveles, lo que resultaría en un resultado incorrecto. Al tener listas separadas, cada llamada puede construir su propio conjunto de resultados y luego combinarlos adecuadamente al retornar.
#


if __name__ == "__main__":
    print(extraer_valores([10, [20, 30], 40]))     # [10, 20, 30, 40]
    print(extraer_valores([1, [2, [], [3]], 4]))   # [1, 2, 3, 4]
    print(extraer_valores([[], [[], []]]))         # []
    print(extraer_valores([]))                     # []
