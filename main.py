# Archivo principal del programa para cargar un currúclum vitae
'''print()
print("Datos del Postulante")
print()
import Datos_Postulante'''

print()
print("Experiencia Laboral")
print()
import Experiencia_Laboral

nueva_exp = input("¿Nueva experiencia laboral?: ")
if nueva_exp == "si":
    import Experiencia_Laboral
else:
    print("continúe")

print()
print("Estudios")
print()
import Estudios 