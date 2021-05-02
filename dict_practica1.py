diccionario1 = {"Euro": "€", "Dolar": "$", "Yen": "¥"}

for keys in diccionario1:
    entrada = input("De que moneda desea el simbolo: ")
    if keys != entrada:
        print("El valor que ingreso no esta en el diccionario, intentelo de nuevo")
    elif keys == entrada:
        print(diccionario1.get(entrada))
        break