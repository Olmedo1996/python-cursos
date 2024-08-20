### numeros
# int (integer) numero entero
numeroEntero = 1

# float número decimal
numeroDecimal = 3.14

#complex: numero complejo (parte entera y otra parte imaginaria)
numeroComplejo = 5 + 2j


print(numeroEntero) 
print(type(numeroEntero)) # int

print(numeroDecimal)
print(type(numeroDecimal)) # float

print(numeroComplejo) #(5 + 2j)
print(type(numeroComplejo)) # complex



#### Casteo, convert
decimal_desde_entero = float(numeroEntero)
entero_desde_decimal = int(numeroDecimal)
complejo_desde_entero = complex(numeroEntero)
enetro_desde_decimal = complex(numeroEntero)

print(decimal_desde_entero)
print(entero_desde_decimal)
print(complejo_desde_entero)
print(enetro_desde_decimal)

# entero_desde_complejo = int(numeroComplejo)
# print(entero_desde_complejo)


### RANDOM

import random

aleatorio = random.randrange(1, 10) #el numero de stop no es incluyente o sea hasta el 9
aleatorio_par = random.randrange(2, 11, 2) #numero par del 2 al 10
aleatorio_impar = random.randrange(1, 10, 2)#numero impar del 1 al 9

# print(aleatorio)