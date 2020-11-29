if __name__ == '__main__':
	n = int()
	p = int()
	r = int()
	c = int()
	r1 = float()
	p1 = float()
	n1 = float()
	n = 0
	p = 0
	r = 1
	c = 1
	r1 = 0
	p1 = 0
	n1 = 0
	print("Ingresar la base de la potencia")
	n = int(input())
	print("Ingresar la potencia")
	p = int(input())
	while (c<=p):
		r = r*n
		c = c+1
	r1 = n1**p1
	print("La potencia de : ",n," elvado a ",p," es: ",r)
	print("La potencia de : ",n1," elvado a ",p1," es: ",r1)

