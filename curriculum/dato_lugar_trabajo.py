# Lugar de trabajo
def lugar_trabajo():
    
    provincias = ("1.Buenos Aires", "2.Ciudad Autónoma de Buenos Aires", "3.Catamarca", "4.Chaco", "5.Chubut", "6.Córdoba", 
              "7.Corrientes", "8.Entre Ríos", "9.Formosa", "10.Jujuy", "11.La Pampa", "12.La Rioja", "13.Mendoza", "14.Misiones",
              "15.Neuquén", "16.Río Negro", "17.Salta", "18.San Juan", "19.San Luis", "20.Santa Cruz", "21.Santa Fe", 
              "22.Santiago del Estero", "23.Tierra del Fuego, Antártida e Islas del Atlántico Sur", "24.Tucumán")
    print(*provincias, sep='\n')
    
    
    while True:
        try:
            opcion = int(input("Elija la opcion de provincia: "))
            if opcion > 24:
                print("Su opcion elegida debe estar entre los valores inidicados")
            elif opcion <1:
                print("Su opcion elegida debe estar entre los valores inidicados")
            else:
                break
        
        except ValueError:
            print("Opción inválida, debe ser un número")
        
