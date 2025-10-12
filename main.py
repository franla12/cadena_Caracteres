from aritmeticas import *

nombre_jugador = (input("¿Cual es tu nombre, cadete espacial?: "))
mensaje_inicial = f"Saludos, {nombre_jugador}. El Guardián te pondrá a prueba... "
mensaje_comienzo = "\nComienza la prueba de fuerza... "
mensaje_logica = "\nComienza la prueba logica..."
mensaje_primer_prueba = "1| ¿El primer número es mayor que el segundo? \n2| ¿El primer número es igual al segundo? \n3| ¿El segundo número es menor o igual que 10? \nElija la opción correcta: "
numero_uno = int(input("Ingrese el primer numero: "))
numero_dos = int(input("Ingrese el segundo numero: "))
print(mensaje_inicial)
input(mensaje_comienzo)

print(f"La suma de ambos numeros es: {mostrar_suma(numero_uno, numero_dos)}")
print(f"La resta de ambos numeros es: {mostrar_resta(numero_uno, numero_dos)}")
print(f"La multiplicacion entre ambos numeros es: {mostrar_multiplicacion(numero_uno, numero_dos)}")
print(f"La division entre ambos numeros es: {mostrar_division(numero_uno, numero_dos)}")

input(mensaje_logica)
input(mensaje_primer_prueba)











