testigo=True

for Intentos in range (3):
    Usuario= input ("Ingrese usuario: ")
    Contrasenia = input ("Ingrese contraseña: ")
    if Usuario == 'admin' and Contrasenia == 'dificil123':
        print("Login exitoso... ¡¡Bienvenido!!")
        testigo=False
        break        
    else:
        print("Credenciales incorrectas!")
        print(f"Le quedan {3-Intentos} intentos")

if testigo:
    print("Lo siento... agotó sus intentos, vuelva a repetir el ingreso")

     