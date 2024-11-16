#PEDIRLE AL USUARIO INGRESE CUALQUIER TEXTO
#INGRESE TRES LETRAS DE SU ELECCION
#CUANTAS VECES APARECE CADA UNA DE LAS LETRAS QUE ELIGIO DENTRO DEL TEXTO
#CUANTAS PALABRAS HAY EN TODO EL TEXTO
#PRIMERA Y ULTIPMA LETRA DEL TEXTO
#PALABRAS A LA INVERSA
#VERIFICAR SI SE ENCUENTRA LA PALABRA PYTHON EN EL TEXTO(BOOL)

texto_base = input("ingresa el texto que quieras analizar: ")
letras = []
texto_base = texto_base.lower()
letras.append(input("ingresa la primer letra: ").lower())
letras.append(input("ingresa la segunda letra: ").lower())
letras.append(input("ingresa la trecera letra: ").lower())

print("cantidad de letras")
cantidad_letras1 = texto_base.count(letras[0])
cantidad_letras2 = texto_base.count(letras[1])
cantidad_letras3 = texto_base.count(letras[2])

print(f"hemos encontrado una letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"hemos encontrado una letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"hemos encontrado una letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("cantidad de palabras")
palabras = texto_base.split()
print(f"hemos encontrado {len(palabras)} palabras en tu texto ")

print("letras de inicio y de fin")
letra_inicio = texto_base[0]
letra_final = texto_base[-1]
print(f"la letra inicial '{letra_inicio}' y la letra final es '{letra_final}' ")
print("texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"si ordenamos las cosas no deberia de haber problema:  '{texto_invertido}'")

buscar_python = 'python' in texto_base
dic {True: "si",False:"no"}
print(f"la palabra ' python' "{dic[buscar_pytho]})