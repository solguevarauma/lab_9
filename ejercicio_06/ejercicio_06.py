"""
Ejercicio 6 (reto). Reporte de ventas por sucursal

Una empresa guarda las ventas de cada sucursal en un diccionario. Los valores
pueden estar agrupados en listas anidadas:

    ventas = {
        "Centro": [120, [80, 50]],
        "Norte": [],
        "Sur": [[200], [100, [25]]]
    }

Vas a construir un reporte reutilizando el ejercicio 5 y una nueva función
recursiva de cola.

Parte A. Suma con acumulador

    def sumar_cola(valores, i=0, acumulado=0):
        pass

La entrada es una lista plana de números. La función devuelve la suma desde la
posición i hasta el final, agregada al valor inicial de acumulado. Puedes
asumir que 0 <= i <= len(valores).

Ejemplos

    sumar_cola([10, 20, 30])          # 60
    sumar_cola([])                    # 0
    sumar_cola([10, 20, 30], 1)       # 50
    sumar_cola([10, 20], 0, 100)      # 130

Restricciones

- No utilices ciclos ni cortes.
- El resultado parcial debe viajar en acumulado.
- La llamada recursiva debe estar en posición de cola: no deben quedar sumas
  pendientes después de que retorne.

Parte B. Reporte integrado

    def reporte_sucursales(ventas):
        pass

Devuelve un diccionario con:

- "sucursales": lista de reportes individuales, en el mismo orden del
  diccionario de entrada. Cada uno incluye "nombre", "cantidad_ventas"
  (cantidad de valores numéricos) y "total" (suma de esos valores).
- "total_general": suma de las ventas de todas las sucursales.

Resultado esperado

    {
        "sucursales": [
            {"nombre": "Centro", "cantidad_ventas": 3, "total": 250},
            {"nombre": "Norte", "cantidad_ventas": 0, "total": 0},
            {"nombre": "Sur", "cantidad_ventas": 3, "total": 325}
        ],
        "total_general": 575
    }

Para un diccionario vacío:

    reporte_sucursales({})   # {"sucursales": [], "total_general": 0}

Requisitos

- Recorre el diccionario utilizando obligatoriamente:

    for nombre, registros in ventas.items():
        ...

- Reutiliza extraer_valores() del ejercicio 5 para obtener las ventas de cada
  sucursal. El archivo ya trae la importación:

    from ejercicio_05.ejercicio_05 import extraer_valores

- Utiliza sumar_cola() para calcular el total de cada sucursal.
- Acumula el total general durante el recorrido.
- No modifiques el diccionario ni sus listas.
- Devuelve el reporte; no lo imprimas.

Ejecuta este archivo desde la carpeta principal con:
    python -m ejercicio_06.ejercicio_06
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ejercicio_05.ejercicio_05 import extraer_valores


# Parte A ---------------------------------------------------------------

def sumar_cola(valores, i=0, acumulado=0):
    """Suma desde la posición i hasta el final, agregada a acumulado."""
    # Caso base: si hemos llegado al final de la lista, devolvemos el acumulado
    if i >= len(valores):
        return acumulado
    # Caso recursivo: sumamos el valor actual al acumulado y llamamos a la función con el siguiente índice
    else:
        return sumar_cola(valores, i + 1, acumulado + valores[i])


# Parte B ---------------------------------------------------------------

def reporte_sucursales(ventas):
    """Genera un reporte de ventas por sucursal."""
    reporte = {"sucursales": [], "total_general": 0}

    for nombre, registros in ventas.items():
        # Extraemos los valores de ventas de la sucursal
        valores = extraer_valores(registros)
        # Calculamos la cantidad de ventas y el total usando sumar_cola
        cantidad_ventas = len(valores)
        total = sumar_cola(valores)
        # Agregamos el reporte individual de la sucursal
        reporte["sucursales"].append({
            "nombre": nombre,
            "cantidad_ventas": cantidad_ventas,
            "total": total
        })
        # Acumulamos el total general
        reporte["total_general"] += total

    return reporte 


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué devuelve ventas.items() en cada iteración?
# Devuelve una tupla con el nombre de la sucursal y la lista de registros de ventas correspondiente. Por ejemplo, en la primera iteración podría devolver ("Centro", [120, [80, 50]]).
#
# 2. ¿Qué responsabilidad tiene cada una de estas funciones?
#    extraer_valores():
#    sumar_cola():
#    reporte_sucursales():
#
# 3. Completa la traza de sumar_cola([10, 20, 30]):
#
#    Llamada |  i  | acumulado
#    --------|-----|----------
#       1    |  0  |    0
#       2    |  1  |   10
#       3    |  2  |   30
#       4    |  3  |   60
#
# 4. ¿Por qué sumar_cola() es recursiva de cola?
#
#
# 5. ¿En cuál de estas dos expresiones queda una suma pendiente después
#    de la llamada?
#    return valores[i] + sumar(valores, i + 1) 
#    return sumar_cola(valores, i + 1, acumulado + valores[i])
# En la primera expresión queda una suma pendiente después de la llamada, ya que se está sumando el valor actual a lo que devuelva la llamada recursiva. En la segunda expresión, no queda ninguna operación pendiente después de la llamada, ya que el resultado de la llamada recursiva se devuelve directamente sin necesidad de realizar más cálculos.
#


if __name__ == "__main__":
    print(sumar_cola([10, 20, 30]))        # 60
    print(sumar_cola([]))                  # 0
    print(sumar_cola([10, 20, 30], 1))     # 50
    print(sumar_cola([10, 20], 0, 100))    # 130

    ventas = {
        "Centro": [120, [80, 50]],
        "Norte": [],
        "Sur": [[200], [100, [25]]]
    }
    print(reporte_sucursales(ventas))
    # {'sucursales': [{'nombre': 'Centro', 'cantidad_ventas': 3, 'total': 250},
    #                 {'nombre': 'Norte', 'cantidad_ventas': 0, 'total': 0},
    #                 {'nombre': 'Sur', 'cantidad_ventas': 3, 'total': 325}],
    #  'total_general': 575}

    print(reporte_sucursales({}))   # {'sucursales': [], 'total_general': 0}
