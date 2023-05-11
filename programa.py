#Se importa la libreria tkinter con todas sus funciones
from tkinter import *

#---------------------------------
#Funciones de la app
#---------------------------------



#Variables
BASE=460
ALTURA=220





#---------------------------------
#ventana principal
#---------------------------------

#se declara una variable llamada "ventana_principal" que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk( )

#Titulo de la ventana
ventana_principal.title("Sistema UIS Socorro")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="black")

#frame de graficacion
Frame_graficacion = Frame(ventana_principal)
Frame_graficacion.config(bg="white", width=480, height=240)
Frame_graficacion.place(x=10 , y=10)

#Creacion canvas
c = Canvas(Frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="yellow")
c.place(x=10, y=10)

#Lineas
linea1 = c.create_line(10,10, BASE-10,10, fill="red")
linea2 = c.create_line(BASE-10, 10,BASE-10, ALTURA-10, fill="red")
linea3 = c.create_line(BASE-10, ALTURA-10,10, ALTURA-10, fill="red")
linea4 = c.create_line(10, ALTURA-10, 10,10, fill="red")

#Lineas diagonal
linea5 = c.create_line(10,210, BASE-10,10, fill="red")
linea6 = c.create_line(450, ALTURA-10, 10,10, fill="red")

#CRUZ







#Desplegar ventana
ventana_principal.mainloop()