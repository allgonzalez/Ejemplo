from ColaPedidos import ColaPedidos

tiempo = 0
opcion = ''
pedido =  ColaPedidos()
while opcion !=5:
    print('--------------Pizzeria-----------')
    print('1. Ingresar Orden')
    print('2. Entregar Orden')
    print('3. Mostrar Ordenes')
    print('4. Mostar Datos del Estudiante')
    print('5. Salir')
    print('')
    opcion = input('>Ingrese una opción: ')
    
    if opcion == '1':
        print("-------------Ingredientes disponibles------------")
        print("-Pepperoni")
        print("-Salchicha")
        print("-Carne")
        print("-Queso")
        print("-Piña")
        ingrediente = input('>Ingrese el ingrediente: ')
        nombre = input('>Ingrese su nombre: ')
        cantidad = int(input('>Ingrese la cantidad de Pizzas a ordenar: '))

        #Dependiendo del tiempo se asignan valores al tiempo para agregarlos a la cola
        if ingrediente.upper() == 'PEPPERONI':
            tiempo = 3
        elif ingrediente.upper() == 'SALCHICHA':
            tiempo = 4
        elif ingrediente.upper() == 'CARNE':
            tiempo = 10
        elif ingrediente.upper() == 'QUESO':
            tiempo = 5
        elif ingrediente.upper() == 'PIÑA':
            tiempo = 2
        else:
            print("INGREDIENTE NO DISPONIBLE!")
            continue
        
        
        #Una vez visto que ingrediente y seteado el tiempo se agrega a la cola
        pedido.agregar(nombre, cantidad, ingrediente, tiempo)
    elif opcion == '2':
        if pedido.vacia():
            print('No hay pedidos para entregar')
        else: 
            #Entrego orden
            pedido.entregarOrden()
    
    elif opcion == '3':
        if pedido.vacia():
            print('No hay ordenes aún')
        else:
            #Muestro mis pedidos
            pedido.mostrarPedidos()
           
    elif opcion == '4':
        print("Nombre: ")
        print("Carnet: ")
        print("Carrera: ")

    elif opcion == '5':
        print('Gracias por su preferencia :)')
        break
    else:
        print('Ingrese una opción válida >:| !!')

