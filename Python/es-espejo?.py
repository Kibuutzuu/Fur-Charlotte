palabra = str(input("Ingrese una palabra: "))

letra = -1 #variables de inicio, al ser -1 se asume que trabajaremos con la frase del final hacia el comienzo
total = len(palabra)+1 ##len +1 ya que al trabajar con la condición != en este caso se omite el ultimo caracter, por ende, el código va a terminar 1 numero antes y ese es el numero que estamos agregando para que se detenga en el momento preciso
palabranueva = "" ## string vacio para comparar la palabra con su reverso
while abs(letra) != total: ## abs es el numero absoluto de algo, sin signo, por ende el -1 se va a ver como 1 en la comparación (letra es distinto que total)
    palabranueva += palabra[letra] ##va a agregar la ultima letra al string vacio, luego la penultima y asi hasta completar la frase
    letra = letra - 1 ##se resta 1 para que vaya del final al comienzo
if palabra == palabranueva: #esta condicion pregunta con "==" (operador lógico) si la palabra original es la misma que la que esta en reverso ( palabra = palabra nueva, el "=" es de asignación, acuerdate siempre la diferencia)
    print("Es una palabra espejo")
else: print("No es una palabra espejo") ## si no es igual, devuelve un mensaje respecto a ello

## tip: ya que se vió la diferencia entre "==" y "=", la mejor manera de diferenciar una y otra es qué devuelven, con la palabra oso puedes decir que oso = oso, ya que esto significa que son iguales, pero si pones oso == oso la respuesta es True
## en el primer caso estás asignando algo, en el segundo, estas preguntando su valor booleano
## el tip? preguntate siempre si quieres una respuesta de verdadero/falso (==) o solamente quieres que oso signifique algo (=)
