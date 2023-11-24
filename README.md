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
3. **Falta de modularidad**. Cada función debe de tener una sola responsabilidad. Sin embargo, en el código proporcionado vemos que una sola función se encarga de hacer la suma, resta, multimplicación, etc. En resumen, en nuestro código tenemos una sola función que se encarga de todo, por lo que deberíamos separarlo en funciones diferentes.


## Código
