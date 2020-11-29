if __name__ == '__main__':
	n = int()
	tipo = str()
	n = 0
	tipo = ""
	print("Programa para verificar si un numero es par o impar")
	print("Ingrese el numero a verificar ")
	n = int(input())
	if (n%2==0):
		tipo = "par"
	else:
		tipo = "impar"
	print("El numero ",n," es ",tipo)

