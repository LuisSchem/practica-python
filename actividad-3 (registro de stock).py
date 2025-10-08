# Nivel 2 | Registro de Stock {
# Dado un diccionario llamado stock que contiene productos como claves y una tupla con su
# precio y cantidad disponible como valor, escribí un programa que:
# A- Le pida al usuario que ingrese el nombre de un producto
# B- Verifique si el producto existe en el diccionario
# C- Si existe, muestre por pantalla el precio y la cantidad disponible
# D- Si no existe, deja un mensaje de que no se encontró el producto
# }

stock = {
    "atun":(2500,25),
    "picadillo":(500,30),
    "fideos":(800,250),
    "aceite":(2000,35)
    }
articuloBusco = ""


while True:
    articuloBusco = input("Ingrese nombre de artículo (0 para salir) ")
    if articuloBusco == "0":
        print("Salida...")
        break
    else:
        if articuloBusco in stock:
            precio,cantidad=stock[articuloBusco]
            print(f"Cada unidad de {articuloBusco}, cuesta $ {precio} y hay {cantidad} unidades")
        else:
            print("Artículo no encontrado...")  
            
            

