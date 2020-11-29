if __name__ == '__main__':
	a = float()
	b = float()
	c = float()
	d = float()
	lc = float()
	at = float()
	ar = float()
	ats = float()
	areatotal = float()
	a = 0
	b = 0
	c = 0
	d = 0
	lc = 0
	at = 0
	ar = 0
	ats = 0
	areatotal = 0
	print("Ingrese la altura del paralelogramo")
	lc = float(input())
	print("Ingrese el largo del rectangulo")
	at = float(input())
	print("Ingrese la altura del rectangulo")
	ar = float(input())
	a = lc**2
	b = (lc*at)/2
	ats = b*3
	d = lc*ar
	areatotal = a+b+ats
	print("Area Total del paralelogramo: ",areatotal,", compuesto por un cuadrado de lado: ",a," area del triangulo ",b," area del rectangulo ",d)

