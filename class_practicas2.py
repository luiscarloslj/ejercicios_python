# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
# Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
# La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
class Cliente:
    def __init__(self):
        self.nombre = nombre
        self.cantidad = cantidad
    def depositar(self):
        deposito = self.cantidad
        print(f'Su deposito es de {deposito} quetzalez')
    def extraer(self):
        extraido = self.cantidad
        print(f'Su extraccion es de {extraido} quetzalez')
        return 