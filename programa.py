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
"""linea1 = c.create_line(10,10, BASE-10,10, fill="red", width=5)
linea2 = c.create_line(BASE-10, 10,BASE-10, ALTURA-10, fill="red", width=5)
linea3 = c.create_line(BASE-10, ALTURA-10,10, ALTURA-10, fill="red", width=5)
linea4 = c.create_line(10, ALTURA-10, 10,10, fill="red", width=5)

#Lineas diagonal
linea5 = c.create_line(10,210, BASE-10,10, fill="red")
linea6 = c.create_line(450, ALTURA-10, 10,10, fill="red")

#CRUZ

linea7 = c.create_line(BASE - 120,100, BASE-180 , ALTURA -120 , fill="green")
linea8 = c.create_line(BASE - 120,150, BASE-120 , ALTURA -120 , fill="green")


#Texto
texto1= c.create_text(BASE/2, ALTURA/2, text="UIS SOCORRO", anchor="center", font=("Arial" , "20", "bold"), fill="green", activefill="white")

#cuadrados y rectangulos
rect1= c.create_rectangle(20, 20, 120, 120, fill="blue", outline="red", width="3")

#Poligonos
poligono1=c.create_polygon(0, 0, BASE/2, ALTURA/2, BASE, 0, fill="red")
poligono2=c.create_polygon(0, ALTURA, BASE/2, ALTURA/2, BASE,ALTURA, fill="green")
poligono3=c.create_polygon(0,0,BASE/2,ALTURA/2,0, ALTURA, fill="blue", outline="black")"""


#trabajo
poligono1 = c.create_polygon((BASE/2)/2,0,BASE/2,(ALTURA/2)/2,(BASE/2)/2,ALTURA/2,0,(ALTURA/2)/2, fill="blue", outline="green")
poligono1 = c.create_polygon((BASE/2)*1.5,0,BASE,(ALTURA/2)/2,(BASE/2)*1.5,ALTURA/2,BASE/2,(ALTURA/2)/2, fill="blue", outline="green")
poligono1 = c.create_polygon((BASE/2)/2,ALTURA/2,BASE/2,(ALTURA/2)*1.5,(BASE/2)/2,ALTURA,0,(ALTURA/2)*1.5, fill="blue", outline="green")
poligono1 = c.create_polygon((BASE/2)*1.5,ALTURA/2,BASE,(ALTURA/2)*1.5,(BASE/2)*1.5,ALTURA,BASE/2,(ALTURA/2)*1.5, fill="blue", outline="green")

#elipse
"""elipse1=c.create_oval(BASE/2, ALTURA/2, BASE,ALTURA, fill="orange")"""

#circulo
circulo1=c.create_oval(BASE/2-30, ALTURA/2-30, BASE/2+30, ALTURA/2+30, fill="red")
circulo2=c.create_oval(BASE/10, ALTURA/10, BASE/3-30, ALTURA/2+10, fill="red")
circulo3=c.create_oval(BASE/2, ALTURA/2, BASE,ALTURA, fill="orange")

#Arcos
arc1=c.create_arc(BASE/2-30, ALTURA/2-30, BASE/2+30, ALTURA/2+30, start=45, extent=280, fill="black")
"""arc2=c.create_arc(BASE/90, ALTURA/90, BASE/3-30, ALTURA/2+10, start=45, extent=280, fill="black")"""





#Desplegar ventana
ventana_principal.mainloop()