palabra = input("Ingrese una frase: ")

contador = 0 ##estas son nuestras variables principales, al hacerlo con un ciclo while necesitamos un contador si o si (o alguna variable que itere)
numero = 1 ##este número representa la cantidad de letras que hay, inicia en 1 porque al momento de llegar a una letra nueva (o la inicial) se asume que esa letra ya la vimos (por eso 1 y no 0)
vacio = "" ##en este string vacio se va a guardar la frase nueva (onda c1h4r), si no estuviera presente la condicion completa probablemente se veria cortado (no he intentado, pero se me ocurre que aparezca algo parecido a ch4r, por ejemplos del programa y porque me parece bonito que el ejemplo ronde a tu nombre)

while contador < len(palabra): #es menor < (y no menor o igual <=) ya que el len empieza a contar desde el 1 (12345) y la palabra se cuenta desde el 0 (01234) donde cada numero representa una letra (en palabra = charlotte por ejemplo si buscas palabra[0:5] se imprimirá char, esto es porque el 5 se omite y imprime del 0 al 4)
    if contador < len(palabra) - 1 and palabra[contador] == palabra[contador + 1]: ##explicación por partes:
      ## contador < len(palabra)-1 porque ahora se ve el valor de la letra que sigue, no puedes evaluar en charlotte qué letra sigue después de la e porque no existe ninguna letra, sin embargo, puedes evaluar que la letra t es distinta a la letra e que sigue, por ende, t tiene un valor de 2 y la e sólo un valor de 1
      ## and porque son condiciones que se deben de cumplir si o si, nos interesa que las 2 se cumplan para que no hayan errores en el código, ya que si evaluas la letra que sigue de la e en el ejemplo, devolverá un error de traceback (que no puede seguir el código ya que no existe el dato que estás pidiendo, por ende, entra en conflicto)
      ## palabra[contador] == palabra[contador+1] va a revisar constantemente si la letra que estás viendo de tu palabra es la misma que la letra siguiente, si tienen el mismo valor (esto se ve por tabla ascii, ninguna letra tiene un valor igual a la letra que seleccionaste)
        numero += 1 ##se aumenta el numero en 1 ya que se cumplió que la letra que sigue es la misma
    else:
        vacio += palabra[contador] + str(numero) ## en caso de que el if no se cumpla, meterá en el formato c3 (letra-numero) al string vacio, es una suma ya que al concatenar strings estos no generan espacios a menos que concatenes un espacio
        numero = 1 ##el número se reinicia a 1 para empezar con otra letra
    contador += 1 ## el contador (fuera de ciclos, para que se ejecute cada vez que se cumple algo) aumenta, esto hará que se repita el while con la letra siguiente y a la vez que la condición del while en algun momento retorne false, deteniendo el código

print(vacio) ##se imprime la frase
