import core


import os



bold = "\033[1m"

diccProducto = {"data":[]}
diccProducto=core.LoadInfo("productos.json")
diccProvedores = {"data":[]}
diccProvedores=core.LoadInfo("proveedores.json")
diccCompra={"data":[]}
diccDevo={"data":[]}
def LoadInfoDevo():
    
    global diccProvedores
    if (core.checkFile("devoluciones.json")):
        global diccDevo
        diccDevo = core.LoadInfo("devoluciones.json")
        
    else:
        core.crearInfo("devoluciones.json",diccCompra)

def LoadInfoCompra():
    global diccProducto
    global diccCompra
    global diccProvedores
    if (core.checkFile("compras.json")):
        
        diccCompra = core.LoadInfo("compras.json")
        
    else:
        core.crearInfo("compras.json",diccCompra)


def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE COMPRAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Devolución")
    print("4. Anular factura de compra")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    os.system('clear')
    band=True
   
    if (opcion == 1):
            data = {
            'productos': [],
            'fecha': '',
            'id': '',
            'provedor': '',
            'total': 0,'cproducto':[]
            

            }

            while band: 
                os.system('clear') 
                print('+', '-' * 55, '+')
                print("|{:^16}{}{:^17}|".format(' ', 'REGISTRO DE COMPRA', ' '))
                print('+', '-' * 55, '+')

                print(' 1. Ingresar productos.\n',
                '2. Ingresar fecha.\n',
                '3. Ingresar identificador de factura.\n',
                '4. Ingresar proveedor.\n','5.volver a registro de compra.')
                

                op = int(input(':'))
                os.system('clear')
        
                if op == 1:
                 can = int(input('Ingresa la cantidad de productos que deseas añadir: '))
                 for _ in range(can):
                    for i, item in enumerate(diccProducto['data']):
                        print(i, '.', 'NOMBRE:', item['nombre'], 'ID:', item['id'])
                    ni = int(input('Ingresa el índice del producto que deseas añadir a tu compra: '))
                    os.system('clear')
                    item = diccProducto["data"][ni]
                    print('la cantidad actual en bodega de ',item['nombre'],'es de ', item['cantidad'],' unidades')
                    os.system('clear')
                    h=item['stockMax']
                    t=-item['cantidad']+h
                    cafp = int(input('Cantidad de producto que deseas comprar: '))
                    os.system('clear')
                    
                    if(item['cantidad']>h):
                        print('la cantidad ingresada es mayor que la capacidad actual para el producto', item['nombre'],' \n vuelva a ingresar el producto con una cantidad inferior.')
                        input('presiona enter para continuar...')
                        os.system('clear')
                        print('recuerda que debe ser menor a la capacidad producto disponible en bodega ',t,' unidades')
                        cafp = int(input('Cantidad de producto que deseas comprar: '))
                        item['cantidad']+=cafp
                        data['cproducto'].append(cafp)
                        os.system('clear')
                    else:
                        item['cantidad'] += cafp
                        data['cproducto'].append(cafp)

                        os.system('clear')
                        
                    
                    tp = item['valorCompra']
                    
                    data['total'] += cafp * tp
                    
                    data['productos'].append(item)
                    core.EditarData("productos.json",diccProducto)
                    
                 input('pulsa enter para continuar....')
                 os.system('clear')

                if op == 2:
                 data['fecha'] = input('Ingresa la fecha de la compra: ')
                 os.system('clear')

                if op == 3:
                 data['id'] = input('Ingresar número de identificación de la factura de compra: ')
                 os.system('clear')
                if op == 4:
                    for i, item in enumerate(diccProvedores['data']):
                        print(i, '.', 'NOMBRE:', item['nombre'], 'ID:', item['id'])
                    os.system('clear')
                    co = int(input('Ingresa la numeración del proveedor de la factura: '))
                    os.system('clear')
                    item = diccProvedores['data'][co]
                    data['provedor']=item
                        
                if op==5:
                 band=False
                 core.crearInfo('compras.json',data)
        
       
    
    if opcion == 2:
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSQUEDA DE COMPRAS',' '))
        print('+','-'*49,'+')
        for i, item in enumerate(diccCompra["data"]):
            print(i, '.', 'FECHA:', item['fecha'], 'ID:', item['id'])    

        op = int(input('Ingresa el índice de la factura deseada: '))
        factura_seleccionada = diccCompra['data'][op]
        print('\033[1m', '       FACTURA DE PAGO      ')
        print('PRODUCTOS:')
        for producto in factura_seleccionada['productos']:
            id = producto['id']
            nom = producto['nombre']
            vv = producto['valorVenta']
            vc = producto['valorCompra']
            c = producto['cantidad']
            print('ID:', id, 'NOMBRE:', nom, '    VALOR DE VENTA:', vv)
            print('VALOR DE COMPRA:', vc, 'CANTIDAD:', c)
            p1=factura_seleccionada['provedor']['id']
            p2=factura_seleccionada['provedor']['nombre']
            p3=factura_seleccionada['provedor']['email']
        print('PROVEEDOR:')
        print('ID PRO:',p1)
        print('NOMBRE PRO:',p2)
        print('EMAIL PRO:',p3)
        print('\033[1m', 'TOTAL:', factura_seleccionada['total'])
        os.system('pause')
    





    if opcion == 3:
      os.system("clear")
      print('+', '-' * 49, '+')
      print("|{:^16}{}{:^15}|".format(' ', 'DEVOLUCION DE COMPRAS', ' '))
      print('+', '-' * 49, '+')
      for i, item in enumerate(diccCompra["data"]):
          print(i, '.', 'FECHA:', item['fecha'], 'ID:', item['id'])

      op = int(input('Ingresa el índice de la compra en devolución: '))
      factura_seleccionada = diccCompra['data'][op]

      for producto, cantidad_devuelta in zip(factura_seleccionada['productos'], factura_seleccionada['cproducto']):
          id_producto = producto['id']
          cantidad_devuelta = int(cantidad_devuelta)

        
          for item_producto in diccProducto['data']:
              if item_producto['id'] == id_producto:
                  item_producto['cantidad'] -= cantidad_devuelta
                  break

     
      core.EditarData("productos.json", diccProducto)

      item_devolucion = diccCompra["data"].pop(op)
      diccDevo['data'].append(item_devolucion)

      
      core.EditarData("compras.json", diccCompra)
      core.crearInfo("devoluciones.json", diccDevo)

      os.system('pause')

        
    if (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE COMPRAS',' '))
        print('+','-'*49,'+')
        for i,item in enumerate(diccCompra["data"]):
            print(i,'.','FECHA:',item['fecha'],'ID:',item['id'])    

        op=int(input('ingresa el indice de la compra que desea eliminar: '))
        
        item=diccCompra['data'][op]
        itemDel = diccCompra["data"].pop(op)
        core.EditarData("compras.json",diccCompra)
    if (opcion == 5):
            isCliRun = False
    if (isCliRun):
            MainMenu()