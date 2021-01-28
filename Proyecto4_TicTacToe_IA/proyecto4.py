
tablero=[' ' for x in range(10)]
c_posicion='123456789'

def insertar(marca,ins_posicion):
	tablero[ins_posicion]=marca

def p_tablero(tablero):
	print("     |     |     \n")
	print("  "+tablero[1]+"  |  "+tablero[2]+"  |  "+tablero[3]+"  \n")
	print("     |     |     \n")
	print("------------------\n")
	print("     |     |     \n")
	print("  "+tablero[4]+"  |  "+tablero[5]+"  |  "+tablero[6]+"  \n")
	print("     |     |     \n")
	print("------------------\n")
	print("     |     |     \n")
	print("  "+tablero[7]+"  |  "+tablero[8]+"  |  "+tablero[9]+"  \n")
	print("     |     |     \n")

def espaciolibre(esp_posicion):
	return (tablero[esp_posicion]==' ')

def tablerolleno(tablero):
	if tablero.count(' ')>1:
		return False
	else:
		return True

def ganador(tablero,marca):
	return ((tablero[1]==marca and tablero[2]==marca and tablero[3]==marca) or
	        (tablero[4]==marca and tablero[5]==marca and tablero[6]==marca) or
	        (tablero[7]==marca and tablero[8]==marca and tablero[9]==marca) or
	        (tablero[1]==marca and tablero[4]==marca and tablero[7]==marca) or
	        (tablero[2]==marca and tablero[5]==marca and tablero[8]==marca) or
	        (tablero[3]==marca and tablero[6]==marca and tablero[9]==marca) or
	        (tablero[1]==marca and tablero[5]==marca and tablero[9]==marca) or
	        (tablero[3]==marca and tablero[5]==marca and tablero[7]==marca))

def turnojugador():
	while True:
		turno=input("Ingrese posicion para marcar (1-9)\n")
		if turno in c_posicion:
			turno=int(turno)
			if espaciolibre(turno):
				insertar('X',turno)
				break
			else:
				print("El espacio ya esta ocupado\n")
		else:
			print("Seleccione una posicion correcta\n")

def turnoIA():
	movposibles=[x for x, marca in enumerate(tablero) if marca==' ' and x != 0]
	movimiento=0
	for marca in ['O','X']:
		for m in movposibles:
			c_tablero=tablero[:]
			c_tablero[m]=marca
			if ganador(c_tablero,marca):
				movimiento=m
				return movimiento

	esquinas=[]
	for i in movposibles:
		if i in [1,3,7,9]:
			esquinas.append(i)
	if len(esquinas) > 0:
		turno=selrandom(esquinas)
		return turno
	if 5 in movposibles:
		turno=5
		return turno
	lados=[]
	for i in movposibles:
		if i in [2,4,6,8]:
			lados.append(i)
	if len(lados)>0:
		turno=selrandom(lados)
		return turno

def selrandom(lista):
	import random
	l=len(lista)
	r=random.randrange(0,l)
	return lista[r]

def main():
	print("Bienvenido al 3 en raya\n")
	p_tablero(tablero)
	while not(tablerolleno(tablero)):
		if not(ganador(tablero,'O')):
			turnojugador()
			p_tablero(tablero)
		else:
			print("Lo siento, perdiste\n")
			break
		if not(ganador(tablero,'X')):
			turno=turnoIA()
			if turno==0:
				print(" ")
			else:
				insertar('O',turno)
				print("IA puso un O en la posicion ",turno,":\n")
				p_tablero(tablero)
		else:
			print("Has Ganado\n")
			break

	if tablerolleno(tablero):
		print("Empate\n")



main()
while True:
	x=input("Quieres jugar otra vez? (s/n)\n")
	if x.lower()=='y':
		tablero=[' ' for x in range(10)]
		print('-------------------------\n')
		main()
	elif x.lower()=='n':
		break
	else:
		print("Ingrese una opcion correcta\n")
