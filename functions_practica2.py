class Sumando:
    def __init__(self, n1,n2):
        self.sumar = n1 + n2

miSuma = Sumando(1,2)
print(miSuma.sumar)

class Atributos:
    casa = "grande"
    numeros = 2
    
variables = Atributos()
print(getattr(variables, 'numeros')) #Getattr trae el valor del atributo como vairables.numeros
print(hasattr(variables,'casa')) #hasattr devuelve el valor true si esta el atributo y False sino esta

delattr(Atributos,'casa') # delattr borra el atributo de la clase, funciono pero no ejecutando setattr antes
print(hasattr(variables,'casa'))
setattr(variables,'numeros','10') #cambia el valor del atributo casa, es decir tenia grande ahora es pequeña
print(getattr(variables, 'numeros'))

   

    


    


    
    