if __name__ == '__main__':
	x = int()
	n = int()
	contador = int()
	print("Escribe un numero")
	n = int(input())
	x = 1
	contador = 0
	while x<=n:
		if n%x==0:
			contador = contador+1
		x = x+1
	if contador==2:
		print("El numero ",n," es primo")
	else:
		print("El numero ",n," no es primo")

