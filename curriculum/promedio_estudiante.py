def prom_postulante():
    """ Permite cargar promedio general del estudiante """
    while True:
        try:
            promedio = float(input("Ingrese su promedio: "))
            print(promedio)
            if promedio > 10:
                print("El promedio debe ser menor o igual a 10")
    
            elif promedio <1:
                print("El promedio debe ser mayor o igual a 1")
        
            else:
                print("Correcto")
                break
            
        except ValueError:
            print("Debe ingresar un valor correcto")
               

    