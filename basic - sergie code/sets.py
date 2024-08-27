#SETS: una coleccion desordenaada de elementos unicos y mutables

# sets son elementos unicos que no permite duplicados
# se pueden agregar y eliminar elementos pero los elementos no son cambianbles ya que no tienen un orden
from os import remove


conjunto = {1, 1,1, 2,2, 3,3}
print(conjunto)

#no se puede
# conjunto[1] = 6 
# print(conjunto) #error

#puede ser de varios tipos de datos
# conjunto = {1,True, "string", 2.3}


longitud = len(conjunto) #3 no toma en cuenta los duplicados
print(longitud)


tipo = type(conjunto)
print(tipo) #class set



constructor = set(("Es", "este", "un", "conjunto", "?")) #imprime de forma desordenada
print(constructor) #{'Es', 'este', 'un', '?', 'conjunto'}


if "conjunto" in constructor:
    print("Exite en el set")


if "python" not in constructor:
    print("no esta")

# agregar elementos a un conjunto set
telefonos = {"xiaomi", "samsung", "motorola"}
telefonos2 = {"nokia", "huawei", "onePlus"}

telefonos.add("motorola")
print(telefonos)

telefonos.add("Iphone")

telefonos.update(telefonos2) #sumamos otra coleccion (puede ser cualquier colleccion)
print(telefonos)


#eliminar )al no tener un orden en especifico debemos tener cuiddado al borrar un elemento del set
autos = {"Ferrari", "Peugeot", "Fiat", "Renault", "Ford", "Toyota"}

autos.remove("Ferrari") #tendras un error si el nombre o elemento no esta en el conjunto, esto es por si quieras controlar el error
print(autos) #

autos.discard('Kia') #no da un error si no existe

autos.pop() #eleminara uno de forma aleatoria 
print(autos)

autos.clear() #elimina todos los elementos
print(autos)


#recorrer los elementos en un bucle ,es igual a todos los otros conjuntos pero imprime de forma desordenada y no podras usar indices
meses = {'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'}

for mes in meses:
    print(mes) #como no tiene un orden especifico cada vez se imprime otro valor en el orden

[print(mes) for mes in meses] #shorthand

#join de conjuntos Teoria de conjuntos de la matemática
a = {1,2,3,4,5}
b = {1,3,5,7,9}

booleanos = {True, False}
#unión
u = a.union(b) # ocupa otro espacio en memoria no modifica el conjunto original, en cambio update modifica el conjunto original
u2 = a | b # signigica "a o b", es iguala union hace exactamente lo mismo
print("union", u)
print("con |", u2)

#intersección
i = a.intersection(b)
i2 = a & b
print(i) # {1 , 3, 5} # elementos en comun
print(i2) # igual a intersection se dice " y "

#modifica el conjunto original
# a.intersection_update(b)
# print(a)

#comportamiento con booleanos
booleanos_union = a.union(booleanos)
print(booleanos_union)