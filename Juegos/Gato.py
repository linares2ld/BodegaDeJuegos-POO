import tkinter as tk
from tkinter import messagebox as mb
import numpy as np

class Gato():
    def __init__(self):
        self.contador = 0
        self.ganador = 0
        self.jugador1 = True
        self.jugadasjugador1 = np.zeros((9))
        self.jugadasjugador2 = np.zeros((9))
        self.botones = []
        self.metodos = [self.B1,self.B2,self.B3,
                        self.B4,self.B5,self.B6,
                        self.B7,self.B8,self.B9]

    def interfaz(self):
        self.root = tk.Tk()
        self.root.title("Gato")
        self.root.geometry("450x350")

        for i in range(9):
            self.botones.append(tk.Button(self.root,
                                          width=11,
                                          height=5,
                                          command=self.metodos[i]))

        c=0
        for i  in range(3):
            for j in range(3):
                self.botones[c].place(x=30+j*100,y=30+i*100)
                c += 1


        self.binicio = tk.Button(self.root,
                                 text="Inicio",
                                 width=6,
                                 height=2,
                                 command=self.inicio)
        self.binicio.place(x=355,y=150)

        self.color_defecto = self.binicio.cget('bg')
        self.root.mainloop()

    def jugada(self,posicion):
        if self.jugador1:
            self.jugadasjugador1[posicion] = 1
            jugador="#0000FF"
        else:
            self.jugadasjugador2[posicion] = 1
            jugador="#FF0000"
        self.botones[posicion].config(bg=jugador,
                                      state=tk.DISABLED)
        self.resultado()
        self.mostrarGanador()
        self.jugador1 = not self.jugador1
        self.contador += 1
        if self.contador == 8:
            self.ganador = 3

    def mostrarGanador(self):
        if self.ganador == 1:
            mb.showinfo(title="Mensaje del juego",message="Ganó azul")
            for i in range(9):
                self.botones[i].config(state=tk.DISABLED)
        elif self.ganador == 2:
            mb.showinfo(title="Mensaje del juego",message="Ganó rojo")
            for i in range(9):
                self.botones[i].config(state=tk.DISABLED)
        elif self.ganador == 3:
            mb.showinfo(title="Mensaje del juego",message="Empate")
            for i in range(9):
                self.botones[i].config(state=tk.DISABLED)      

    def resultado(self):
        if self.jugador1:
            n = self.jugadasjugador1
            for i in range(8):
                if i == 0:
                    m = sum(n[0:3])
                elif i == 1:
                    m = sum(n[3:6])
                elif i == 2:
                    m = sum(n[6:9])
                elif i == 3:
                    m = n[0] + n[3] + n[6]
                elif i == 4:
                    m = n[1] + n[4] + n[7]
                elif i == 5:
                    m = n[2] + n[5] + n[8]
                elif i == 6:
                    m = n[0] + n[4] + n[8]
                elif i == 7: 
                    m = n[2] + n[4] + n[6]

                if m == 3:
                    self.ganador = 1
                    break
        else:
            n = self.jugadasjugador2
            for i in range(8):
                if i == 0:
                    m = sum(n[0:3])
                elif i == 1:
                    m = sum(n[3:6])
                elif i == 2:
                    m = sum(n[6:9])
                elif i == 3:
                    m = n[0] + n[3] + n[6]
                elif i == 4:
                    m = n[1] + n[4] + n[7]
                elif i == 5:
                    m = n[2] + n[5] + n[8]
                elif i == 6:
                    m = n[0] + n[4] + n[8]
                elif i == 7: 
                    m = n[2] + n[4] + n[6]

                if m == 3:
                    self.ganador = 2
                    break

    def inicio(self):
        self.contador = 0
        self.ganador = 0
        self.jugador1 = True
        self.jugadasjugador1 = np.zeros((9))
        self.jugadasjugador2 = np.zeros((9))
        for i in range(9):
                self.botones[i].config(bg=self.color_defecto,
                                       state=tk.NORMAL)
    def B1(self):
        self.jugada(0)
    def B2(self):
        self.jugada(1)
    def B3(self):
        self.jugada(2)
    def B4(self):
        self.jugada(3)
    def B5(self):
        self.jugada(4)
    def B6(self):
        self.jugada(5)
    def B7(self):
        self.jugada(6)
    def B8(self):
        self.jugada(7)
    def B9(self):
        self.jugada(8)
        
calculadora = Gato()
calculadora.interfaz()
