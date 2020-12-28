# Metodo input()

x=input("Variable X: ")
y=input("Variable y: ")
z=int(x)+int(y)
print(z)

# convertidores int, float, etc

def temp(c):
    c=int(c)
    f=(9/5)*c + 32
    return print(f)
temp(input("Temperatura:"))



def suma(x,y):
    z=x+y
    return print(z)
a=int(input("a="))
b=int(input("b="))
suma(a,b)


def leng(m,s):
    h=int(m)/60+int(s)/3600
    return(print(h))
m=int(input("Minutos: "))
s=int(input("Segundos: "))
leng(m,s)


def div(a,b):
    if(b==0):
        return(print("Error, el divisor no puede ser 0"))
    else:
        c=a/b
        return(print(c))

a=input("Valor a: ")
b=input("Valor b: ")
div(int(a),int(b))
