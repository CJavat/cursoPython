# INTRODUCCIÓN AL MANEJO DE ERRORES EN PYTHON

""" while True: # PARA QUE EL BUCLE SIGA EN CASO DE QUE HAY UN ERROR
    try: # LO QUE DEBE DE EJECUTARSE.
        edad = int(input("INGRESA TU EDAD: "))
        print("TU EDAD ES: ", edad)
        break
    except: # MENSAJE DE ERROR SI ES QUE OCURRE.
        print("INGRESASTE UN VALOR ERRONEO. INTENTA DE NUEVO")
    finally: # SE EJECUTA SIEMPRE.
        print("LA EJECUCION HA FINALIZADO.") """

# EXCEPCIONES MULTIPLES
""" while True: # PARA QUE EL BUCLE SIGA EN CASO DE QUE HAY UN ERROR
    try: # LO QUE DEBE DE EJECUTARSE.
        num1 = int(input("INGRESA UN NUMERO: "))
        resultado = 100 / num1
        print("TU EDAD ES: ", num1)
        break
    except ZeroDivisionError: # MENSAJE DE ERROR CUANDO SE QUIERE DIVIDIR ENTRE CERO.
        print("NO SE PUEDE DIVIDIR ENTRE CERO")

while True: # PARA QUE EL BUCLE SIGA EN CASO DE QUE HAY UN ERROR
    try: # LO QUE DEBE DE EJECUTARSE.
        edad = int(input("INGRESA TU EDAD: "))
        print("TU EDAD ES: ", edad)
        break
    except ValueError: # MENSAJE DE ERROR SI HAY ALGUN VALOR ERRONEO
        print("INGRESASTE UN VALOR ERRONEO. INTENTA DE NUEVO") """

while True: # PARA QUE EL BUCLE SIGA EN CASO DE QUE HAY UN ERROR
    try: # LO QUE DEBE DE EJECUTARSE.
        edad = int(input("INGRESA TU EDAD: "))
        print("TU EDAD ES: ", edad)
        break
    except KeyboardInterrupt: # MENSAJE DE ERROR SI HAY ALGUN VALOR ERRONEO
        print("\n HAS CANCELADO LA EJECUCION")
        break