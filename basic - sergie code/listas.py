#LISTAS: colección (array) de datos que permite almacenar múltiples elementos en una sola varibale (parecido a array de javascript)
#cáracteristicas: ordenada (podemos ingresar a un elemento por indice u obtenerlo) y es mutable 


# indice:     0         1          2       3
frutas = ['naranja', 'Manzana', 'Pera', 'Pera'] #permite duplicados

longitud = len(frutas)

# se puede tener listas de strings, number y booleans
# asi tambien una lista mixta de distintos tipos de datos

tipo = type(frutas) #esti es el tipo de datos, es list
print(tipo)


#desde constructor
listaDesdeConstructor = list(('Beta', 2, True)) #doble parentesis
print(listaDesdeConstructor)


#acceder a los datos:
naranja = frutas[0]
print(naranja)

parteLista = frutas[1:3] #desde 1(manzana) hasta 3 no incluye
print(parteLista)

desdeElComienzo = frutas[:2]
print(desdeElComienzo)

hastaElFinal = frutas[2:]
print(hastaElFinal)


#valores negativos
pera = frutas[-1]
print(pera)

parteLista = frutas[1:-1]
print(parteLista)


#verificar si existe en lista

if "Manzana" in frutas:
    print("si existe")

print("si existe") if "Manzana" in frutas else print("no existe")


#cambiar los datos de una lista
techs = ['Python', 'Javascript', 'Java', 'c#', 'React', 'NodeJS', 'Django', 'R'] #lista

techs[3] = 'TensorFlow'
print(techs)

techs[2:4] = ['Numpy', 'Scrapy']
print(techs)

# Agregar elementos
techs.insert(2, 'Java')
print(techs)

techs.append('TensorFlow')
print(techs)

front_tech = ["Nextjs", "Astro", "Svelve", "Vue", "Vite"]
# front_tech = ("Nextjs", "Astro", "Svelve", "Vue", "Vite") se agrega cualquier tipo de lista con extend tambien puede ser un diccionario solo agrega la key

techs.extend(front_tech)
print(techs)

# QUITAR ELEMENTOS
techs.remove('Vue')
print(techs)

techs.pop()
print(techs)
techs.pop(0) #acirde al indice
print(techs)

del techs[7]
print(techs)

#vacial lista
# techs.clear()
# print(techs)

#recorrer listas
for tech in techs:
    print(tech)

for i in range(len(techs)):
    print(techs[i])

[print(tech) for tech in techs]

# Ejemplo
listaConY = []

for tech in techs:
    if "y" in tech:
        listaConY.append(tech)

print(listaConY)

listConY = [tech for tech in techs if "y" in tech]
print(listaConY)

#ordenar listas  
techs.sort() #de forma alfabetica
numeros = [1,2,5,3,5,9,7,5,3,4]
numeros.sort(reverse=True) #DESC
print(numeros)
techs.reverse() #de forma al revés a como estaba la lista


#copiar la lista
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
meses2 = ['Junio', 'Julio', 'Agosto', 'Septiembre']

copiaMeses = meses.copy()
copiaMeses2 = list(meses)
copiaMeses3 = meses[:]

# meses.append('prueba') #para probar que es otro espacio en memoria
# print(meses)
# print(copiaMeses)

#unir listas
print(meses + meses2)
meses.extend(meses2)
print(meses)


