def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("No se puede dividir por cero")