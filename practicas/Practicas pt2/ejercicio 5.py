"""
    Construir un pequeño programa que convierta números binarios en enteros.
    NUMEROS BINARIOS:
    | 128 | - | 64 | - | 32 | - | 16 | - | 8 | - | 4 | - | 2 | - | 1 |
"""

valorBinario = [128, 64, 32, 16, 8, 4, 2, 1]
numeroBinario = "11111111"

resultado = 0
contador = 0

while(contador <= 7):
    if numeroBinario[contador] == "1":
        resultado += valorBinario[contador]
    contador += 1

print("El numero decimal es: {}".format(resultado))