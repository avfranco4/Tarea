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
	if (a>b):
		r = a
	print("Ingrese el segundo termino: ")
	b = int(input())
	if (b>a):
		r = b
	print("Ingrese el tercer termino: ")
	c = int(input())
	if (c>b):
		r = c
	print("El mayor numero es: ",r)

