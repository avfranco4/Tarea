if __name__ == '__main__':
	i = int()
	n = int()
	suma = int()
	i = 1
	n = 0
	suma = 0
	print("Ingrese el limite de numeros a presentar")
	n = int(input())
	while (i<=n):
		print(i)
		suma = suma+i
		i = i+1
	print("La suma de los numeros es: ",suma)

