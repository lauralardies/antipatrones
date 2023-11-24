from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division



def calcular(operacion, num1, num2):
    try:
        if operacion == "suma":
            return suma(num1, num2)
        elif operacion == "resta":
            return resta(num1, num2)
        elif operacion == "multiplicacion":
            return multiplicacion(num1, num2)
        elif operacion == "division":
            return division(num1, num2)
        else:
            raise ValueError("Operacion no valida")
    except ValueError as e:
        print(e)
        return None