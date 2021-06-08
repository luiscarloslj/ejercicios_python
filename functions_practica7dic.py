# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra
# que contiene y su frecuencia. Escribir otra función que reciba el diccionario
# generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

mydic = {}


def get_list(phrase):
    mydic = phrase.split(sep=" ")
    return mydic


print(type(get_list("Hola mundo")))
