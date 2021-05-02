diccionario1 = {}
diccionario1["Nombre"] = input("Ingrese su nombre: ")
diccionario1["Edad"] = input("Ingrese su edad: ")
diccionario1["Direccion"] = input("Ingrese su direccion: ")
diccionario1["Telefono"] = input("Ingrese su Telefono: ")
print(f'Su Nombre es {diccionario1.get("Nombre")}, tiene {diccionario1.get("Edad")} años, vive en {diccionario1.get("Direccion")}, y su numero de telefono es {diccionario1.get("Telefono")}.')
