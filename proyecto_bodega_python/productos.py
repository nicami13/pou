import core
import os
diccProducto = {"data":[]}
"""
Metodo para cargar informacion de productos:
Si el archivo de recursos no existe lo crea de forma
automatica con la estructura inicia del diccionario vacio
diccCliente = {"data":[]}
"""
def LoadInfoProducto():
    global diccProducto
    if (core.checkFile("productos.json")):
        diccProducto = core.LoadInfo("productos.json")
    else:
        core.crearInfo("productos.json",diccProducto)
def rec_can(can,v):
    v['cantidad']+=can
    return v
    
    
def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^14}{}{:^14}|".format(' ','ADMINISTRACION DE PRODUCTOS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Activar o Inactivar")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):

        data ={
            "id":input("Ingrese el Id del producto :"),
            "nombre":input("Ingrese el Nombre del producto :"),
            "cantidad":0,
            "stockMin":int(input("Ingrese el Stock minimo :")),
            "stockMax":int(input("Ingrese el Stock maximo :")),
            "valorCompra":float(input("Ingrese el valor de compra :")),
            "valorVenta":float(input("Ingrese el valor de venta :")),
            "estado":True
        }
    
        core.crearInfo("productos.json",data)
        
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE PRODUCTOS',' '))
        print('+','-'*49,'+')

        
        for i,item in enumerate(diccProducto["data"]):
            print(i,'.','NOMBRE:',item['nombre'],'ID:',item['id'])    

        op=int(input('ingresa el indice del producto deseado: '))

        item=diccProducto['data'][op]
        print(f'Id cliente : {item["id"]}')
        print(f'Nombre cliente : {item["nombre"].upper()}')
        print(f'stock Minimo : {item["stockMin"]}')
        print(f'stock Maximo : {item["stockMax"]}')
        print(f'precio de venta:{item["valorCompra"]}')
        print(f'precio de compre:{item["valorVenta"]}')
        print(f'cantidad en bodega:{item["cantidad"]} ')
        if(item['estado']==True):
            print('estado:Activo')
        else:
            print('estado:Inactivo')    
        
        
        if(op<0 or op>1):
            print('indice invalido :(')
        os.system("pause")        


    elif (opcion == 3):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DE PRODUCTOS',' '))
        print('+','-'*49,'+')
        
        for i,item in enumerate(diccProducto["data"]):
            print(i,'.','NOMBRE:',item['nombre'],'ID:',item['id'])    

        op=int(input('ingresa el indice del producto deseado: '))
        item = diccProducto["data"][op]

        item["nombre"] = input("Ingrese en nuevo nombre o presione enter para omitir :") 
        item["valorVenta"] =float(input("Ingrese en nuevo precio a venta o presione enter para omitir :")) 
        item["valorCompra"] =float(input("Ingrese en nuevo precio a compra o presione enter para omitir :")) 
        item["stockMin"]=int(input("Ingrese en nuevo stock minimo o presione enter para omitir :")) 
        item["stockMax"]=int(input("Ingrese en nuevo stock maximo o presione enter para omitir :")) 
        core.EditarData("productos.json",diccProducto)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE PRODUCTOS',' '))
        print('+','-'*49,'+')
        for i,item in enumerate(diccProducto["data"]):
            print(i,'.','NOMBRE:',item['nombre'],'ID:',item['id'])    

        op=int(input('ingresa el indice del producto deseado: '))
        
        
        print("1.Activar\n2.Inactivar")
        diccProducto["data"][op]["estado"] = True if int(input(":")) == 1 else False 
        core.EditarData("productos.json",diccProducto)
                # os.system("pause")
                # core.crearInfo("productos.json",itemDel)

    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()