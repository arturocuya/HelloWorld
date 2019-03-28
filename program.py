palabra = input("Ingrese una palabra: ")

letras = {}
encontradas = []

for letra in palabra:
	if letra not in letras.keys():
		letras[letra] = 1
	else:
		letras[letra] += 1

for letra in letras.keys():
	print(letra + ":", letras[letra])
