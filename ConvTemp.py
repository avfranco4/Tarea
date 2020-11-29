if __name__ == '__main__':
	gc = float()
	gf = float()
	gk = float()
	gc = 0
	gf = 0
	gk = 0
	print("Programa para convertir de grados centigrados a grados Farenheit y a grados grados kelvin ")
	print("Ingrese los grados centigrados")
	gc = float(input())
	if (gc>0):
		gf = (gc*9/5)*32
		gk = (gc+273.15)
		print("La equivalencia en grados F es ",gf)
		print("La equivalencia en grados K es ",gk)

