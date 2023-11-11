# Ventana para cargar imagen de perfil
# foto = input("Ingrese su foto")
from tkinter import *
ventana = Tk()
ventana.geometry("500x500+0+0")
ventana.config(bg="blue")
ventana.title("Imagen de perfil")
# creamos la imagen
imgageL=PhotoImage(file="")
fondo=PhotoImage(fie="")
lblFondo=Label(ventana,image=fondo).place(x=0, y=0)
lblImagen=Label(ventana,image=imgageL).place(x)
ventana.mainloop()
