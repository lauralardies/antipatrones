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
```
