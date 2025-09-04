palabra, contador = str(input("Ingrese una frase: ")), 0 ##creo 2 variables, una que pregunta una palabra y otra que se inicia en 0 porque es un contador
for i in palabra: ##el ciclo for recorrerá letra por letra esa palabra, ya que al poner str() al pedir una palabra todo se considerará un string (incluso numeros o caracteres especiales)
    if i in "aeiouAEIOU": contador += 1 ## si i se encuentra entre las vocales (escritas en minuscula y mayuscula porque no necesariamente va a ser solo en minuscula, con i.upper() puedes preguntar solo si existe entre las vocales en mayuscula porque será una forzozamente
      ##si encuentra una vocal, aumentará el contador de vocales
print(f"{palabra} tiene {contador} vocales") ## imprime por medio del format (la f) la plantilla de que la palabra tiene n numero de vocales

##este código está reducido, si quieres que lo haga a lo largo por cualquier confusión o por comodidad, dimelo
