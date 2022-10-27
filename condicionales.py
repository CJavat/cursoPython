edad = int(input("Dame tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# ELIF

if edad >= 50:
    print("Eres viejo.")
elif edad >= 25 and edad <= 49:
    print("Eres adulto.")
else:
    print("Eres niño o adolescente.")