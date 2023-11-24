from tkinter import *

root = Tk() # Crear ventana principal

# Personalizamos la ventana principal
root.title("Calculadora")
root.resizable(0,0) # Evitamos que el usuario cambie el tamaño
root.geometry("400x400") # Tamaño de la ventana

input_texto = ""

# Creamos el frame donde se mostrarán los resultados
input_usuario = Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_usuario.pack(side=TOP)

input_area = Entry(input_usuario, font=('arial', 18, 'bold'), textvariable=input_texto, width=50, bg="#eee", bd=0, justify=RIGHT)
input_area.grid(row=0, column=0)
input_area.pack(ipady=10) 

# Creamos el frame donde se mostrarán los botones
btns_frame = Frame(root, width=400, height=350, bg="grey")
btns_frame.pack()

root.mainloop() # Este comando nos permite mostrar la ventana principal