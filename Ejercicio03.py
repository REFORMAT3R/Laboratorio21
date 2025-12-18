class OperadorInvalido(Exception):
    pass

def calcular(operacion):
    try:
        # Separar la operación
        partes = operacion.split()

        if len(partes) != 3:
            raise ValueError("La operación debe tener el formato: numero operador numero")

        num1_str, operador, num2_str = partes

        # Convertir a float
        num1 = float(num1_str)
        num2 = float(num2_str)

        # Validar operador y realizar operación
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            raise OperadorInvalido(f"Operador inválido: {operador}")

        return resultado

    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero"

    except ValueError:
        return "Error: los valores ingresados no son números válidos"

    except OperadorInvalido as e:
        return f"Error: {e}"

print(calcular("10 / 2"))
print(calcular("10 / 0"))
print(calcular("10 a 2"))
print(calcular("diez + 2"))