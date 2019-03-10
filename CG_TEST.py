from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np
root = Tk()
root.title("Рыбка")
root.geometry('1000x600+100+100')

Canv = Canvas(root, width=800, height=600)
Canv.pack(side='left')

Buttons = Frame(root)

Transfer = Frame(Buttons)
Scale = Frame(Buttons)
Turn = Frame(Buttons)

# Перенос
TrvalueL = Label(Transfer, text='Перенос', font='Verdana 16').grid(row=0, column=0, columnspan=4)
TrxL = Label(Transfer, text='dX', font='Verdana 14').grid(row=1, column=0)
TryL = Label(Transfer, text='dY', font='Verdana 14').grid(row=1, column=2)

# Масштабирование
SvalueL = Label(Scale, text='Масштабирование', font='Verdana 16').grid(row=0, column=0, columnspan=4)
SxL = Label(Scale, text='Xc', font='Verdana 14').grid(row=1, column=0)
SyL = Label(Scale, text='Yc', font='Verdana 14').grid(row=1, column=2)
ScxL = Label(Scale, text='KX', font='Verdana 14').grid(row=2, column=0)
ScyL = Label(Scale, text='KY', font='Verdana 14').grid(row=2, column=2)

# Поворот
TuvalueL = Label(Turn, text='Поворот', font='Verdana 16').grid(row=0, column=0, columnspan=4)
TuxL = Label(Turn, text='  X', font='Verdana 14').grid(row=1, column=0)
TuyL = Label(Turn, text='Y', font='Verdana 14').grid(row=1, column=2)
TuangL = Label(Turn, text='Угол', font='Verdana 14').grid(row=2, column=0, columnspan=2)

# Перенос
TrxV = Entry(Transfer, width=5)
TryV = Entry(Transfer, width=5)


# Масштабирование
SxV = Entry(Scale, width=5)
SyV = Entry(Scale, width=5)
ScxV = Entry(Scale, width=5)
ScyV = Entry(Scale, width=5)

# Поворот
TuxV = Entry(Turn, width=5)
TuyV = Entry(Turn, width=5)
TuangV = Entry(Turn, width=10)

#Перенос
TrxV.grid(row=1, column=1)
TryV.grid(row=1, column=3)

# Масштабирование
SxV.grid(row=1, column=1)
SyV.grid(row=1, column=3)
ScxV.grid(row=2, column=1)
ScyV.grid(row=2, column=3)

# Поворот
TuxV.grid(row=1, column=1)
TuyV.grid(row=1, column=3)
TuangV.grid(row=2, column=2, columnspan=2)

def create():
    global Canv, Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Begin_body, Begin_eye, Begin_mouth, Begin_plavnik1, Begin_plavnik2, Begin_plavnik3, Begin_head
    
    dx = 400
    dy = 300
    a = 100
    b = 40
    x = []
    y = []
    for t in np.arange(0,2*pi, 0.1):
        x.append(dx + a*cos(t))
        y.append(dy + b*sin(t))
    for i in range(len(x)):
         Body.append([x[i], y[i]])
    a = 32
    b = 25
    x = []
    y = []
    for t in np.arange(0,2*pi, 0.1):
        x.append(332+a*cos(t))
        y.append(dy + b*sin(t))

    for i in range(len(x)):
         Head.append([x[i], y[i]])
    
##    Head = [dx - 100, dy - 25, dx - 35, dy + 25]
    Eye = [dx - 80, dy - 20, dx - 70, dy - 10]
    Plavnik1 = [[dx - 35,dy + 35], [dx, dy + 70], [dx + 70, dy + 70],[dx + 35, dy + 35]]
    Plavnik2 = [[dx - 35,dy - 35], [dx, dy - 70], [dx + 70, dy - 70],[dx + 35, dy - 35]]
    Plavnik3 = [[dx + 100,dy], [dx + 150, dy - 40], [dx + 125, dy],[dx + 150, dy + 40]]
    Mouth = [dx - 85, dy, dx - 65, dy]
##    Mouth = [dx - 100, dy - 40, dx + 100, dy + 40]
    Begin_body = Body.copy()
    Begin_eye = Eye.copy()
    Begin_mouth = Mouth.copy()
    Begin_plavnik1 = Plavnik1.copy()
    Begin_plavnik2 = Plavnik2.copy()
    Begin_plavnik3 = Plavnik3.copy()
    Begin_head = Head.copy()



def draw():
    global Points, Canv, Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Xc, Yc

    Canv.delete('all')

    Canv.create_polygon(Plavnik1, fill='#e6e6fa', outline='black')
##    print("1 check")
    Canv.create_polygon(Plavnik2, fill='#e6e6fa', outline='black')
