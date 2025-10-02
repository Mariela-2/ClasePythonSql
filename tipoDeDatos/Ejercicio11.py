""" Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. """

cantidadAhorros=float(input("Ingresa la cantidad de dinero depositada en la cuenta de ahorros: \n"))
interesAnual=0.04

ahorrosPrimerAño=cantidadAhorros*(1+interesAnual)
ahorrosSegundoAño=ahorrosPrimerAño*(1+interesAnual)
ahorrosTercerAño=ahorrosSegundoAño*(1+interesAnual)

print("La cantidad de ahorros tras el primer año es: " + str(round(ahorrosPrimerAño,2)))
print("La cantidad de ahorros tras el segundo año es: " + str(round(ahorrosSegundoAño,2)))
print("La cantidad de ahorros tras el tercer año es: " + str(round(ahorrosTercerAño,2)))    