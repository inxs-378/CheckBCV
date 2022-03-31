from tkinter import PhotoImage,Tk,Button,Toplevel,messagebox,Entry,Label,Canvas,END
from tkinter.constants import E,NW,W
import requests
import pandas
import os

while True:
    
    if os.path.exists('/Cbcv/'):
        url = 'http://www.bcv.org.ve/sites/default/files/EstadisticasGeneral/2_1_2a22_smc.xls'
        r = requests.get(url, allow_redirects=True)
        open('/Cbcv/2_1_2a22_smc.xls', 'wb').write(r.content)
        df = pandas.read_excel('/Cbcv/2_1_2a22_smc.xls')
        value_time = df.iloc[3,3]
        value_usd = df.iloc[13,6]
        value_eur = df.iloc[9,6]
        value_cop = df.iloc[22,6]

        class Calc:
            def getandreplace(self):
                self.txt = self.e.get()
                self.txt = self.txt.replace('÷', '/')
                self.txt = self.txt.replace('x', '*')

            def evaluation(self, specfunc):
                self.getandreplace()
                try:
                    self.txt = round(eval(str(self.txt)),3)
                except SyntaxError:
                    self.displayinvalid()
                else:
                    self.refreshtext()

            def displayinvalid(self):
                self.e.delete(0, END)
                self.e.insert(0, 'ERROR')

            def refreshtext(self):
                self.e.delete(0, END)
                self.e.insert(0, self.txt)

            def clearall(self):
                self.e.delete(0, END)
                self.e.insert(0, '0')

            def action(self, argi: object):
                self.txt = self.getvalue()
                self.stripfirstchar()
                self.e.insert(END, argi)

            def keyaction(self, event=None):
                self.txt = self.getvalue()
                if event.char.isdigit():
                    self.stripfirstchar()
                elif event.char in '/*-+.':
                    self.stripfirstchar()
                elif event.char == '\x08':
                    self.clearall()
                elif event.char == '\r':
                    self.evaluation('eq')
                else:
                    self.displayinvalid()
                    return 'break'

            def stripfirstchar(self):
                if self.txt[0] == '0':
                    self.e.delete(0, 1)

            def getvalue(self):
                return self.e.get()

            def cl_ref(self):
                messagebox.showinfo("Referencia del Dia", 
                f"{value_time}\n\n1USD$ = {value_usd}Bs\n1EUR€ = {value_eur}Bs\n1COL$ = {value_cop}Bs\n\n(Datos extraidos del BCV)")

            def openi(self):
                ventana2=Toplevel()
                ventana2.title("Tutorial")
                ventana2.resizable(False, False)
                canvas = Canvas(ventana2, width=351 , height=337)
                canvas.pack(expand = 'YES', fill = 'both')
                my_image = PhotoImage(file='C:\Cbcv\prueba.png')
                canvas.create_image(0, 0, anchor=NW, image=my_image)
                ventana2.mainloop()

            def __init__(self, master):
                self.txt = 'o'
                master.title('CheckBCV')
                master.resizable(False, False)
                master.configure(background="gray")
                self.e = Entry(master, font=('arial',20,'bold'), width=20, bd=15, justify="right")
                self.e.grid(row=1, column=1, columnspan=4)
                self.e.insert(0, '0')
                self.e.focus_set()

                ancho_boton=6
                color_boton=("gray77")
                estilo=('arial',16)

                Button(master, text="Ayuda", bg="Orange", width=ancho_boton, font=('arial',8), command=self.openi).grid(row=0, column=4)
                Button(master, text="G", bg="white", width=0, font=('arial',8,'bold')).grid(row=1, column=5)
                Button(master, text="R", bg="Yellow", width=0, font=('arial',8,'bold'), command= self.cl_ref).grid(row=2, column=0, sticky=E)
                Button(master,text="EUR€", bg='green yellow', font=estilo, width=ancho_boton, command=lambda:self.action(value_eur)).grid(row=2, column=1)
                Button(master,text="USD$", bg='green yellow', font=estilo, width=ancho_boton, command=lambda: self.action(value_usd)).grid(row=2, column=2)
                Button(master,text="COL$", bg='green yellow', font=estilo, width=ancho_boton, command=lambda: self.action(value_cop)).grid(row=2, column=3)
                Button(master, text='AC',bg='red', font=estilo, width=ancho_boton, command=lambda: self.clearall()).grid(row=2, column=4)
                Button(master, text="7", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('7')).grid(row=3, column=1)
                Button(master, text="8", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('8')).grid(row=3, column=2)
                Button(master, text="9", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('9')).grid(row=3, column=3)
                Button(master, text="÷", bg="Royalblue1", width=ancho_boton, font=estilo, command=lambda: self.action('÷')).grid(row=3, column=4)
                Button(master, text="4", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('4')).grid(row=4, column=1)
                Button(master, text="5", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('5')).grid(row=4, column=2)
                Button(master, text="6", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('6')).grid(row=4, column=3)
                Button(master, text="x", bg="Royalblue1", width=ancho_boton, font=estilo, command=lambda: self.action('x')).grid(row=4, column=4)
                Button(master, text="1", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('1')).grid(row=5, column=1)
                Button(master, text="2", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('2')).grid(row=5, column=2)
                Button(master, text="3", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('3')).grid(row=5, column=3)
                Button(master, text="-", bg="Royalblue1", width=ancho_boton, font=estilo, command=lambda: self.action('-')).grid(row=5, column=4)
                Button(master, text="0", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('0')).grid(row=6, column=1)
                Button(master, text=".", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.action('.')).grid(row=6, column=2)
                Button(master, text="=", bg=color_boton, width=ancho_boton, font=estilo, command=lambda: self.evaluation('eq')).grid(row=6, column=3)
                Button(master, text="+", bg="Royalblue1", width=ancho_boton, font=estilo, command=lambda: self.action('+')).grid(row=6, column=4)
            
                Sublabel = Label(master, text='Creado por Javier Ramsbott. GNU GPL 2021', bg='gray')
                Sublabel.grid(row=7, column=1, columnspan=6, sticky=W)

                self.e.bind('<Key>', lambda evt: self.keyaction(evt))

        root = Tk()
        obj = Calc(root)
        root.mainloop()

    else:
        os.makedirs('/Cbcv')
    