n_numeros = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
promedio = 0
contador = 0
pares = 0
while contador < n_numeros:
	print("Ingrese un número. Registrados ", contador, "de", n_numeros)
	numero = int(input())
	if numero%2 == 0:
		pares += 1
		promedio += numero
	contador += 1
if promedio != 0:
	promedio /= pares
	print("El promedio de los numeros pares es de: ", promedio)
else:
	print("No hay numeros pares")
