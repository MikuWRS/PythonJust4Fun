# se veran tipos de datos, condicionantes, operaciones, strings, tuplas, listas, diccionarios, boleanos
# declaraciones de variables
entero=5
flotante=5.0
cadena='python'
caracter='C'

# Modulo Numeros
x = 7
y = 3

# Operadores de Numeros
#   +    -       /          *           **
# suma resta division multiplicacion potencia
# NOTA: la division siempre da el resultado como flotante
print(5+5)
print(5/5)

# Tipeo Dinamico

x=float(5)
print(x)
print(int(x))

# Methods
# var.upper() para mayusculas
# var.title() para poner la primera en mayusculas
# var.lower() para minusculas
x = "hielo seco"
print(x)
print(x.upper())
print(x.title())
print(x.lower())

# replace(x,y): reemplaza todas las "x" por "y"
print(x.replace('s','r'))

# concatenando strings
x="Wena"
y="compare"
z="que talca"
print(x+' '+y+' '+z)

# funcion .format
c="Wena compare {}"
z="perry"
print(c.format(z))
print(c.format("Sandro"))
#print(c.format(input()))
j="Jamon"
l="Lana"
st=["carlos","tiempo","lara"]
a=f"Hola {st[0]} tienes {st[1]}"
# print(a.format(j,l)) # se puede reemplazar por f"..."
print(a)

# listas []
# NOTA: el indice puede ser negativo, y tomara la posicion como si fuera un grupo ciclico
l=["pastel","choclo","papas","lechuga","zanahoria",3,3.5]
print(l)
# algunas funciones de listas
print(len(l))
print(l.pop());print(l) # saca el ultimo elemento
print(l.append(9));print(l) # agrega un elemento al final
print(l.remove(9));print(l) # saca el valor indicado

# tuplas ()
# NOTA: son igual que las listas, pero no se puede agregar ni quitar elementos
t=("Rojo", "Azul", " Verde", "Claro", "Oscuro")
print(t);print(len(t))

# diccionarios {}
d={"numero":1234, "nombre":"Carlos","comuna":"la Granja"}
d["comuna"]="Renca"
d["año"]=2020;
print(d)
print(len(d))
d.pop("año") # para usar el pop sin especificar el campo, usar x.popitem() y sacara el ultimo elemento
print(d)

# booleanos
print(5>5)
print(4<9)

# Notas

# asignaciones multiples
a=b=c=1
q,w,e=1,2,3

# tipos de datos en python
# Numeros (int, float, complex)
# strings (+ para concatenar, * para repetir)
# listas
# Tuplas
# Diccionarios


# Data Type Conversion

# int(x [,base]): Convierte x en un integer. La base se especifica si x es un string.
# float(x): Convierte x en un flotante.
# complex(real [,imag]) : Crea un numero complejo.

# str(x) : Converts object x to a string representation.
# repr(x) : Converts object x to an expression string.
# eval(str) Evaluates a string and returns an object.

# tuple(s) : Converts s to a tuple.
# list(s) : Converts s to a list.
# set(s) : Converts s to a set.
# dict(d) : Creates a dictionary. d must be a sequence of (key,value) tuples.

# frozenset(s) : Converts s to a frozen set.
# chr(x) : Converts an integer to a character.
# unichr(x) : Converts an integer to a Unicode character.
# ord(x) : Converts a single character to its integer value.
# hex(x) : Converts an integer to a hexadecimal string.
# oct(x) : Converts an integer to an octal string.




# Operadores Logicos

# and, or, note
print("Operadores")
print(5>4 and 3>1) #true
print(not 5>4 or 1>2) # false

# operadores de miembros
# is, is not: Evalua si las variables son el mismo objeto
# in, not in: Evalua si la variable esta en una secuencia especifica
y=[1,2,3,4]
print(2 not in y)

# operadores a nivel de bit
#  & ,  | , ^ ,  ~ ,     <<    ,     >>
# and, or, xor, neg, Left shift, right shift
