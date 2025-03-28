import tkinter as tk

# Versão do App
App_version = "0.0.1"

# Configurações da janela principal
janela = tk.Tk()
janela.title("To Do List--VERSION: " + App_version)
janela.geometry("500x500")

# Frame principal com padding
frame = tk.Frame(janela, padx=40, pady=40, bg = "black")
frame.grid(column=0, row=0)  # Usando grid para posicionar o frame

# Labels e widgets dentro do frame, agora usando grid
tk.Label(frame, text="TO-DO LIST", font=("Arial", 16)).grid(row=0, column=0, pady=10)

tk.Label(frame, text="Adicionar tarefa:").grid(row=1, column=0, pady=5)
entry_tarefa = tk.Entry(frame, width=40)
entry_tarefa.grid(row=2, column=0, pady=5)

#Label de listas de tarefas
tk.Label(frame, text="TAREFAS").grid(row=4, column=0, pady=10)

# Botão para adicionar a tarefa
botao_adicionar = tk.Button(frame, text="Adicionar")
botao_adicionar.grid(row=3, column=0, pady=10)

#Botao para excluir tarefa
botao_excluir = tk.Button(frame, text="Excluir tarefa")
botao_excluir.grid(row=3, column= 0, pady= 10)

# Faz a janela aparecer e permanecer aberta
janela.mainloop()
