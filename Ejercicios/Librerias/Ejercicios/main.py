import User
import dades

salir = False

while salir == False:
    print(f"Menu:\n"
          f"1. Registrar usuario\n"
          f"2. Login\n"
          f"3. Mostrar datos de un usuario\n"
          f"4. Salir")
    opcion = input("Introduce una opción: ")
    if opcion == "1":
        usuario = input("Introduce un usuario valido: ")
        password = input("Introduce una contraseña valida: ")
        x = User.validarUsuari(usuario,password)
        print(x)
    elif opcion == "2":

    elif opcion == "3":

    elif opcion == "4":
        salir == True
    else:
        print("Error, no has introducido nignuna opción valida")

