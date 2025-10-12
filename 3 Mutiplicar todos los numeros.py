#3- Mutiplicar todos los números 
#Escribí una función multiplicar() utilizando args, que reciba varios números 
# y devuelva el resultado de multiplicarlos todos.

listaNumeros=[]

def multiplicar(*args):
    producto = 1
    for numero in listaNumeros:
        producto *= numero        
    return(producto)
    


while True:
    numeroIngresado = int(input("Ingrese un número (0 para terminar) "))
    if numeroIngresado != 0:
        listaNumeros.append(numeroIngresado)
    else:
        
        print("El producto de la lista de los números ingresados es: ",multiplicar(listaNumeros))
        salgo=input("Continuar <S> ")
        if salgo == "S" or salgo == "s":
            pass
        else:
            print("Adios...")
            break