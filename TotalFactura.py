if __name__ == '__main__':
	subtotal = float()
	total = float()
	descuento = float()
	limite1 = float()
	limite2 = float()
	subtotal = 0
	total = 0
	descuento = 0
	limite1 = 200
	limite2 = 500
	print("Calcular el valor de venta")
	print("Para compras mayores a USDcv200, se aplica un 10% "+"de descuento")
	print("Para compras mayores a USD 500, se aplica un 15% "+"de descuento")
	print("Ingrese el subtotal de la compra")
	subtotal = float(input())
	if (subtotal>=limite1) or (subtotal<limite2):
		descuento = 0.10
	else:
		descuento = 0.15
	total = subtotal+(subtotal*descuento)
	print("El total de la compra",total)

