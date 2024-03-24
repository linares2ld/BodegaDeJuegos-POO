import tkinter as tk
from tkinter import messagebox as mb
import time
import numpy as np

class SimonDice():
    def __init__(self):
        self.numero_combinaciones = 6
        self.contador = 0
        self.listareferencia = []
        self.listajuego = []
        self.botones = []
        self.bcolores =["#0000FF","#FF0000","#00FF00","#FFFF00"]
        self.metodos = [self.B1,self.B2,self.B3,self.B4]
    def interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("300x250")
        self.root.title("Simón dice")
        
        for i in range(4):
            self.botones.append(tk.Button(self.root,
                                          width=11,
                                          height=5,
                                          bg=self.bcolores[i],
                                          command=self.metodos[i],
                                          state=tk.DISABLED))

        c=0
        for i  in range(2):
            for j in range(2):
                self.botones[c].place(x=30+j*100,y=30+i*100)
                c += 1

        self.binicio = tk.Button(self.root,
                                 text="Inicio",
                                 width=5,
                                 height=1,
                                 command=self.inicio)
        self.binicio.place(x=240,y=100)
        self.root.mainloop()

    def B1(self):
        self.resultado(1)

    def B2(self):
        self.resultado(2)

    def B3(self):
        self.resultado(3)

    def B4(self):
        self.resultado(4)

    def resultado(self,posicion):
        self.listajuego.append(posicion)
        
        if self.listareferencia[self.contador] != self.listajuego[self.contador]:
            mb.showerror(title="Mensaje del juego",message="Perdiste")
            for i in range(4):
                self.botones[i].config(state=tk.DISABLED)

        self.contador += 1
        if self.contador == self.numero_combinaciones:
            mb.showinfo(title="Mensaje del juego",message="Ganaste")
            for i in range(4):
                self.botones[i].config(state=tk.DISABLED)

    def inicio(self):
        for i in range(4):
            self.botones[i].config(state=tk.NORMAL)

        self.contador = 0
        self.listareferencia = []
        self.listajuego = []
        self.listareferencia = np.random.randint(1,5,self.numero_combinaciones)
        for i in self.listareferencia:
            if i == 1:
                self.botones[0].config(bg="#FFFFFF")
            elif i == 2:
                self.botones[1].config(bg="#FFFFFF")
            elif i == 3:
                self.botones[2].config(bg="#FFFFFF")
            else:
                self.botones[3].config(bg="#FFFFFF")

            self.root.update()
            time.sleep(0.4)

            if i == 1:
                self.botones[0].config(bg="#0000FF")
            elif i == 2:
                self.botones[1].config(bg="#FF0000")
            elif i == 3:
                self.botones[2].config(bg="#00FF00")
            else:
                self.botones[3].config(bg="#FFFF00")

            self.root.update()
            time.sleep(0.4)

calculadora = SimonDice()
calculadora.interfaz()
