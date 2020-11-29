if __name__ == '__main__':
	n = int()
	tipo = str()
	n = 0
	tipo = ""
	print("Programa para verificar si un numero es par")
	print("Ingrese el numero a verificar ")
	n = int(input())
	if (n%2==0):
		tipo = "par"
	print("El numero ",n," es ",tipo)

