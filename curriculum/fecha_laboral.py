def fecha_lab():
    """ Función para determinar fechas de incio y fin de trabajo; y años trabajados """
    import datetime

    # ¿Trabaja actualmente en la empresa?
    
    while True:
        valor1 = ("si")
        valor2 = ("no")
        mensaje = input("¿Sigue trabajando aquí?si/no: ")
        mensaje_lower = mensaje.lower()


        if mensaje_lower in valor2:
            while True:
                try:
                    desde = input("Ingresa la fecha de inicio en formato YYYY-MM-DD: ")
                    desde = datetime.datetime.strptime(desde, '%Y-%m-%d')
                    #desde = int(desde)
                    hasta = input("Ingresa la fecha de fin en formato YYYY-MM-DD: ")
                    hasta = datetime.datetime.strptime(hasta, '%Y-%m-%d')
                    años_trabajados = hasta.year - desde.year
                    print("Años trabajados:",años_trabajados)
                    break
            #return desde
                except ValueError:
                    print("La entrada es incorrecta: escribe un numero entero")
            break

        elif mensaje_lower in valor1:
            while True:
                try:
                    desde2 = input("Ingresa la fecha de inicio en formato YYYY-MM-DD: ")
                    desde2 = datetime.datetime.strptime(desde2, '%Y-%m-%d')
        
                    actualidad = datetime.datetime.now()   
                    años_trabajados = datetime.datetime.now().year - desde2.year
                    print("Años trabajados:",años_trabajados)
                    break
                except ValueError:
                    print("La entrada es incorrecta: escribe un numero entero")
            break
        
        else:
            print("No valido. Debe ingresar SI o NO")
        
