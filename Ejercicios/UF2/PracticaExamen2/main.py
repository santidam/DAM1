import user
import dates


salir = False

while salir == False:
    print("""1. Registrar usuari
2. Login
3. Mostrar dades d’un usuari
4. Sortir""")

    comando = input("Introduce un comando del menu: ").lower()
    if comando == "sortir":
        salir = True
    elif comando == "1":
        usuario = input("Introduce un nombre de usuario: ")
        contraseña = input("Introduce una contraseña: ")
        user.registrarUsuario(usuario,contraseña)

    # elif comando == "2":


    # elif comando == "3":

    # elif comando == "4":

    # else:
    #     print("Error, introduce un cmando valido")    