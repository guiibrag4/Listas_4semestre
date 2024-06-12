import tkinter as tk
from xmlrpc.client import ServerProxy

# Conexão com o servidor RPC
server = ServerProxy('http://localhost:8000')

def somar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = server.somar(num1, num2)
    label_result.config(text=f'Resultado: {result}')

def subtrair():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = server.subtrair(num1, num2)
    label_result.config(text=f'Resultado: {result}')

def multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = server.multiplicar(num1, num2)
    label_result.config(text=f'Resultado: {result}')

def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = server.dividir(num1, num2)
    label_result.config(text=f'Resultado: {result}')

# Interface gráfica
root = tk.Tk()

label_num1 = tk.Label(root, text='Número 1:')
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text='Número 2:')
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

button_somar = tk.Button(root, text='Somar', command=somar, fg='white', bg='blue')
button_somar.pack()

button_subtrair = tk.Button(root, text='Subtrair', command=subtrair)
button_subtrair.pack()

button_multiplicar = tk.Button(root, text='Multiplicar', command=multiplicar)
button_multiplicar.pack()

button_dividir = tk.Button(root, text='Dividir', command=dividir)
button_dividir.pack()

label_result = tk.Label(root, text='Resultado:')
label_result.pack()

# button_somar.config (height=3, width=20)

root.mainloop()