if __name__ == '__main__':
	dm = int()
	a = int()
	m = int()
	d = int()
	aa = int()
	ma = int()
	da = int()
	an = 1970
	mn = 1
	dn = 1
	aa = 2013
	ma = 3
	da = 12
	print("Fecha actual (dd mm aa)")
	da = int(input())
	ma = int(input())
	aa = int(input())
	if an<1970 and an>2010:
		print("Has introducido un año invalido")
	print("Introduce año nacimiento")
	an = float(input())
	if mn<1 and mn>12:
		print("Has introducido un mes invalido")
	print("Introduce mes de naciemiento")
	mn = float(input())
	if mn==1:
		mes = "Enero"
		dm = 31
	elif mn==2:
		mes = "Febrero"
		dm = 28
	elif mn==3:
		mes = "Marzo"
		dm = 31
	elif mn==4:
		mes = "Abril"
		dm = 30
	elif mn==5:
		mes = "Mayo"
		dm = 31
	elif mn==6:
		mes = "Junio"
		dm = 30
	elif mn==7:
		mes = "Julio"
		dm = 31
	elif mn==8:
		mes = "Agosto"
		dm = 31
	elif mn==9:
		mes = "Septiembre"
		dm = 30
	elif mn==10:
		mes = "Octubre"
		dm = 31
	elif mn==11:
		mes = "Noviembre"
		dm = 30
	elif mn==12:
		mes = "Diciembre"
		dm = 31
	if dn<1 and dn>dm:
		print("Has introducido un dia invalido")
	print("Introduce el dia de tu nacimiento")
	dn = float(input())
	if (ma)==(mn):
		if (da)==(dn):
			a = aa-an
			m = 0
			d = 0
			print("Caso 1")
		if (da)>(dn):
			a = aa-an
			m = 0
			d = da-dn
			print("Caso 2")
		if (da)<(dn):
			a = aa-an-1
			m = 11
			d = 30-d
			print("Caso 3")
	else:
		if da>dn:
			if da==dn:
				a = aa-an
				m = ma-mn
				d = 0
				print("Caso 4")
			if da>dn:
				a = aa-an
				m = ma-mn
				d = da-dn
				print("Caso 5")
			if da<dn:
				a = aa-an
				m = ma-mn
				d = 30-d
				print("Caso 6")
		else:
			if da==dn:
				a = aa-an-1
				m = mn-ma
				m = 12-m
				d = 0
				print("Caso 7")
			if da>dn:
				a = aa-an-1
				m = mn-ma
				m = 12-m
				d = da-dn
				print("Caso 8")
			if da<dn:
				a = aa-an-1
				m = mn-ma+1
				m = 12-m
				d = da-dn
				d = 30-d
				print("Caso 9")
	print("Naciste el: ",dn," de ",mes," de ",an)
	print("Tu edad es: ",a," años ",m," meses y ",d," dias")

