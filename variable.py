nombre = input("Ingresa tu nombre ")
ventas = float(input("Ingresa el total de tus ventas "))
print(f"Hola, {nombre} \nTus ventas fueron de: {ventas}\nTu comision es de: {round(ventas * 0.13,2)}")