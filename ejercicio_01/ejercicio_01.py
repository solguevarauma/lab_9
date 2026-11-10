"""
Ejercicio 1. Potencia recursiva

Implementa una función que calcule una potencia mediante multiplicaciones y
llamadas recursivas. Recibe una base numérica y un exponente entero no
negativo.

    def potencia(base, exponente):
        pass

En este ejercicio, cualquier base elevada a cero devuelve 1, incluido
potencia(0, 0).

Ejemplos

    potencia(2, 4)    # 16
    potencia(5, 0)    # 1
    potencia(-2, 3)   # -8
    potencia(0, 5)    # 0

Restricciones

- No utilices ciclos.
- No utilices  ni pow().
- La solución debe ser recursiva.
"""


def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: multiplicar la base por la potencia de la base con el exponente reducido en 1
    else:
        return base * potencia(base, exponente - 1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuál es el caso base?
# Cualquier número elevado a 0 es 1.
#
# 2. ¿Qué argumento cambia en cada llamada?
# El argumento que cambia es el exponente, que se reduce en 1 en cada llamada recursiva.
#
# 3. ¿Qué operación queda pendiente mientras se resuelve la llamada recursiva?
# La operación pendiente es la multiplicación de la base por el resultado de la llamada recursiva con el exponente reducido en 1.
#
# 4. Escribe las llamadas y los retornos de potencia(3, 3).
# potencia(3, 3) -> 3 * potencia(3, 2) -> 3 * 3 * potencia(3, 1) -> 3 * 3 * 3 * potencia(3, 0) -> 3 * 3 * 3 * 1 -> 27
#

if __name__ == "__main__":
    print(potencia(2, 4))    # 16
    print(potencia(5, 0))    # 1
    print(potencia(-2, 3))   # -8
    print(potencia(0, 5))    # 0
