# Antipatrones

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/antipatrones)
https://github.com/lauralardies/antipatrones

## Enunciado

Dada una porción de código Python escrita en estilo "Spaghetti Code", se te pide que identifiques las principales características de este antipatrón y refactorices el código para mejorar su legibilidad y mantenibilidad.

Considera el siguiente fragmento de código:

```
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
```

## Identificación de características de "Spaghetti Code"

El código proporcionado en la sección anterior muestra algunas características típicas del estilo de programación conocido como "Spaghetti Code". Algunas de las características principales que hemos podido identificar son las siguientes:

1. **Uso excesivo de `if`**. Se emplean muchas sentencias `if`, lo puede dificultar la lectura y comprensión del código. Para mejorar el código, deberíamos acompañar a las sentencias `if` con `else if`.
2. **Mal manejo de errores**. En vez de elevar excepciones para manejar los errores, simplemente se imprimen mensajes de error (otra cosa que nunca se debería hacer, hacer `print` en una función). Por lo tanto, podrá haber complicaciones a la hora de buscar y gestionar errores. Por otro lado, simplemente mostrar el error en pantalla puede hacer más difícil la gestión y el control de errores en el código.
3. **Falta de modularidad**. Cada función debe de tener una sola responsabilidad. Sin embargo, en el código proporcionado vemos que una sola función se encarga de hacer la suma, resta, multimplicación, etc. En resumen, en nuestro código tenemos una sola función que se encarga de todo, por lo que deberíamos separarlo en funciones diferentes. Este cambio nos aportará un código mucho más legible y reutilizable.

## Archivos

Todos los archivos se encuentran dentro de una carpeta llamada `Antipatrones` y esta contiene a su vez:
- Otra carpeta llamada `Operaciones`, donde almacenamos todos los archivos en los que creamos funciones encargadas de hacer las operaciones suma (en `suma.py`), resta (en `resta.py`), multiplicación (en `multiplicacion.py`) y división (en `division.py`).
- Archivo `operacion.py` donde llamamos a las operaciones indicadas por el usuario.
- Archivo `main.py` desde el cual creamos la interfaz de usuario que representa una calculadora interactiva.
- Archivo `run.py` que se trata del lanzador del programa.

## Código

### Archivo `suma.py`
```
def suma(num1, num2):
    '''
    Función que se encarga de sumar dos números
    '''
    return num1 + num2
```

### Archivo `resta.py`
```
def resta(num1, num2):
    '''
    Función que se encarga de restar dos números
    '''
    return num1 - num2
```

### Archivo `multiplicacion.py`
```
def multiplicacion(num1, num2):
    '''
    Función que se encarga de multiplicar dos números
    '''
    return num1 * num2
```

### Archivo `division.py`
```
def division(num1, num2):
    '''
    Función que se encarga de dividir dos números
    '''
    if num2 != 0:
        return num1 / num2
    else: # Si el divisor es cero, lanzamos una excepción
        raise ValueError("No se puede dividir por cero")
```

### Archivo `operacion.py`
```
from Operaciones.suma import suma
from Operaciones.resta import resta
from Operaciones.multiplicacion import multiplicacion
from Operaciones.division import division



def calcular(operacion, num1, num2):
    try: # Intentamos realizar la operación
        if operacion == "suma":
            return suma(num1, num2) # Hemos creado una función suma que solo tiene la responsabilidad de sumar
        elif operacion == "resta":
            return resta(num1, num2) # Hemos creado una función resta que solo tiene la responsabilidad de restar
        elif operacion == "multiplicacion":
            return multiplicacion(num1, num2) # Hemos creado una función multiplicacion que solo tiene la responsabilidad de multiplicar
        elif operacion == "division":
            return division(num1, num2) # Hemos creado una función division que solo tiene la responsabilidad de dividir
        else:
            raise ValueError("Operacion no valida") # Si la operación no es ninguna de las anteriores, lanzamos una excepción para controlar el error
    except ValueError as e: # Capturamos la excepción en caso de que no se pueda dividir por cero
        print(e)
        return None # Devolvemos None en caso de que no se pueda realizar la operación
```

### Archivo `main.py`
```
from tkinter import *
from operacion import calcular

def main():
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
        input_texto = []
        input_area.delete(0, END)

    def btn_igual():
        '''
        Función que se encarga de realizar la operación
        '''
        texto = input_texto[-3:]
        num1 = int(texto[0])
        num2 = int(texto[2])
        operacion = texto[1]
        if operacion == "+":
            operacion = "suma"
        elif operacion == "-":
            operacion = "resta"
        elif operacion == "x":
            operacion = "multiplicacion"
        elif operacion == "/":
            operacion = "division"
        resultado = str(calcular(operacion, num1, num2))
        input_area.delete(0, END)
        input_area.insert(0, resultado)

    # Botones 
    clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
    dividir = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
    siete = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
    ocho = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
    nueve = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
    multiplicar = Button(btns_frame, text = "x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("x")).grid(row = 1, column = 3, padx = 1, pady = 1)
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
```

### Archivo `run.py`
```
from main import main

if __name__ == '__main__':
    main()
```
