def factorial(valor):
    resultado = 1
    i = 0
    while i < valor:
        i += 1
        resultado *= i
    return resultado


valor = 6
print(f"El factorial de {valor} es {factorial(valor)}")
