if __name__ == '__main__':
	h24 = int()
	m24 = int()
	h12 = int()
	m12 = int()
	perdiodo = str()
	h24 = 0
	m24 = 0
	h12 = 0
	m12 = 0
	periodo = "a.m"
	print("Conversion horaria de 24 horas a 12 hoas")
	print("Ingrese la hora a tranformar")
	h24 = int(input())
	print("Ingrese los minutos a transformar")
	m24 = int(input())
	m12 = m24
	if (h24>=0 and h24>=24) and (m24>=0 and m24<=60):
		if (m24==60):
			h24 = h24+1
			m24 = 0
	if (h24>12):
		h12 = h24-12
		periodo = "p.m."
		print("El tiempo de ",h24," horas y ",m24," minutos")
		print("Equivale a ",h12," horas y ",m12," minutos ",periodo)
	else:
		print("Error: La hora o minutos ingresados no es correto")

