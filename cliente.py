import relojes, threading
from tkinter import *

# class GUI:
#     def __init__(self, nPractica):
#         self.tamVentana = '750x450'
#         self.titulo = 'Practica ' + str(nPractica)
#         self.cambiarTamaño = False

#     def cargarVentana(self):
#         ventana = Tk()
#         self.ventana = ventana
#         ventana.title(self.titulo)
#         ventana.geometry(self.tamVentana)
        
#         if self.cambiarTamaño:
#             ventana.resizable(1,1)
#         else:
#             ventana.resizable(0,0)

#     def setTexto(self, texto):
#         text = Label(self.ventana, text=texto)
#         text.pack()

#     def iniciarVentana(self):
#         self.ventana.mainloop()

# v1 = GUI(2)

# r1 = relojes.Reloj()

# v1.cargarVentana()
# v1.setTexto(r1.iniciarReloj())

# v1.iniciarVentana()

