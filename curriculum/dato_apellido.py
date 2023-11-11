def apellido_postulante():
    """ Función para validar apellido del postulante"""
    while True:
        apellido = input("Ingrese su apellido: ")
        apellido.isalpha()
        apellido_long = len(apellido)
        
        if apellido_long > 15:
            print(f"El apellido no debe superar los 15 carácteres. Tiene {apellido_long}.")
        
        elif apellido_long < 2:
            print(f"El apellido debe tener más de un carácter. Tiene {apellido_long}.")
        elif apellido.isalpha() is True:
            print("Apellido correcto")
            break
        
        else:
            print("Apellido incorrecto. Vuelva a ingresar")
    