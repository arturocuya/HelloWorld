palabra = input("Ingrese una palabra: ")

letras = {}
vocales = ['a','e','i','o','u']

for letra in palabra:
	if letra in vocales:
		if letra not in letras.keys():
			letras[letra] = 1
		else:
			letras[letra] += 1

for letra in letras.keys():
	print(letra + ":", letras[letra])
