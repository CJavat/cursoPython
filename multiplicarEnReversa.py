numero = 0
resultado = 1

numero = int(input("Ingresa un número: "));

for i in range(1, numero+1):
  resultado += i
  print(resultado)
  
print("El resultado es: ", resultado)