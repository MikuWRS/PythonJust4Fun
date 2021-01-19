import random

def vidas_rest(vidas):
	if vidas==7:
		print("7 vidas restantes")
		print("-----------------")
		print("        0       ")
	if vidas==6:
		print("6 vidas restantes")
		print("-----------------")
		print("        0/      ")
	if vidas==5:
		print("5 vidas restantes")
		print("-----------------")
		print("       \\0/       ")
	if vidas==4:
		print("4 vidas restantes")
		print("-----------------")
		print("       \\0/       ")
		print("        |        ")
	if vidas==3:
		print("3 vidas restantes")
		print("-----------------")
		print("       \\0/       ")
		print("        |        ")
		print("       /         ")
	if vidas==2:
		print("2 vidas restantes")
		print("-----------------")
		print("       \\0/       ")
		print("        |        ")
		print("       / \\       ")
	if vidas==1:
		print("1 vidas restantes")
		print("-----------------")
		print("       \\0/_|     ")
		print("        |        ")
		print("       / \\       ")
	if vidas==0:
		print("0 vidas restantes")
		print("-----------------")
		print("        0_|      ")
		print("       /|\\       ")
		print("       / \\       ")

palabras=["torpedear","embalar","refugio","silencio","asfixiar","arrancar","especular"]
palabra=random.choice(palabras)
letrasvalidas='abcdefghijklmnñopqrstuvwxyz'
vidas=8
aciertos=''

while len(palabra)>0:
	main=""
	errores=0
	for letra in palabra:
		if letra in aciertos:
			main=main+letra
		else:
			main=main+"_"+" "
	if main==palabra:
		print(main)
		print("Ganaste\n")
		break
	print("Adivina la palabra: ",main)
	suposicion=input()

	if suposicion in letrasvalidas:
		aciertos=aciertos+suposicion
	else:
		print("Ingresar un caracter valido")
		suposicion=input()

	if suposicion not in palabra:
		vidas-=1
		vidas_rest(vidas)

	if vidas==0:
		print(palabra)
		print("Perdiste\n")
		break

#nombre=input("Hola ingresa tu nombre: ")
