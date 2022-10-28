# INTRODUCCIÓN A WHILE.

# i = 0
# while i < 2:
#     i += 1
#     print("Estoy iterando, voy por el salto: ", i)

# INTRODUCCIÓN A FOR.

# lista = ['Uno', 'Dos', 'Tres']
# tupla = (1, 2, 3, 4, 5)

# for i in lista:
#     print(i)

# for j in tupla:
#     print(j)

# FUNCIÓN RANGE
# range(inicio, final, suma)
# for i in range(0, 10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# CONTINUE Y BREAK
for i in range(0, 11):
    if i == 4:
        continue

    print(i)

    if i == 5:
        break