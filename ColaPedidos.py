from html.entities import codepoint2name
from multiprocessing.spawn import get_preparation_data
from os import startfile, system
import time
from NodoPedidos import Pedidos

class ColaPedidos():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None

    def agregar(self, nombre, cantidad,  ingrediente, tiempo):
        global tiempoH, tiempoG
        tiempoG = 0
        cont = 1
        cont2 = 1
        
        pedido = Pedidos(nombre, cantidad, ingrediente, tiempo)
        if self.vacia() == True:
            
            self.primero = self.ultimo = pedido
            tiempoH = pedido.tiempo*pedido.cantidad
            print(f'Pedido de {pedido.cantidad} Pizza de {pedido.ingrediente} a nombre de {pedido.nombre} lista en {tiempoH} min') 

        else:
            temp = self.ultimo 
            self.ultimo = temp.siguiente = pedido
            tiempoH = (pedido.tiempo*pedido.cantidad) + tiempoH
            print(f'Pedido de {pedido.cantidad} Pizza de {pedido.ingrediente} a nombre de {pedido.nombre} lista en {tiempoH} min')
           


        graphviz= '''
            digraph G{
        
            rankdir = LR

            node [margin=0 shape=circle style=filled]
            '''

        temp1 = self.primero
        while temp1 != None:
            tiempoG = (temp1.tiempo*temp1.cantidad) + tiempoG
            graphviz += "Nodo"+str(cont)+'[label="Nombre: '+temp1.nombre+'\nCantidad: '+str(temp1.cantidad)+'\nTipo_Pizza: '+temp1.ingrediente+'\nTiempo: '+str(tiempoG)+' min"];\n'
            temp1 = temp1.siguiente
            cont += 1

        #agregar los punteros
        while cont2 < cont-1:
            graphviz += 'Nodo'+str(cont2)+'->'+'Nodo'+str(cont2+1)+';'
            cont2 += 1

        graphviz += 'label = "TIEMPO TOTAL DE LOS PEDIDOS DE PIZZA: '+str(tiempoH)+' min"'
        graphviz += '''
            }
            '''

        miArchivo = open('graphviz.dot', 'w')
        miArchivo.write(graphviz)
        miArchivo.close()
    
        system('dot -Tpng graphviz.dot -o ColaPedidos.png')


        #system('cd ./graphviz.png')

        startfile('ColaPedidos.png')


    
    def mostrarPedidos(self):
        temp = self.primero
        npedido = 1
        tiempo2 = 0
        while temp != None:
            tiempo2 = temp.tiempo*temp.cantidad + tiempo2
            print(f'{npedido}. Pedido {temp.cantidad} Pizza de {temp.ingrediente} a nombre de {temp.nombre} lista en {tiempo2} min')
            temp = temp.siguiente
            npedido +=1

            
    
    def entregarOrden(self):
        global tiempoT
        tiempoT = 0
        cont = 1
        cont2 = 1

        print('Entregando pedido', self.primero.ingrediente)
        time.sleep(5)
        print('Pedido entregado con éxito...!')
        self.primero = self.primero.siguiente 
        
        if self.primero != None:
            graphviz= '''
            digraph G{
        
            rankdir = LR
           

            node [margin=0 shape=circle style=filled]
            '''


            temp1 = self.primero
            while temp1 != None:
                tiempoT = (temp1.tiempo*temp1.cantidad) + tiempoT
                graphviz += "Nodo"+str(cont)+'[label="Nombre: '+temp1.nombre+'\nCantidad: '+str(temp1.cantidad)+'\nTipo_Pizza: '+temp1.ingrediente+'\nTiempo: '+str(tiempoT)+' min"];\n'
                temp1 = temp1.siguiente
                cont += 1

            #agregar los punteros
            while cont2 < cont-1:
                graphviz += 'Nodo'+str(cont2)+'->'+'Nodo'+str(cont2+1)+';'
                cont2 += 1


            graphviz += 'label = "TIEMPO TOTAL DE LOS PEDIDOS DE PIZZA: '+str(tiempoT)+' min"'
            graphviz += '''
            }
            '''

            miArchivo = open('graphviz.dot', 'w')
            miArchivo.write(graphviz)
            miArchivo.close()
    
            system('dot -Tpng graphviz.dot -o ColaPedidos.png')
            startfile('ColaPedidos.png')



  


        
        
        
