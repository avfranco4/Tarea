if __name__ == '__main__':
	a = int()
	b = int()
	c = int()
	r = int()
	a = 0
	b = 0
	c = 0
	r = 0
	print("Ingrese el primer termino: ")
	a = int(input())
	print("Ingrese el segundo termino: ")
	b = int(input())
	print("Ingrese el tercer termino: ")
	c = int(input())
	if (a>b):
		r = a
	else:
		r = b
	if (b>c):
		r = b
	else:
		r = c
	if (c>a):
		r = c
	else:
		r = a
	print("El mayor numero es: ",r)

