from tkinter import *
from operacion import calcular

root = Tk() # Crear ventana principal

# Personalizamos la ventana principal
root.title("Calculadora")
root.resizable(0,0) # Evitamos que el usuario cambie el tamaño
root.geometry("400x400") # Tamaño de la ventana

input_texto = [] # Variable que almacena el texto del input

# Creamos el frame donde se mostrarán los resultados
input_usuario = Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_usuario.pack(side=TOP)

input_area = Entry(input_usuario, font=('arial', 18, 'bold'), textvariable=input_texto, width=50, bg="#eee", bd=0, justify=RIGHT)
input_area.grid(row=0, column=0)
input_area.pack(ipady=10) 

# Creamos el frame donde se mostrarán los botones
btns_frame = Frame(root, width=400, height=350, bg="grey")
btns_frame.pack()

# ---------
# Funciones
# ---------
def btn_click(item):
    '''
    Función que se encarga de mostrar el texto en el input
    '''
    input_texto.append(item)
    input_area.insert(END, str(item))

def btn_clear():
    '''
    Función que se encarga de limpiar el input
    '''
    input_texto = ""
    input_area.delete(0, END)

def btn_igual():
    '''
    Función que se encarga de realizar la operación
    '''
    if len(input_texto) == 3:
        num1 = int(input_texto[0])
        num2 = int(input_texto[2])
        operacion = input_texto[1]
        if operacion == "+":
            operacion = "suma"
        elif operacion == "-":
            operacion = "resta"
        elif operacion == "x":
            operacion = "multiplicacion"
        elif operacion == "/":
            operacion = "division"
        resultado = str(calcular(operacion, num1, num2))
    else:
        resultado = ""
    input_area.delete(0, END)
    input_area.insert(0, resultado)

# Botones 
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
dividir = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
siete = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
ocho = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nueve = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiplicar = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
cuatro = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
cinco = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
seis = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
resta = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
uno = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
dos = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
tres = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
sumar = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1) 
cero = Button(btns_frame, text = "0", fg = "black", width = 32, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 3, padx = 1, pady = 1)
igual = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_igual()).grid(row = 4, column = 3, padx = 1, pady = 1)


root.mainloop() # Este comando nos permite mostrar la ventana principal