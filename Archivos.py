file=open("texto.txt", "r", encoding="utf-8")
       # (../direccion/archivo, r=read;w=write;a=append, encoding="utf-8")
x=file.read()
print(x)
file2=open("texto.txt","a")
#file2.write("Ra\n")
#file2.write("Seth\n")
nordicos=open("Nordicos.txt","w")
nordicos.write("Freyja")
nordicos.close()
file.close()


# otros tipos de metodos para archivos
# r: solo lectura
# w: solo escritura, sobreescribe si existe
# a: solo escritura, si existe agrega al final del archivo
# x= r | w | a
# x+: permite tanto escritura como lectura
# xb: permite formato binario segun x
# xb+: permite tanto escritura como lectura en formato binario segun x

# Atributos de file.
# closed: retorna si el archivo esta cerrado o no
# mode: retorna el metodo del archivo (r,w,a)
# name: retorna el nombre del archivo

file3=open("Nordicos.txt","r+")
y=file3.read()
print(y)
