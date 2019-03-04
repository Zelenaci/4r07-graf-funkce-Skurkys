import tkinter as tk
from tkinter import Label,Radiobutton, IntVar, StringVar, Button, Entry, LabelFrame, Message, messagebox
import pylab as lab
from tkinter import filedialog

class Application(tk.Tk):
    name = 'Graf funkce'
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=5)
        
        self.grflblfr = LabelFrame(self,text=u"Generuj graf funkce", padx=20)
        self.grflblfr.grid(row=1,column=1)
        
        self.fcelbl = Label(self.grflblfr)
        self.fcelbl.grid(row=1, column=1)
        
        self.vyber = IntVar()
        
        self.sinrdb = Radiobutton(self.fcelbl,text=u"sin",variable=self.vyber, value=1)
        self.sinrdb.grid(row=1,column=1)
        
        self.logrdb = Radiobutton(self.fcelbl,text=u"log",variable=self.vyber, value=2)
        self.logrdb.grid(row=2,column=1) 
        
        self.exprdb = Radiobutton(self.fcelbl,text=u"exp",variable=self.vyber, value=3)
        self.exprdb.grid(row=3,column=1)
        
        self.oddolbl = Label(self.grflblfr)
        self.oddolbl.grid(row=1, column=2)
        
        self.odmess = Message(self.oddolbl, text=u"Od:")
        self.odmess.grid(row=1, column=1)
        
        self.fMin=StringVar()
        
        self.odentr = Entry(self.oddolbl, textvariable=self.fMin,width=10)
        self.odentr.grid(row=1,column=2)
        
        self.domess = Message(self.oddolbl, text=u"Do:")
        self.domess.grid(row=2, column=1)
        
        self.fMax=StringVar()
        
        self.doentr = Entry(self.oddolbl, textvariable=self.fMax,width=10)
        self.doentr.grid(row=2,column=2)
        
        self.vga = Button(self,text=u"Vytvoř graf", width=10, height=4, command=self.fGraf)
        self.vga.grid(row=1,column=2)
        
        self.grftxtlblfr = LabelFrame(self,text=u"Generuj graf z textových dat", padx=25)
        self.grftxtlblfr.grid(row=2,column=1)
        
        self.soubor = StringVar()
        self.soubor.set("cesta/k/souboru")
        
        self.csentr = Entry(self.grftxtlblfr, textvariable = self.soubor)
        self.csentr.grid(row=1,column=1)
        
        self.vyb = Button(self.grftxtlblfr,text=u"Vyber soubor",command = self.VyberSoubor)
        self.vyb.grid(row=2,column=1)
        
        self.vgb = Button(self,text=u"Vytvoř graf", width=10, height=4, command=self.fSoubor)
        self.vgb.grid(row=2,column=2)
        
        self.osylblfr = LabelFrame(self,text=u"Popisky os", padx=40)
        self.osylblfr.grid(row=3,column=1)
        
        self.osxmess = Message(self.osylblfr, text=u"Osa X:")
        self.osxmess.grid(row=1, column=1)
        
        self.osx = StringVar()
        
        self.osxentr = Entry(self.osylblfr, textvariable=self.osx,width=10)
        self.osxentr.grid(row=1,column=2)
        
        self.osymess = Message(self.osylblfr, text=u"Osa Y:")
        self.osymess.grid(row=2, column=1)
        
        self.osy = StringVar()
        
        self.osyentr = Entry(self.osylblfr, textvariable=self.osy,width=10)
        self.osyentr.grid(row=2,column=2)
        
        
        
    
        
    def fGraf(self):
        try:
            od=float(self.fMin.get())
            do=float(self.fMax.get())
            x=lab.linspace(od, do, 500)
            if self.vyber.get() == 1:
                y=lab.sin(x)
            elif self.vyber.get() == 2:
                y=lab.log10(x)
            elif self.vyber.get() == 3:
                y=lab.exp(x)
            lab.figure()
            lab.plot(x,y)
            lab.xlabel(self.osx.get())
            lab.ylabel(self.osy.get())
            lab.grid(True)
            lab.show()
        except:
            messagebox.showerror(title='Chybné meze',
                                 message='Zadejte meze osy X\njako reálná čísla')        

    def VyberSoubor(self):
        self.cesta = filedialog.askopenfilename(title = 'Vyber soubor')
        if self.cesta != '':
            self.soubor.set(self.cesta)

    def fSoubor(self):
        try:
            cesta = self.soubor.get()
            f = open (cesta, 'r')
            x = []
            y = []
            while True:
                radek = f.readline()
                if radek == '':
                    break
                else:
                    cisla = radek.split()
                    x.append (float(cisla[0]))
                    y.append (float(cisla[1]))
            f.close()
            lab.figure()
            lab.plot(x,y)
            lab.xlabel(self.osx.get())
            lab.ylabel(self.osy.get())
            lab.grid(True)
            lab.show()
        except:
            messagebox.showerror(title='Chybný formát souboru', 
                          message='Graf se nepodařilo vytvořit,\nzkontrolujte formát souboru.')


app = Application()
app.mainloop()
