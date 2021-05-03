# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no
class Alumno:
    def __init__ (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def muestra_nota(self):
        if self.nota > 60:
            print(f'Usted aprobo con una nota de {self.nota}.')
        else:
            print(f'Usted ha reprobado con una nota de {self.nota}.')
estudiante = Alumno("Luis", 59)
estudiante.muestra_nota()