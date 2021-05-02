#mySolution

'''asignaturas = ["Matematicas", "Sociales", "Ciencias", "Idioma", "Fisica"]
a_borrar = []
for asignatura in asignaturas:
    nota = int(input("Cuales es su nota en " + asignatura + ": "))
    if nota > 69:
      a_borrar.append(asignatura)

print(set(asignaturas).difference(a_borrar))''' #set borra datos que se repiten en dos listas

#Otra solucion

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))