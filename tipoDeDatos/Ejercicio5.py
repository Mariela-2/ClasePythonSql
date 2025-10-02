""" Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe 
mostrar por pantalla la paga que le corresponde. """

horasTrabajadas=float(input("Ingresa las horas trabajadas: \n"))
costoPorHora=float(input("Ingresa el costo por hora: \n"))

sueldo=horasTrabajadas*costoPorHora

print("La paga que te corresponde es: " + str(sueldo))    