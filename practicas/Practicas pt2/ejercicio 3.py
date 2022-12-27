"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, 
    y devuelva las palabras que tengan mas de n caracteres.
"""
def filtrar_palabras(lista, n):
    palabrasFiltradas = []
    for i in lista:
        if len(i) > n:
            palabrasFiltradas.append(i)
    return palabrasFiltradas

lista = ["Palabra 1", "Palabra2", "Pal3ssss", "Palabra2", "Pal3ssss"]

numero = 4
resultado = filtrar_palabras(lista, numero)

palabras = ""
longitudResultado = len(resultado)
contadorPalabras = 0

for j in resultado:
    if contadorPalabras < longitudResultado-1:
        palabras += j
        palabras += ", "
    else:
        palabras += j
        palabras += "."
        
    contadorPalabras += 1


print("Las palabras con mas caracteres que {} son:\n {}".format(numero, palabras))