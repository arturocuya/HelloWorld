palabra = input("Ingrese una palabra: ")

letras = {}
encontradas = []

for letra in palabra:
	if letra not in encontradas:
		encontradas.append(letra)
		letras[letra] = 1
	else:
		letras[letra] += 1

for encontrada in encontradas:
	print(encontrada + ":", letras[encontrada])
