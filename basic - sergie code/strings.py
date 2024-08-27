#  str (string) texto o cadena de caracteres

texto = "ESTE ES UN CURSO DE PYTHON"

comillaSimple = 'Este es un texto'
comillaDobles = "Este es un texto"
comillaTriplesDobles =  """ESTE ES UN TEXTO"""
comillaTriplesSimples =  '''ESTE ES UN TEXTO'''

#### TYPE
print(comillaSimple)
print(type(comillaSimple))

####ARAYS DE CARACTERES
caracter = texto[1] #caracter por indice
print(caracter)

### Len (Length)
amplitud = len(texto)
print(amplitud)

# In: para saber si esta en el texto

print("PYTHON" in texto) #True
print("PyThoN".lower() in texto.lower()) #True

# Not in: con la palabra reservada no podemos negar y pedir un resultado negativo
print("Java" not in texto) #True porque java no esta en el texto


#Slice: cortar una parte del texto
print(texto[11:26]) #SE imprime del inidce 11 a 26
print(texto[:11]) #ESTE ES UN
print(texto[11:]) #CURSO DE PYTHON
print(texto[-6:]) #PYTHON


# Modificacion de texto (mayusculas, minusculas capitalize)
texto_con_espacios = "             ESPACIO   "
mayusculas = texto.upper()
minusculas = texto.lower()
capitalize = texto.capitalize()

print(mayusculas)
print(minusculas)
print(capitalize)
print(texto_con_espacios.strip())
print(texto_con_espacios)

reemplazo = texto_con_espacios.replace("ESPACIO", "mundo") #reemplaza ESPACIO por 
print(reemplazo)

texto_con_comas = "HOLA, MUNDO, QUE, QUE TAL"
separar_por_comas = texto_con_comas.split(",")
print(separar_por_comas) #lista

texto_a_modificar = "este es Un Texto a MODIFICAR"
estaComenzando = texto_a_modificar.startswith("este")
estaFinalizando = texto_a_modificar.endswith("MODIFICAR")
titulo = texto_a_modificar.title()
contador = texto_a_modificar.count("e")
encontrar = texto_a_modificar.find("MODIFICAR") #indice donde comienza la palabra encontrada
print(titulo)
print(contador)
print(encontrar)

#################################
# F-Strings (Templat strings)
num = 5
txt = "ricardo"
# num_float

print(f"la edad de {txt} es {num}, decimal {num:.2f}")

resultado= f"El resultado de 69 X 75 es {69*75}"
print(resultado)


# Escapes \ backsslash - barra invertida
escape = "Mi pais favorito es \"Lituania\" por que si"
print(escape)