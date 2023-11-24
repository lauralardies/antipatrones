def division(num1, num2):
    '''
    Función que se encarga de dividir dos números
    '''
    if num2 != 0:
        return num1 / num2
    else: # Si el divisor es cero, lanzamos una excepción
        raise ValueError("No se puede dividir por cero")