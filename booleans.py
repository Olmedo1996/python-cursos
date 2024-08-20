### Tipo de dato que toma dos valores Verdadero o Falso (True o False)
a = True
b = False

string  = bool("string") #True
num = bool(2022) #True
lista = bool(['Naranja', 'manzana']) #True
dict = bool({"nombre":"string"}) #True


#False
string2 = bool("") #False
num2 = bool(0)
lista2 = bool([])
dict2 = bool({})


## verdaderamente vacío
none = bool(None) #False