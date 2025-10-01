Intentos=3
Usuario = ""
Contrasenia = ""
while Intentos != 0:
    Usuario= input ("Ingrese usuario: ")
    Contrasenia = input ("Ingrese contraseña: ")
    if Usuario == 'admin' and Contrasenia == 'dificil123':
        print("Login exitoso... ¡¡Bienvenido!!")
        Intentos=0
        
    else:
        print("Credenciales incorrectas!")
        Intentos -= 1
        print("Le quedan ", Intentos," intentos")
       