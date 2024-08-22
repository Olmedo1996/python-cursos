### Operadores

## operadores aritméticos (+, -, *, /, %, ** ,//)
a= 10
b = 5

#suma
print(a+b)
#resta
print(a-b)
#multiplicación
print(a*b)
#división
print(a/b) #devuelve flotante

#floorDivision
floorDivision = a // b #entero
print(floorDivision)
#resto
resto = a % b
print(resto)


print("resultado:", floorDivision)
print("resto:", resto)


#exponenciacion

print(a**b)


#Asinación:
x=10
print(x)
x += 3 #suma al anterior
print(x)
x -= 3 #resta al anterior
print(x)
x *= 3
print(x) # multiplica
x /= 3
print(x) #divide
x //= 3
x %= 2
x **= 2

#operadores de comparación (True o False)

num1 = 5
num2 = 5

print(num1 == num2) #si son iguales True
print(num1 != num2) #si son distitntos True
print(num1 > num2) # mayor a 
print(num1 < num2) #menor a 
print(num1 >= num2) #mayor o igual
print(num1 <= num2) #menor o igual 

#operadores logicos (and, or, not)

edad = 17

tramite = edad >= 18 and edad <= 65
print("tramite:", tramite)

semaforo = "Verde"
cruzar = semaforo == "Verde" or semaforo == "Amarillo"
print("cruzar", cruzar)

verdad = True
print("niega:", not verdad)

#operdores de identidad
nombre = "Diego Olmedo"
profesor = "Diego Olmedo"
alumno = "Blanca"
sonIguales = nombre is profesor
print("son iguales", sonIguales)

sonDistintos = profesor is not alumno
print("son distintos", sonDistintos)


#operdaores de pertenencia (is, not in)
palabra = "Mundo"
texto = "Hola Mundo"
pertenece = palabra in texto
noPertenece = "Mundo2" not in texto
print("Mundo pertenece a 'Hola Mundo'", pertenece) #compara pertenencia
print("Mundo2 no pertenece a 'Hola Mundo'", noPertenece) #compara no pertenencia


