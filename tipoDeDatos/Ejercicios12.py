""" Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
fresca y el coste final total. """

barrasDePanNoFrescasVendidas=int(input("Ingresa el número de barras de pan no frescas vendidas: \n"))
precioHabitualPorBarraDePan=3.49  
descuentoPorNoSerFresca=0.60
costoFinalTotal=(barrasDePanNoFrescasVendidas*precioHabitualPorBarraDePan*(1-descuentoPorNoSerFresca))  
print("El precio habitual de una barra de pan es: " + str(precioHabitualPorBarraDePan) + " €")
print("El descuento que se le hace por no ser fresca es del 60%")
print("El coste final total es: " + str(round(costoFinalTotal,2)) + " €")