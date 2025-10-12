#1 – Sistema de calificaciones de estudiantes {
#Creá un programa que guarde las notas de varios estudiantes en un diccionario,
#Luego, crea funciones para: 
# A- Agregar estudiante con sus notas
# B- Calcular el promedio de un estudiante
# C- Mostrar los estudiantes aprobados (promedio >=6)
alumnos = {
    "Ana":[9,8,10],
    "Luis":[10,10,9],
    "Carlos":[4,6,5]
}
def agregar_estudiante(base,nombre):
    if alumnos.get(nombreEstudiante) is None:
        alumnos.setdefault(nombreEstudiante,0)
        listaNotas=[]
        for contador in range(3):
            nota = int(input(f"Ingrese la nota {contador+1} de {nombreEstudiante} "))
            listaNotas.append(nota)
            alumnos[nombreEstudiante] = listaNotas
    else:
        print(f"El estudiante {nombreEstudiante} ya está ingresadp, intente nuevamente...")


def promedio_estudiante(base,nombre):
    if alumnos.get(nombreEstudiante) is None:
        print(f"El estudiante {nombreEstudiante} no está el la lista")   
    else:
        print(alumnos[nombreEstudiante])
        sumaNotas= sum(alumnos[nombreEstudiante])
        cantidadNotas= len(alumnos[nombreEstudiante]) 
        promedio =  sumaNotas / cantidadNotas  
        print(f"El promedio de {nombreEstudiante} es {promedio}")

        
def estudiantes_aprobados(base):
    for clave in alumnos:    
        promedio = sum(alumnos[clave])/len(alumnos[clave])
        if promedio >= 6:
            print(f"El promedio de {clave} es {promedio}, por lo tanto APRUEBA")


        

## CUERPO PRINCIPAL

while True:
    print("1- Agregar estudiantes y sus notas")
    print("2- Calcular promedio de estudiante")
    print("3- Mostrar estudiantes aprobados")
    print("0- Salir")
    opcionMenu=int(input("Ingrese opción (1,2,3 o 0): "))
    if opcionMenu == 1 or opcionMenu == 2 or opcionMenu == 3 or opcionMenu == 0:
        if opcionMenu == 1:
            while True:
                nombreEstudiante = input("Ingrese el nombre del estudiante (0 Para salir): ")
                if nombreEstudiante != "0":                    
                    agregar_estudiante(alumnos,nombreEstudiante)                                    
                else:
                    break            
        if opcionMenu == 2:
            while True:
                nombreEstudiante = input("Ingrese el nombre del estudiante (0 p/ salir): ")
                if nombreEstudiante != "0":
                    promedio_estudiante(alumnos,nombreEstudiante)                    
                else:
                    break
        if opcionMenu == 3:
            estudiantes_aprobados(alumnos)
        if opcionMenu == 0:
            print ("Hasta luego...")
            break            
    else:
        print("Opción incorrecta, intente nuevamente")