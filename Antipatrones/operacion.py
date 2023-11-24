from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division



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