""" Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
anual y el número de años, y muestre por pantalla el capital obtenido en la inversión. """

cantidadAInvertir= float(input("Ingresa la cantidad a invertir: \n"))
interesAnual=float(input("Ingresa el interés anual \n"))
numeroDeAños=int(input("Ingresa el número de años: \n"))

CapitalFinal=(cantidadAInvertir*(1+ interesAnual/100)**numeroDeAños)
print("El capital obtenido en la inversión es: " + str(CapitalFinal))


