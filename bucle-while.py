## BUCLES : estrucura que se repite mientras no cumpla cierta condición
### BUCLE WHILE:
print("#######################################################")

a = 1

while a<= 10:
    print(f"{a} MENOR A 10")
    a+=1 

print("#######################################################")

#break: terminar de un bucle
b = 1

while b<= 10:
    print(f"{b} MENOR A 10")
    if b == 5:
        print(f"{b} TERMINA")
        break
    b+=1 

print("#######################################################")
#break: terminar de un bucle
c = 1
while c<= 10:
    c+=1 # 
    print(f"{c} MENOR A 10")
    if c == 5:
        print(f"SALTO EL {c}")
        continue #desde aqui para abajo saltea dodo es por eso que si la suma +1 esta debajo se genera el bucle infinito
    # c+=1 # bucle infinito

print("#######################################################")
c = 1
while c <= 10:
    print(f"cumple la condicion {c}?")
    c+=1
else:
    print(f"{c} ya no se cumple la condicion?")


print("#######################################################")
#EJEMPLO PRACTICO
# strip saca los espacios en blanco
while True:
    respuesta = input("¿Desea continuar ? (s/n)").strip().lower()
    if respuesta == 'n':
        break