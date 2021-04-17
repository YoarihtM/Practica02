import relojes 
from tkinter import *

class GUI:
    def __init__(self, nPractica):
        self.tamVentana = '750x450'
        self.titulo = 'Practica ' + str(nPractica)
        self.cambiarTamaño = False

    def cargarVentana(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.titulo)
        ventana.geometry(self.tamVentana)
        
        if self.cambiarTamaño:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        texto = Label(ventana, text='')
        texto.pack()

        texto1 = Label(ventana, text='')
        texto1.pack()

        texto2 = Label(ventana, text='')
        texto2.pack()

        texto3 = Label(ventana, text='')
        texto3.pack()

    def iniciarVentana(self):
        self.ventana.mainloop()

v1 = GUI(2)

v1.cargarVentana()
v1.iniciarVentana()