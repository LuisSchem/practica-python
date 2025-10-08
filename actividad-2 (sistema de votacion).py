# Nivel 4 | Sistema de votación {
# Se quiere implementar un sistema básico de votación donde cada persona puede votar una
# sola vez por su candidato favorito
# A- El programa debe permitir que tres personas voten
# B- Antes de permitir votar, debe pedir el nombre del votante
# C- Si el votante ya emitió su voto anteriormente, debe mostrar un mensaje: “Ya votaste” y
# no permitirle votar de nuevo
# D- Si es la primera vez que vota, el sistema debe pedir el nombre del candidato al que desea
# votar.
# E- Al finalizar, el programa debe mostrar los resultados con la cantidad de votos que recibió
# cada candidato
# }


cantidadDeVotantes=1
##nombreVotante = " "
##numeroCandidato = 0
votantes = {}
votaciones = {}



while cantidadDeVotantes <= 3:
    nombreVotante = input("Ingrese su nombre: ")
    if votantes.get(nombreVotante) is None:
            while True:
                  numeroCandidato = int(input("Por favor, elija su candidato (Opción 1-2-3) \n 1- Candidato 1 \n 2- Candidato 2 \n 3- Candidato 3 \n Opción: "))
                  if numeroCandidato == 1 or numeroCandidato == 2 or numeroCandidato == 3:
                        votantes.setdefault(nombreVotante,0)
                        votaciones[numeroCandidato] = votaciones.get(numeroCandidato, 0) + 1
                        cantidadDeVotantes += 1
                        break
                  else:
                        print(f"Estimado {nombreVotante} Ud eligió {numeroCandidato} y solo puede elegir las opciones 1, 2 o 3. Inténtelo nuevamente")
    else: 
          print(f"Estimado {nombreVotante}, Ud ya votó, no puede hacerlo nuevamente... lo esperamos en otra oportunidad")

print (votaciones)





      

      
