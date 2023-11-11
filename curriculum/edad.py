
#Función que arroja la edad del postulante

def edad_postulante():
    import datetime
    while True:
        try:
            fecha = input("Ingresa la fecha en formato YYYY-MM-DD: ")
            fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
            edad = datetime.datetime.now().year - fecha.year
            print(edad,"años")
            break
        except ValueError:
            print("Fecha inválida")
