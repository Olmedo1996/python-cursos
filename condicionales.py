### CONDICIONALES (if, elif, else)
# Es la estructura que nos permite tomar un flujo u otro según una condicion
a = 5
b = 9
c =  7
if a>b:
    print(f"{a} es mayor que {c}")
elif c>b:
    print(f"{c} es mayor que {b}")
else:
    print(f"{a} es menor que {b} y {c} es menor que {b}")



## ej : edad
edad = 20

if edad >= 18 and edad <= 60: 
    print("Puedes entar")
else:
    if edad <18:
        print("no puedes entrar")
    else:
        print("tampoco")



### shorthands

a = 5
b = 2

if a > b : print(f"{a} es mayor que {b}")

#otro
print(f"{a} es menor que {b}") if b > a else  print(f"{a} es mayor que {b}") #shorthand de if + else