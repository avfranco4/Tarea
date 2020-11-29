if __name__ == '__main__':
	c = int()
	n = int()
	num = int()
	sp = int()
	so = int()
	sn = int()
	spo = int()
	c = 1
	n = 1
	num = 0
	sp = 0
	so = 0
	sn = 0
	spo = 0
	print("Ingrese el limite de numeros a verificar")
	n = int(input())
	while (c<=n):
		print("Ingrese el numero a verificar")
		num = int(input())
		if (num%2==0):
			sp = sp+num
		else:
			so = so+num
		if (num>0):
			spo = spo+num
		else:
			sn = sn+num
		c = c+1
		print("La suma de los pares es: ",sp)
		print("La suma de los impares es: ",so)
		print("La suma de los positivos es: ",spo)
		print("La suma de los pares es: ",sn)

