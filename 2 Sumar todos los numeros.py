# 2- Sumar todos los números {
# Definí una función sumar_todos() utilizando args que reciba una cantidad 
# indefinida de números y devuelva la suma total 
# (Acá podemos usar la función integrada de python sum )😉

listaNumeros=[]

def sumar_todo(*args):
    pass
    return sum(listaNumeros)


while True:
    numeroIngresado = int(input("Ingrese un número (0 para terminar) "))
    if numeroIngresado != 0:
        listaNumeros.append(numeroIngresado)
    else:
        print("La suma total de los números ingresados es: ",sumar_todo(listaNumeros))
        salgo=input("Continuar <S> ")
        if salgo == "S" or salgo == "s":
            pass
        else:
            print("Adios...")
            break
    