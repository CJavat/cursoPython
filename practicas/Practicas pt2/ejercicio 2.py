"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""
def mas_larga(lista):
    longitudPalabra = 0
    mayor = ""
    for i in lista:
        longitudPalabra = len(i)
        if longitudPalabra > len(mayor):
            mayor = i
        elif longitudPalabra < len(mayor):
            mayor = mayor
    return mayor

listaDePalabras = []

seguirIntroduciendo = True
while seguirIntroduciendo == True:
    palabra = input("Escribe una palabra: ")
    listaDePalabras.append(palabra)
    
    respuesta = input("Quieres seguir introduciendo datos?, responde: si o no.\n")
    if respuesta.lower() == "si":
        seguirIntroduciendo = True
    elif respuesta.lower() == "no":
        seguirIntroduciendo = False

palabraMasLarga = mas_larga(listaDePalabras)
print("La palabra más larga es: {}".format(palabraMasLarga))