# Programa principal

print("Ingrese su Currículum Viate")

# importa datos del postulante
from dato_nombre import nombre_postulante
from dato_apellido import apellido_postulante
from dato_numero_dni import numero_dni
from edad import edad_postulante
from dato_numero_cel import numero_cel
from dato_mail import mail_postulante

# importa datos de experiencia laboral

from dato_compañia_trabajo import dato_compania
from dato_lugar_trabajo import lugar_trabajo
from fecha_laboral import fecha_lab
from datos_puestos_laborales import puestos_laborales
from dato_desempeño_laboral import desempeño_laboral
from dato_numero_cel import numero_cel

# importa datos de estudios

from dato_institucion import dato_inst_educ
from dato_carrera import dato_carrera
from fecha_de_estudio import fecha_estudio
from promedio_estudiante import prom_postulante


def menu():

    print("1. DATOS")
    print("2. EXPERIENICIA")
    print("3. ESTUDIOS")
    print("0. Salir")

def main():
    while True:
        while True:
            menu()
            try:
                opcion = int(input("Escriba la opción a cargar: "))
                break
            except TypeError as e:
                print("ERROR: Ha digitado un valor inválido")
            except ValueError as e:
                print("ERROR: Ha digitado un valor inválido")

        if opcion == 1:
            print("Datos personales")
            resultado = nombre_postulante(), apellido_postulante(),numero_dni(),edad_postulante(),numero_cel(),mail_postulante()
        
        elif opcion == 2:
            print("Experiencia laboral")
            resultado = dato_compania(), lugar_trabajo(), fecha_lab(), puestos_laborales(),desempeño_laboral(),numero_cel()
            
        elif opcion == 3:
            print("Estudios")
            resultado = dato_inst_educ(), dato_carrera(), fecha_estudio(), prom_postulante()
        elif opcion == 0:
            print("Gracias")
            print("El programa ha terminado") 
            break
        else:
            print("Debe ser 1, 2, 3 o 0 para salir")
        
        #Esta opcion no logré que funcionara
        '''mensaje_opcion = int(input("desea continuar: "))
        while True:
            
            if mensaje_opcion == 2:
                print("Muchas gracias")
                break
            
            elif mensaje_opcion <1:
                print("invalido")
            elif mensaje_opcion >2:
                print("invalido")
            elif mensaje_opcion == 1:
                menu()
            else:
                print("invlido")'''

        
print()


if __name__ == '__main__':
    main()
        
            
