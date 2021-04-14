import os,time,random
from tkinter import *

#### creacion de la pantalla ####
root = Tk()
root.title('Practica 1 - Desarrollo de Sistemas Distribuidos')
frame = Frame()
frame.pack()
frame.config(width=800, height=400)

#### declarion de las variables de h y m ###
h1 = random.randint(0,23)
m1 = random.randint(0,60)
h2 = random.randint(0,23)
m2 = random.randint(0,60)
h3 = random.randint(0,23)
m3 = random.randint(0,60)
h4 = random.randint(0,23)
m4 = random.randint(0,60)    

#### funcion para editar el reloj 1 ####
def edit1():
    global valor1
    valor1 = False
    edicion = Toplevel(root)
    edicion.config(width = 300, height=130)
    edicion.title('Cambiar hora')
    global horaEdit
    lblHoraEdit = Label(edicion, text='Hora', font=('Open Sans', 13))
    lblHoraEdit.place(x=25, y=20)
    horaEdit = Entry(edicion, width=7)
    horaEdit.place(x=25, y=50)
    lblMinEdit = Label(edicion, text='Minutos', font=('Open Sans', 13))
    lblMinEdit.place(x=95, y=20)
    minEdit = Entry(edicion, width=11)
    minEdit.place(x=95, y=50)
    lblSegEdit = Label(edicion, text='Segundos', font=('Open Sans', 13))
    lblSegEdit.place(x=185, y=20)
    segEdit = Entry(edicion, width=13)
    segEdit.place(x=185, y=50)
    guardarBtn = Button(edicion, text='Guardar', command=None)
    guardarBtn.place(x=120, y=85)

############ reloj1 vista #############
def hr1(h1,m1):
    for s in range(0,10): #### aqui estoy intentando que aparezca el segundero pero no cuenta y despues muestra el ultimo numero del conteo
        lblTiempo1 = Label(frame, text='{}:{}:{}'.format(h1,m1,s), font=('Digital-7 Mono', 70))
        lblTiempo1.place(x=30, y=60)
        time.sleep(1) ### con esta se supone que manejamos la velocidad

lblReloj1 = Label(frame, text = 'Reloj 1', font=('Open Sans', 15))
lblReloj1.place(x=30, y=15)

hr1(h1,m1)

editar1Btn = Button(frame, text='', command=edit1)
editar1Btn.place(x=100, y=15)


############ reloj2 vista #############
lblReloj2 = Label(frame, text = 'Reloj 2', font=('Open Sans', 15))
lblReloj2.place(x=30, y=160)
editar2Btn = Button(frame, text='', command=None)
editar2Btn.place(x=100, y=160)
def hr2(h2,m2):
    for s in range(0,10):#### aqui estoy intentando que aparezca el segundero pero no cuenta y despues muestra el ultimo numero del conteo
        lblTiempo2 = Label(frame, text='{}:{}:{}'.format(h2,m2,s), font=('Digital-7 Mono', 70))
        lblTiempo2.place(x=30, y=205)
        time.sleep(1) ### con esta se supone que manejamos la velocidad
hr2(h2,m2)

############ reloj3 vista #############
lblReloj3 = Label(frame, text = 'Reloj 3', font=('Open Sans', 15))
lblReloj3.place(x=420, y=15)
editar3Btn = Button(frame, text='', command=None)
editar3Btn.place(x=500, y=15)
def hr3(h3,m3):
    for s in range(0,10): #### aqui estoy intentando que aparezca el segundero pero no cuenta y despues muestra el ultimo numero del conteo
        lblTiempo3 = Label(frame, text='{}:{}:{}'.format(h3,m3,s), font=('Digital-7 Mono', 70))
        lblTiempo3.place(x=420, y=60)
        time.sleep(1) ### con esta se supone que manejamos la velocidad
hr3(h3,m3)

############ reloj4 vista #############
lblReloj4 = Label(frame, text = 'Reloj 4', font=('Open Sans', 15))
lblReloj4.place(x=420, y=160)
editar4Btn = Button(frame, text='', command=None)
editar4Btn.place(x=500, y=160)
def hr4(h4,m4):
    for s in range(0,10):#### aqui estoy intentando que aparezca el segundero pero no cuenta y despues muestra el ultimo numero del conteo
        lblTiempo4 = Label(frame, text='{}:{}:{}'.format(h4,m4,s), font=('Digital-7 Mono', 70))
        lblTiempo4.place(x=420, y=205)
        time.sleep(1) ### con esta se supone que manejamos la velocidad
hr4(h4,m4)


root.mainloop()

### este codigo si funciona como deberia de funcionar los relojes, pero tengo duda en los segundos
### si quieres pruebalo aparte para que veas como se ve en consola

'''
while(True):
    
    hru1 = int(input("Que hr desea colocar al reloj 1: "))
    
    if hru1 >= 0 and hru1 <= 23:
        h1 = hru1
    else:
        print('no se pudo')

    minu1 =  int(input("Que min desea colocar al reloj 1: "))
    if minu1 >= 0 and minu1 <= 60:
        m1 = minu1
    else:
        print('no se pudo')

    tr1 = int(input("Que velocidad desea colocar al reloj 1: "))
    for s in range(60):
        os.system('clear')
        print('{}:{}:{}'.format(h1,m1,s))
        
        print('{}:{}:{}'.format(h2,m2,s))
        print('{}:{}:{}'.format(h3,m3,s))
        print('{}:{}:{}'.format(h4,m4,s))
        time.sleep(tr1) #para que dure en vista
        '''