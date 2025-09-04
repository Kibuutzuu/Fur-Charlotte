contraseña = str(input("Ingrese una contraseña: "))
largo = len(contraseña) ##buscamos el largo de la contraseña por el primer criterio, debe tener 8 caracteres minimo
mayus = 0 ##contadores de mayusculas y numeros por el segundo y tercer criterio, deben tener al menos 1
numeros = 0
if largo >= 8: ##preguntamos enseguida si tiene al menos 8 caracteres, ya que, si ejecuta todo el código al comienzo sólo estás gastando memoria de forma innecesaria y lo más probable es que el código demore un poco más en cargar, cuando hagas proyectos grandes te darás cuenta lo importante que es que te enseñe esto
    for i in contraseña: ## si se cumple el criterio, empieza a ver letra por letra la contraseña
        if i.isupper(): ## analiza si tiene mayusculas y las suma al contador cuando encuentra, es un operador logico, devuelve solo true o false y podias ponerlo como if i in "" y en las comillas escribir todas las mayusculas
            mayus += 1
        if i in "123456789": ##es lo mismo que con las mayusculas, se pone if y no elif porque no estás considerando que se cumpla 1 solamente, quieres que las 2 se cumplan entonces revisas constantemente los 2 criterios, esto podias escribirlo como if i.isdigit()
            numeros += 1
    if mayus >= 1: ##ahora pregunta por el segundo criterio, si es verdad analiza el tercer criterio
        if numeros >= 1: ## analiza el tercer criterio, si es verdad te dice que tu contraseña es válida
            print("Contraseña válida")
        else: print("Le falta al menos un número") ## si el tercer criterio es falso, te da un mensaje para que arregles eso que está mal
    else: print("Le falta al menos una mayuscula") ## si el segundo criterio es falso, te da un mensaje para arreglar lo que está mal sin avanzar al tercer criterio, ahorras memoria
else: print("La contraseña debe ser de al menos 8 caracteres") ## si directamente el primer criterio es falso, te explica que debe ser de minimo 8 caracteres y termina el programa, es más rápido en proyectos grandes


##tip, si en algún momento no sabes detener un código cuando algo no está siendo verdadero, yo personalmente encierro todo el código en un if que fuerce que corra sólo cuando se cumplen todos los criterios
## tip 2, hay un dicho en programación que dice que si tienes que repetirlo dentro del código, significa que puedes optimizarlo, preguntate si estás repitiendo algo muchas veces y ve si puedes hacerlo condicion o automatizacion
## tip 3, si tienes tiempo para optimizar tu código mientras lo trabajas y te sientes capaz de hacerlo, hazlo sin faltas, arreglar código es mucho más fácil cuando lo optimizas ya que puedes irte directamente a la sección afectada en vez de revisar código a ver qué está ocasionando el problema

##Animos!! programar es divertido cuando sientes compañia, y siempre puedes preguntarme o decirme que nos metamos a discord para que te haga esa compañia
## a diferencia de los otros, tu no estás sola en programación, matematicas, en nada mientras exista yo, animos!
