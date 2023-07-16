import clientes
import compras
import ventas
import productos
import proveedores
import os
import msvcrt

if __name__ == "__main__":
    isActivate = True
    opcion=0
    dataproductos={'data':[]}
    dataproveedores={'data':[]}
    datacompras={'data':[]}
    dataventas={'data':[]}
    user = input('Usuario: ')
    contraseña = ""

    print("Ingresa tu contraseña: ", end="")

    while True:
                tecla = msvcrt.getch().decode('utf-8')

                if tecla == '\r' or tecla == '\n':
                    break
                elif tecla == '\b':
                    if len(contraseña) > 0:
                        contraseña = contraseña[:-1]
                        print('\b \b', end='', flush=True)
                else:
                    contraseña += tecla
                    print('*', end='', flush=True)

    os.system('clear')

    if user == '1097488722' and contraseña == 'Camilo01':

        while isActivate:
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
            print('+','-'*55,'+')
            print("1. Gestion de clientes")
            print("2. Gestion de producto")
            print("3. Gestion de Proveedores")
            print("4. Gestion de Compras")
            print("5. Gestion de ventas")
            print("6. Terminar")
            opcion = int(input(":)_"))
            if (opcion == 1):
                clientes.LoadInfoCliente()
                clientes.MainMenu()
            elif (opcion == 2):
                productos.LoadInfoProducto()
                productos.MainMenu()
            elif (opcion == 3):
                proveedores.LoadInfoProvedor()
                proveedores.MainMenu()
            elif (opcion == 4):
                compras.LoadInfoCompra()
                compras.MainMenu()
            elif (opcion == 5):
                ventas.LoadInfoCompra()
                ventas.MainMenu()
            elif (opcion == 6):
                isActivate = False
            else:
                print("Opcion no valida....")
                os.system("pause")

      
    

