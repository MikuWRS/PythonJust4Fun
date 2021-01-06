import json
from difflib import get_close_matches

data=json.load(open("datos.json"))

def buscar(palabra):
	palabra=palabra.lower()
	if palabra in data:
		return data[palabra]
	elif palabra.title() in data:
		return data[palabra.title()]
	elif palabra.upper() in data:
		return data[palabra.upper()]
	elif len(get_close_matches(palabra,data.keys()))>0:
		print("Quisiste decir %s?" %get_close_matches(palabra,data.keys())[0])
		opcion=input("Presiona 's' para si o 'n' para no: ")
		if opcion == 's':
			return data[get_close_matches(palabra,data.keys())[0]]
		elif opcion=='n':
			return "La palabra no esta en el diccionario o no existe"
	else:
		return "Ingresa una opcion correcta"



palabra=input("Ingrese la palabra que quiere buscar: ")
salida=buscar(palabra)
if type(salida)==list:
	for elemento in salida:
		print(elemento)
else:
	print(salida)