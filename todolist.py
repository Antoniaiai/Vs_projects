#Projeto de um to-do list em python com tk inter
App_version = "0.0.1"
#importa o tkinter
import tkinter as tk
from tkinter import *
#config da janelas(nome, tamanho, etc)
janela = tk.Tk()
frame = Frame(janela)
janela.title("To Do List--VERSION:  " + App_version)
janela.geometry("500x500")

# configurações da janela
tk.Label(janela, text="TO-DO LIST").pack()
#faz a janela aparecer e PERMANECER aberta
janela.mainloop()