# Declarar String.
cadena = "Hola Mundo"

# Escapar caraacteres.
cadenaConEscape = "Hola \"Carlos\" Mundo" # Muestra completo el mensaje.
cadenaConEscape = "Hola \nMundo" # Salto de línea.
cadenaConEscape = "Hola \tMundo" # Tabulación.
cadenaConEscape = "Hola \bMundo" # Elimina un espacio.

print(cadena)
print(cadenaConEscape)

# Convertir enteros a strings.
numero1 = 10
print("Hola número: ", numero1)
print(type(numero1))
print(type(str(numero1)))