# Para Python 3 usar input(), para Python 2.7 usar raw_input() 
import random
def dado(numero):
	if numero==1:
		print("|-------|")
		print("|       |")
		print("|   0   |")
		print("|       |")
		print("|-------|")
	elif numero==2:
		print("|-------|")
		print("| 0     |")
		print("|       |")
		print("|     0 |")
		print("|-------|")
	elif numero==3:
		print("|-------|")
		print("| 0     |")
		print("|   0   |")
		print("|     0 |")
		print("|-------|")
	elif numero==4:
		print("|-------|")
		print("| 0   0 |")
		print("|       |")
		print("| 0   0 |")
		print("|-------|")
	elif numero==5:
		print("|-------|")
		print("| 0   0 |")
		print("|   0   |")
		print("| 0   0 |")
		print("|-------|")
	elif numero==6:
		print("|-------|")
		print("| 0   0 |")
		print("| 0   0 |")
		print("| 0   0 |")
		print("|-------|")

x="r"
while x == "r":
	dado(random.randint(1,6))
	#x=input("Presiona r para lanzar el dado")
	x=raw_input("Presiona r para lanzar el dado ")