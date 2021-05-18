# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
# Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
# La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
# EL BANCO herede solo tres atributos de la clase cliente y que cree un diccionario en el objeto de la clase banco, y que agregue a cada cliente
class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.micuenta = 0
        
    def depositar(self):
        self.micuenta += self.cantidad
    def extraer(self, retiro):
        self.retiro = retiro
        self.micuenta -= self.retiro
    def mostrar_total(self):
        print(f'La cantidad que usted tiene en total ahora es de {self.micuenta}')
        
class Banco(Cliente):
    
    def operar(self):
        self.dicc_clientes = {}
        self.dicc_clientes[self.nombre] = self.micuenta
        
    def deposito_total(self):
        print(f'El deposito total de {self.dicc_clientes}') 
        
        
        
        
cliente_uno = Banco("Juan", 10)
cliente_uno.depositar()
cliente_uno.extraer(5)
cliente_uno.mostrar_total()
cliente_uno.operar()
cliente_uno.deposito_total()

cliente_dos = Banco("Mishell", 100)
cliente_dos.depositar()
cliente_dos.extraer(5)
cliente_dos.mostrar_total()
cliente_dos.operar()
cliente_dos.deposito_total()
