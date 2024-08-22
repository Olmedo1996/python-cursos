## BUCLES : estrucura que se repite mientras no cumpla cierta condición
### BUCLE FOR:

techs = ['Python', 'Javascript', 'Java', 'c#', 'React', 'NodeJS', 'Django', 'R'] #lista
x = 1
texto = "No te olvides de que esto es un texto"

for tech in techs:
    if tech == 'React':
        break #continue pass
    print(f"{x}. {tech}")
    x += 1


############
x=1
print("#############################################")
for tech in techs:
    if tech == 'React':
        continue #continue pass
    print(f"{x}. {tech}")
    x += 1

############
x=1
print("#############################################")
# es raro 
for tech in techs:
    print(f"{x}. {tech}")
    if tech == 'React':
        continue #continue pass
    x += 1


#############
#iteraer textos
print("#############################################")
for letra in texto:
    print(letra)

#############
# iterar rangos
print("#############################################")
for i in range(5): # del 0 al 4
    print(i)

print("#############################################")
for i in range(2, 7): # del 2 al 6 (incluye el 2)
    print(i)

print("#############################################")
for i in range(1, 11, 2): #en pares o de a x cantidad dependiendo del tercer valor del range
    print(i) #impares



print("#############################################")
letras = ['a', 'b', 'c']
numeros = [1,2,3]

for letra in letras:
    for n in numeros:
        print(f"{letra} : {n}")