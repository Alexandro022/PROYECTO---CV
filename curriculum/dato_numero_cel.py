def numero_cel():
    while True:
        numero = input("Ingrese un número de referencia en formato (1123456789): ")
        numero_long = len(numero)
        
        if  numero_long < 10:
            print("Su celular debe contar con 10 números")
        elif  numero_long > 10:
            print("Su celular debe contar con 10 números")
            
        else:
            print("Número válido")
    
            try:
                numero = int(numero)
                return numero
            except ValueError:
                print("La entrada es incorrecta: escribe un numero entero")