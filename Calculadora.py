if __name__ == '__main__':
	n = float()
	n1 = float()
	n2 = float()
	r = float()
	n1 = 0
	n2 = 0
	r = 0
	op = 10
	print("Calculadora Basica")
	while op!=0:
		print("Ingrese el valor del numero 1")
		n1 = float(input())
		print("Ingrese el valor del numero 2")
		n2 = float(input())
		print("")
		print("Eligir un numeo del 1 al 4")
		op = float(input())
		print("1- Sumar")
		print("2- Restar")
		print("3- Multiplicar")
		print("4- Dividir")
		print("")
		if op==1:
			r = n1+n2
			print("La Respuesta es: ",r)
		elif op==2:
			r = n1-n2
			print("La Respuesta es: ",r)
		elif op==3:
			r = n1*n2
			print("La Respuesta es: ",r)
		elif op==4:
			r = n1/n2
			print("La Respuesta es: ",r)
		else:
			print("Sistema finalizado")

