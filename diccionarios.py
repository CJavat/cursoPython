# INTRODUCCIÓN A LOS DICCIONARIOS.

diccionario = {
        'user' : 'javato', 
        'pass' : 123456
        }

print(type(diccionario))
print(diccionario)

# TRABAJAR CON DICCIONARIOS.

print(diccionario.keys()) # MUESTRA LAS LLAVES.
print(diccionario.values()) # MUESTRA EL VALOR.
print(diccionario["user"]) # MUESTRA EL VALOR QUE TIENE ESA LLAVE.

diccionario["name"] = "Daniel" # FORMA PARA AGREGAR UN NUEVO ELEMENTO.
diccionario["user"] = "CJAVAT" # FORMA DE MODIFICAR UN ELEMENTO.

print(diccionario)

# MÉTODOS DE LOS DICCIONARIOS.
diccionario2 = {"lastname2" : "Mercado"}

diccionario.pop("user") # ELIMINA EL ELEMENTO QUE SE LE PUSO EN LA CLAVE.
diccionario.clear() # BORRA TODOS LOS DATOS DEL DICCIONARIO.
diccionario.get("pass") # PARA OBTENER EL DATO QUE LE INDICAMOS.
diccionario.setdefault("lastname", "Plascencia") # AGREGAR UN ELEMENTO.
diccionario.update(diccionario2) # ACTUALIZAR UN DICCIONARIO ENTERO (LOS JUNTA).
diccionario.copy() # GENERA UNA COPYA DEL DICCIONARIO.
print(diccionario)