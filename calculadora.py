#!/usr/bin/python3

import sys

def suma (oper1, oper2):
    return oper1 + oper2

def resta (oper1, oper2):
    return oper1 - oper2
    
def multiplicacion (oper1, oper2):
    return oper1 * oper2
    
def division (oper1, oper2):
    try:
        return oper1 / oper2
    except ZeroDivisionError:
        return ("No puedo dividir entre cero")

funciones = {
       "suma" : suma,
       "resta" : resta,
       "multiplicacion" : multiplicacion,
       "division" : division
}

if __name__ == "__main__":

    Num_args = 4
    
    if len(sys.argv) != Num_args:
        sys.exit("usage : [operador][num1][num2]")
        
    try:
        operador = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except IndexError:
        sys.exit("usage : [operador][num1][num2]")
    except ValueError:
        sys.exit("El argumento 1 y 2 tienen que ser de tipo numerico")
        
    try:
        resultado = funciones[operador](num1, num2)
    except KeyError:
        sys.exit("No existe la funcion" + operador)
        
    print (resultado)
    
 
 
        
