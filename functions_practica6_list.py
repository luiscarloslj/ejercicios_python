# Escribir una función que reciba una muestra de números en una lista y devuelva su promedio.

mi_lista = [3, 6, 9, 12]


def media(lista):
    total = sum(lista) / len(lista)
    return total


print(media(mi_lista))
