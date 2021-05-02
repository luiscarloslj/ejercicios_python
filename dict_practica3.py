diccionario1 = {'Platanos' : 1.35, 'Manzana' : 0.80, 'Pera' : 0.85, 'Naranja' : 0.70}
fruta = input("Ingrese una fruta: ")
if fruta in diccionario1:    
    cantidad = float(input(f"Ingrese la cantidad de kilos de {fruta}s que quiere: "))
    multiplicaP = diccionario1[fruta] * cantidad
    print("{0:.2f}".format(multiplicaP))
else:
    print(f"La {fruta} no esta")
