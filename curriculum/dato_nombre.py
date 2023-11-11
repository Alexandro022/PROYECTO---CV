def nombre_postulante():
    """ Función para validar nombre del postulante"""
    while True:
        nombre = input("Ingrese su nombre: ")
        nombre.isalpha()
        nombre_long = len(nombre)
        
        if nombre_long > 15:
            print(f"El nombre no debe superar los 15 carácteres. Tiene {nombre_long}.")
        
        elif nombre_long < 2:
            print(f"El nombre debe tener más de un carácter. Tiene {nombre_long}.")
        elif nombre.isalpha() is True:
            print("Nombre correcto")
            break
        
        else:
            print("Nombre incorrecto. Vuelva a ingresar")
    