# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
class Operaciones:
    def __init__ (self):
        self.valor1 = int(input("ingrese un numero entero: "))
        self.valor2 = int(input("ingrese un numero entero: "))
    def sumar(self):
        return self.valor1 + self.valor2 
miOperacion = Operaciones()
print(miOperacion.sumar())