#!/usr/bin/python3
# Script creado por Fernando SFEIR
# Algunos aspectos a mejorar: control de excepciones
# Modo de uso: python3 Cesar.py C|D 7 'Este es el texto a codificar'
# Donde Cesar.py es el nombre de este script
# La letra C para codificar ó la D para decodificar
# Un número (7 en el ejemplo) para el desplazamiento
# El texto entre comillas simples

# Importo las librerías que voy a utilizar, la "sys" me permite leer los parámetros por consola
import sys

# Defino mi alfabeto... en algún momento había agregado la "ñ" pero en los ejemplos no la estaban usando
# De esta manera, sé que uso 26 caracteres (con la eñe eran 27 y fallaba al traducir los ejemplos de la consigna) 
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26

# Verifico que vengan los 3 argumentos requeridos, el argumento 0 es el propio script
# para ello utilizo la funcion "len" que me proporciona la cantidad de argumentos "sys.argv" proporcionados
if (len(sys.argv) == 4):
  # Paso el texto, que viene en "sys.argv[3]" a mayúsculas, con la funcion "upper" para facilitar la encriptación
  texto = sys.argv[3].upper()
  # Asigno a la variable desplazamiento el valor que vino por la línea de comando en sys.argv[2], previo convertirlo a un número entero con la funcion "int"
  desplazamiento = int(sys.argv[2])
  # Inicializo la variable texto2 en vacío, allí almacenaré el texto luego de procesarlo
  texto2 = ""
  # Verifico, si voy a cifrar "C" o descifrar "D" la cadena proporcionada, de acuerdo al parámetro provisto (sys.argv[1])
  if ((sys.argv[1]) == "C"):
    # Solo un mensajito para saber qué estoy haciendo....
    print("Cifrando...")
    # Recorro el texto ingresado letra por letra
    for letra in texto:
      # Verifico si la letra está en el alfabeto definido anteriormente, de esta manera "escapo" (no "cifro") los números ni los espacios
      if letra in alfabeto:
        # Asigo a texto2 lo que tenía más la letra luego de aplicarle el desplazamiento
        # Para el cálculo del desplazamiento, utilizo la funcion % (módulo, o resto de la división entera), así evito que al sumar
        # me quede un número superior a 27, que es la longitud de mi alfabeto
        # alfabeto.index(letra) me dá la posición de la letra en mi alfabeto
        # len(alfabeto) calcula la cantidad de caracteres en mi alfabeto, en este caso, 27
        texto2 += alfabeto[(alfabeto.index(letra)+desplazamiento)%(len(alfabeto))]
        # Si la letra no está en el alfabeto (es un espacio en blanco o un número), directamente la agrego a mi variable texto2
      else:
        texto2 += letra
    # Muestro el texto cifrado    
    print("El texto cifrado es:", texto2)
  # Si la opción pasada por parámetro no es "C" de cifrar, pregunto si es "D" de descifrar, de acuerdo al parámetro provisto (sys.argv[1])
  elif ((sys.argv[1]) == "D"):
    # Solo un mensajito para saber qué estoy haciendo....
    print("Descifrando...")
    # Recorro el texto ingresado letra por letra
    for letra in texto:
    # Verifico si la letra está en el alfabeto definido anteriormente, de esta manera "escapo" (no "descifro") los números ni los espacios
      if letra in alfabeto:
        # Asigo a texto2 lo que tenía más la letra luego de aplicarle el desplazamiento
        # Para el cálculo del desplazamiento, utilizo la funcion % (módulo, o resto de la división entera), así evito que al restar
        # me quede un número inferior a 1
        # alfabeto.index(letra) me dá la posición de la letra en mi alfabeto
        # len(alfabeto) calcula la cantidad de caracteres en mi alfabeto, en este caso, 27
        texto2 += alfabeto[(alfabeto.index(letra)-desplazamiento)%(len(alfabeto))]
      else:
        # Si la letra no está en el alfabeto (es un espacio en blanco o un número), directamente la agrego a mi variable texto2
        texto2 += letra
    # Muestro el texto descifrado    
    print("El texto descifrado es:", texto2)
# Si la cantidad de argumentos no es 4, muestro el mensaje acerca del uso del script
else:
  print("Debe introducir C o D para codificar/decodificar, el desplazamiento (numero entero) y el texto a cifrar entre comillas simples\n")
  # Muestro la forma de uso, "calculando" el nombre del script con "sys.argv[0]" y lo convierto a texto con "str"
  print("Por ejemplo: \"python3", str(sys.argv[0]), "C 7 'Este es el texto'\"")
