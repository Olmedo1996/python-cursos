# Variables:
# Es un contenedor para almacenar valores de datos
# este contenedor va a tener un nombre
# Es creada la primera vez que se le asigna un valor


x=5
txt = "Esto es un texto"
X = 6

print(x)
print(X)
print(txt)

# nombres admitidos
# puede empezar con una letra o guión bajo 
mivariable = "texto"
_mivariable = 'otro texto'
MiOtraVariable = """
Otro texto más
"""

_MiOtraVariable = """
otro más
"""

print(mivariable)
print(_mivariable)
print(MiOtraVariable)
print(_MiOtraVariable)

# no puede empezar con numero
# 5Variables = "Texto"

# Solo pueden contener caracteres alfanuméricos y guiones bajos (A-z 0-9 _)
miVariable123_ = "texto"
_123miVariable_123 = "texto"
# miVariable$
# miVariable-
# miVariable#


#CaseSesitive
miVariable = "otro valor"
MiVariable = "Otro Valor"

# No se puede utilizar palabras reservadas de python
#False = "hola"
#True = 1231231


# Convenciones de escritura de variables
# Camel case
camelCase = "Comienza con minuscula y cada palabra siguiente comenzará con mayúscula"

#pascal case
PascalCase = "Comienza con mayúscula y cada palabra siguiente comenzará con mayúscula"

#Snake case
snake_case = "se usan las palabras en minúscula y las palabras son separadas con guiones bajos"


#### Multiasignación

x, y, z = 5, 7, 9

print(x)
print(y)
print(z)

a = b = c = "code"

print(a)
print(b)
print(c)

# desde colecciones
frutas = ["manzana", "naranja", "banana"]
m,n, o = frutas

print(m)
print(n)
print(o)


# uso de print y salidas 
txt = "curso"
txt2 = "de"
txt3 = "python"

print(txt + txt2 + txt3)
print(txt , txt2 , txt3)

# Variable globales vs variables de scope

variableGlobal = "para todo el programa"

def funcion():
    # variableGlobal = "cambio la variable global solo dentro de la funcion"
    variableScope = "solo disponible en la funcion"
    global VariableScope
    VariableScope = "variable scope convertida a variable global"

    print(variableGlobal)
    print(variableScope)

funcion()

print(variableGlobal)
print(VariableScope)

# print(variableScope)