##    print("2 check")
    Canv.create_polygon(Body,fill='#e6e6fa', outline='black')
##    print("3 check")
    Canv.create_polygon(Head,fill='#e6e6fa', outline='black')
##    print("4 check")
    Canv.create_oval(Eye,fill='#e6e6fa', outline='black')
##    print("5 check")
    Canv.create_polygon(Plavnik3, fill='#e6e6fa', outline='black')
##    print("6 check")
    Canv.create_line(Mouth)
##    print("7 check")
##
##    Canv.create_polygon(Points, fill='#ffffff', outline='black')


    Canv.create_line(0, 3, 800, 3)
    Canv.create_text(100, 585, text='100')
    Canv.create_text(200, 585, text='200')
    Canv.create_text(300, 585, text='300')
    Canv.create_text(400, 585, text='400')
    Canv.create_text(500, 585, text='500')
    Canv.create_text(600, 585, text='600')
    Canv.create_text(700, 585, text='700')
    Canv.create_text(790, 585, text='X')
    Canv.create_line(3, 0, 3, 600)
    Canv.create_text(16, 100, text='500')
    Canv.create_text(16, 200, text='400')
    Canv.create_text(16, 300, text='300')
    Canv.create_text(16, 400, text='200')
    Canv.create_text(16, 500, text='100')
    Canv.create_text(12, 585, text='0')
    Canv.create_text(12, 10, text='Y')
    Canv.create_line(0, 596, 800, 596)
    Canv.create_line(801, 0, 801, 600)
    
