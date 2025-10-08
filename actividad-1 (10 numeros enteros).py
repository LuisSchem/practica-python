# ------------------------------------------------------------------------------
# Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:

# Almacenar los números ingresados en una lista.

# Calcular la suma de todos los números pares.

# Contar cuántos números impares se ingresaron.

# Mostrar por pantalla:

# La lista completa de números ingresados.

# La cantidad de los números pares.

# La cantidad de números impares

lista_numeros=[]

cantidad_impar = 0
suma_pares=0
for contador in range(10):
    numero=int(input(f"Ingrese el número {contador+1} de la lista: "))
    lista_numeros.append(numero)
for recorrida in lista_numeros:
    if numero % 2 != 0:
        cantidad_impar +=1
    else:
        suma_pares += numero
    
suma_total = sum(lista_numeros)


print(f"La lista ingresada es: {lista_numeros}")
print(f"de los cuales {10-cantidad_impar} son pares y {cantidad_impar} son impares")
print(f"La suma de los pares es {suma_pares} y la de impares es {suma_total-suma_pares}")
print(f"La suma total es {suma_total}")


