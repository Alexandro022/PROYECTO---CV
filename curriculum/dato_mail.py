import re
def mail_postulante():
    while True:
        correo = input("Ingrese su correo electrónico: ")
        expresion_regular = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
        
        mail_long = len(correo)
        
        if not re.match(expresion_regular, correo):
            print(f"{correo} No es válido")
        
        elif  mail_long <7:
            print("Su mail no debe ser inferior a los 7 caracteres")
        
        elif mail_long >= 30:
            print("Su mail no debe ser mayor a los 20 caracteres")
            
        
        else:
            print(f"{correo} Es válida")

            break