def Transfer_ep():
    global TrxV, TryV, Canv, Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Back_body, Back_eye, Back_mouth, Back_plavnik1, Back_plavnik2, Back_plavnik3, Back_head

    code = 0
    try:
        Trx = float(TrxV.get())
        Try = (-1)*float(TryV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод коэффициентов перемещения.')
        code = 1

    if code == 0:
        Back_body.clear()
        Back_body = Body.copy()
        Body.clear()
        for i, element in enumerate(Back_body):
            x = element[0] + Trx
            y = element[1] + Try
            Body.append([x, y])

        Back_head.clear()
        Back_head = Head.copy()
        Head.clear()
        for i, element in enumerate(Back_head):
            x = element[0] + Trx
            y = element[1] + Try
            Head.append([x, y])

        Back_eye.clear()
        Back_eye = Eye.copy()
        Eye.clear()
        Eye.append(Back_eye[0]+Trx)
        Eye.append(Back_eye[1]+Try)
        Eye.append(Back_eye[2]+Trx)
        Eye.append(Back_eye[3]+Try)

        Back_mouth.clear()
        Back_mouth = Mouth.copy()
        Mouth.clear()
        Mouth.append(Back_mouth[0]+Trx)
        Mouth.append(Back_mouth[1]+Try)
        Mouth.append(Back_mouth[2]+Trx)
        Mouth.append(Back_mouth[3]+Try)

        Back_plavnik1.clear()
        Back_plavnik1 = Plavnik1.copy()
        Plavnik1.clear()

        for i, element in enumerate(Back_plavnik1):
            x = element[0] + Trx
            y = element[1] + Try
            Plavnik1.append([x, y])

        Back_plavnik2.clear()
        Back_plavnik2 = Plavnik2.copy()
        Plavnik2.clear()

        for i, element in enumerate(Back_plavnik2):
            x = element[0] + Trx
            y = element[1] + Try
            Plavnik2.append([x, y])

        Back_plavnik3.clear()
        Back_plavnik3 = Plavnik3.copy()
        Plavnik3.clear()

        for i, element in enumerate(Back_plavnik3):
            x = element[0] + Trx
            y = element[1] + Try
            Plavnik3.append([x, y])

        draw()

def Scale_ep():
    global Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Back_body, Back_eye, Back_mouth, Back_plavnik1, Back_plavnik2, Back_plavnik3, Back_head

    code = 0
    try:
        Xc = float(SxV.get())
        Yc = 800 - float(SyV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод центра масштабирования.')
        code = 1
    try:
        kx = float(ScxV.get())
        ky = float(ScyV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод коэффициентов масштабирования.')
        code = 1

    if code == 0:
        
        Back_body.clear()
        Back_body = Body.copy()
        Body.clear()
        for i, element in enumerate(Back_body):
            x = kx*element[0] + (1-kx)*Xc
            y = ky*element[1] + (1-ky)*Yc
            Body.append([x, y])
        
        Back_head.clear()
        Back_head = Head.copy()
        Head.clear()
        for i, element in enumerate(Back_head):
            x = kx*element[0] + (1-kx)*Xc
            y = ky*element[1] + (1-ky)*Yc
            Head.append([x, y])
        
        Back_eye.clear()
        Back_eye = Eye.copy()
        Eye.clear()
        XX1 = kx * Back_eye[0]+(1 - kx) * Xc
        XX2 = kx * Back_eye[2]+(1 - kx) * Xc
        YY1 = ky * Back_eye[1]+(1 - ky) * Yc
        YY2 = ky * Back_eye[3]+(1 - ky) * Yc
        Eye.append(XX1)
        Eye.append(YY1)
        Eye.append(XX2)
        Eye.append(YY2)


        Back_mouth.clear()
        Back_mouth = Mouth.copy()
        Mouth.clear()
        XX1 = kx * Back_mouth[0]+(1 - kx) * Xc
        XX2 = kx * Back_mouth[2]+(1 - kx) * Xc
        YY1 = ky * Back_mouth[1]+(1 - ky) * Yc
        YY2 = ky * Back_mouth[3]+(1 - ky) * Yc
        Mouth.append(XX1)
        Mouth.append(YY1)
        Mouth.append(XX2)
        Mouth.append(YY2)
        
        Back_plavnik1.clear()
        Back_plavnik1 = Plavnik1.copy()
        Plavnik1.clear()
        for i, element in enumerate(Back_plavnik1):
            x = kx*element[0] + (1-kx)*Xc
            y = ky*element[1] + (1-ky)*Yc
            Plavnik1.append([x, y])

        Back_plavnik2.clear()
        Back_plavnik2 = Plavnik2.copy()
        Plavnik2.clear()
        for i, element in enumerate(Back_plavnik2):
            x = kx*element[0] + (1-kx)*Xc
            y = ky*element[1] + (1-ky)*Yc
            Plavnik2.append([x, y])

        Back_plavnik3.clear()
        Back_plavnik3 = Plavnik3.copy()
        Plavnik3.clear()
        for i, element in enumerate(Back_plavnik3):
            x = kx*element[0] + (1-kx)*Xc
            y = ky*element[1] + (1-ky)*Yc
            Plavnik3.append([x, y])


        draw()

def Turn_ep():
    global Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Back_body, Back_eye, Back_mouth, Back_plavnik1, Back_plavnik2, Back_plavnik3, Back_head

    code = 0
    try:
        Xc = float(TuxV.get())
        Yc = float(TuyV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод центра поворота.')
        code = 1

    try:
        teta = float(TuangV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод угла поворота.')
        code = 1

    if code == 0:
        teta = radians(teta)
        #teta= degrees(teta)

######################################################        
        Back_body.clear()
        Back_body = Body.copy()
        Body.clear()
        for i, element in enumerate(Back_body):
            x = Xc + (element[0] - Xc)*cos(teta) + (element[1] - Yc)*sin(teta)
            y = Yc - (element[0] - Xc)*sin(teta) + (element[1] - Yc)*cos(teta)
            Body.append([x, y])

        
        Back_head.clear()
        Back_head = Head.copy()
        Head.clear()
        for i, element in enumerate(Back_head):
            x = Xc + (element[0] - Xc)*cos(teta) + (element[1] - Yc)*sin(teta)
            y = Yc - (element[0] - Xc)*sin(teta) + (element[1] - Yc)*cos(teta)
            Head.append([x, y])
        
        Back_eye.clear()
        Back_eye = Eye.copy()
        Eye.clear()

        XX = (Back_eye[0] + Back_eye[2])/2
        YY = (Back_eye[1] + Back_eye[3])/2
        DELTA_X = Begin_eye[0] - Begin_eye[2]
        DELTA_Y = Begin_eye[1] - Begin_eye[3]
        
        XXC = Xc + (XX - Xc)*cos(teta) + (YY - Yc)*sin(teta)
        YYC = Yc - (XX - Xc)*sin(teta) + (YY - Yc)*cos(teta)
        
        Eye.append(XXC - DELTA_X/2)
        Eye.append(YYC - DELTA_Y/2)
        Eye.append(XXC + DELTA_X/2)
        Eye.append(YYC + DELTA_Y/2)


        Back_mouth.clear()
        Back_mouth = Mouth.copy()
        Mouth.clear()
        XX1 = Xc + (Back_mouth[0] - Xc)*cos(teta) + (Back_mouth[1] - Yc)*sin(teta)
        YY1 = Yc - (Back_mouth[0] - Xc)*sin(teta) + (Back_mouth[1] - Yc)*cos(teta)
        XX2 = Xc + (Back_mouth[2] - Xc)*cos(teta) + (Back_mouth[3] - Yc)*sin(teta)
        YY2 = Yc - (Back_mouth[2] - Xc)*sin(teta) + (Back_mouth[3] - Yc)*cos(teta)
        Mouth.append(XX1)
        Mouth.append(YY1)
        Mouth.append(XX2)
        Mouth.append(YY2)
        
        Back_plavnik1.clear()
        Back_plavnik1 = Plavnik1.copy()
        Plavnik1.clear()
        for i, element in enumerate(Back_plavnik1):
            x = Xc + (element[0] - Xc)*cos(teta) + (element[1] - Yc)*sin(teta)
            y = Yc - (element[0] - Xc)*sin(teta) + (element[1] - Yc)*cos(teta)
            Plavnik1.append([x, y])

        Back_plavnik2.clear()
        Back_plavnik2 = Plavnik2.copy()
        Plavnik2.clear()
        for i, element in enumerate(Back_plavnik2):
            x = Xc + (element[0] - Xc)*cos(teta) + (element[1] - Yc)*sin(teta)
            y = Yc - (element[0] - Xc)*sin(teta) + (element[1] - Yc)*cos(teta)
            Plavnik2.append([x, y])

        Back_plavnik3.clear()
        Back_plavnik3 = Plavnik3.copy()
        Plavnik3.clear()
        for i, element in enumerate(Back_plavnik3):
            x = Xc + (element[0] - Xc)*cos(teta) + (element[1] - Yc)*sin(teta)
            y = Yc - (element[0] - Xc)*sin(teta) + (element[1] - Yc)*cos(teta)
            Plavnik3.append([x, y])       
        draw()

def Back_ep():
    global Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Back_body, Back_eye, Back_mouth, Back_plavnik1, Back_plavnik2, Back_plavnik3, Back_head    
    Body = Back_body.copy()
    Head = Back_head.copy()
    Eye = Back_eye.copy()
    Mouth = Back_mouth.copy()
    Plavnik1 = Back_plavnik1.copy()
    Plavnik2 = Back_plavnik2.copy()
    Plavnik3 = Back_plavnik3.copy()
    draw()

def Begin_ep():
    global Body, Head, Eye, Mouth, Plavnik1, Plavnik2, Plavnik3, Begin_body, Begin_eye, Begin_mouth, Begin_plavnik1, Begin_plavnik2, Begin_plavnik3, Begin_head

    Body = Begin_body.copy()
    Head = Begin_head.copy()
    Eye = Begin_eye.copy()
    Mouth = Begin_mouth.copy()
    Plavnik1 = Begin_plavnik1.copy()
    Plavnik2 = Begin_plavnik2.copy()
    Plavnik3 = Begin_plavnik3.copy()
    draw()

Yc = Xc = 0

Square = []
Back_square = []
Begin_square = []

Body = []
Begin_body = []
Back_body = []

Head = []
Begin_head = []
Back_head = []

Eye = []
Begin_eye = []
Back_eye = []

Mouth = []
Begin_mouth = []
Back_mouth = []

Plavnik1 = []
Begin_plavnik1 = []
Back_plavnik1 = []

Plavnik2 = []
Begin_plavnik2 = []
Back_plavnik2 = []

Plavnik3 = []
Begin_plavnik3 = []
Back_plavnik3 = []

create()
draw()

TransferButton = Button(Buttons, text='Перенос', font='Verdana 14', command=Transfer_ep, width=8)                    # +
ScaleButton = Button(Buttons, text='Масштаб', font='Verdana 14', command=Scale_ep, width=8)                          # +
TurnButton = Button(Buttons, text='Поворот', font='Verdana 14', command=Turn_ep, width=8)                            # +
BackButton = Button(Buttons, text='Назад', font='Verdana 14', command=Back_ep, width=12, height=1)                   # +
BeginButton = Button(Buttons, text='В начало', font='Verdana 14', command=Begin_ep, width=12, height=1)              # +


Transfer.grid(row=0, column=0, columnspan=2)
TransferButton.grid(row=1, column=0, columnspan=2)
Label(Buttons, text='              ').grid(row=2, column=0, columnspan=4)
Label(Buttons, text='              ').grid(row=3, column=0, columnspan=4)
    
Scale.grid(row=4, column=0, columnspan=2)
ScaleButton.grid(row=5, column=0, columnspan=2)
Label(Buttons, text='              ').grid(row=6, column=0, columnspan=4)
Label(Buttons, text='              ').grid(row=7, column=0, columnspan=4)

Turn.grid(row=8, column=0, columnspan=2)
TurnButton.grid(row=9, column=0, columnspan=2)
Label(Buttons, text='              ').grid(row=10, column=0, columnspan=4)
Label(Buttons, text='              ').grid(row=11, column=0, columnspan=4)
BackButton.grid(row=12, column=0, columnspan=4)
BeginButton.grid(row=13, column=0, columnspan=4)

Buttons.pack(side='top')
Canv.pack()

root.mainloop()
