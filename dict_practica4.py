# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
factura_pagar_o_terminar = 0
facturas_precio = {}
numerof = 0
valorf = 0
pagadof = 0
while factura_pagar_o_terminar < 3:
    print("Si desea agregar una factura precione 1:")
    print("Si desea pagar una factura precione 2:")
    print("Si desea terminar precione 3:")
    factura_pagar_o_terminar = int(input(""))
    if factura_pagar_o_terminar == 1:
        numerof = int(input("Ingrese el numero de la factura "))
        valorf = int(input("Ingrese el precio de la factura "))
        pagadof = valorf - int(input("Cuanto desea pagar ")) 
        facturas_precio[numerof] = pagadof
        print(f'El valor de la factura "{numerof}" es de {facturas_precio[numerof]}')
    elif factura_pagar_o_terminar == 2:
        numerof = int(input("Ingrese el numero de la factura "))
        print(f'El valor de la factura es {facturas_precio[numerof]}')
        pagadof = facturas_precio[numerof] - int(input("Ingrese cuanto quiere pagar ")) 
        facturas_precio[numerof] = pagadof
        print(f'El valor de la factura "{numerof}" es de {facturas_precio[numerof]}')
    
# Codigo Sugerido: 
    
# facturas = {}
# cobrado = 0
# pendiente = 0
# more = ''
# while more != 'T':
#     if more == 'A':
#         clave = input('Introduce el número de la factura: ')
#         coste = float(input('Introduce el coste de la factura: '))
#         facturas[clave] = coste
#         pendiente += coste
#     if more == 'P':
#         clave = input('Introduce el número de la factura a pagar: ')
#         coste = facturas.pop(clave, 0)
#         cobrado += coste
#         pendiente -= coste
#     print('Recaudado:', cobrado)
#     print('Pendiente de cobro: ', pendiente)
#     more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')
        
    





 
