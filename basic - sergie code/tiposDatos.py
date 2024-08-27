#  str (string) texto o cadena de caracteres

comillaSimple = 'Este es un texto'
comillaDobles = "Este es un texto"
comillaTriplesDobles =  """ESTE ES UN TEXTO"""
comillaTriplesSimples =  '''ESTE ES UN TEXTO'''

# int (integer) numero entero
numeroEntero = 1

# float número decimal
numeroDecimal = 3.14

#complex: numero complejo (parte entera y otra parte imaginaria)
numeroComplejo = 5 + 2j

#list: representa una colección orenada y mutable de elementos (cada elemento tiene un indice 0 ... n )
lista = [0,1,2,3,4,5,6,7]

#tupla: coleccón ordenada e inmutable de elementos (cada elemento tiene un indice)
tupla = (0,1,2,3,4,5)

#range: frecuencia de numeros generados dentro de un rango
rango = range(1,10)

#dict: diccionario coleccion de pares clave - valor desordenada y mutable
diccionario = {
    "key": "value",
    "edad": 30,
    "diccionario": {
        "nombre":"otro string"
    }
}

#set{}: coleccion desordenada de elementos unicos y mutables
conjunto = {1, 1, 2, 5, 3}
print(conjunto)

#frozenSet([]): coleccion desordenada de elementos unicos e inmutables
conjunto_inmutables = frozenset([3,2,3,5,1])
print(conjunto_inmutables)

#bool valor verdadero o falso
booleanVerdadero = True
booleanFalse = False