def numero_dni():
    while True:
        numero = input("Ingrese su número de DNI: ")
        numero_long = len(numero)
        
        if  numero_long < 5:
            print("El DNI no debe ser menor a 5 dígitos")
        elif  numero_long > 10:
            print("El DNI no debe superar los 10 dígitos")
            
        else:
            print("DNI válido")
    
            try:
                numero = int(numero)
                return numero
            except ValueError:
                print("La entrada es incorrecta: escribe un numero entero")  
