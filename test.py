
# En este archivo se realizaron pruebas antes de agregar lineas de codigo al programa principal.

import os
from datetime import datetime, tzinfo, time, timezone, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))

req = "SaldosUsuario.txt"

file = os.path.join(dir_path,req)

outputFile = open(file,"r+")

a = outputFile.readlines()

print(a)

b = a[1]

print(b)

c = a[2].split()

d = a[3].split()

b[6] = str(float(b[6]) + 200)

c[6] = str(float(c[6]) + 200)

d[7] = str(float(d[7]) + 200)



b.append("\n")
c.append("\n")
d.append("\n")

a[1] = " ".join(b)

a[2] = " ".join(c)

a[3] = " ".join(d)

#print(a)

outputFile.close()

#outputFile = open(file,"w")

#outputFile.writelines(a)

#outputFile.close()

codigosContactos = {1503021029384756:"Peter",2005994729105638:"Marcus",3009955638104729:"Leo"}

def escontacto(codigo):
    return codigo in codigosContactos.keys()

today = datetime.now()

#b = a[1]

#print(b)
#c = a[2].split()
#d = a[3].split()

#b[6] = float(b[6]) + 200
#c[6] = float(c[6]) + 200
#d[7] = float(d[7]) + 200

#print(str(b[6]))
#print(str(c[6]))
#print(str(d[7]))