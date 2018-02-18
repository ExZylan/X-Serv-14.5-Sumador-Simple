#!/usr/bin/python3

import sys 


def suma(op1, op2):
    return op1+op2

def resta(op1, op2):
    return op1-op2

def mult(op1, op2):
    return op1*op2

def div(op1, op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        return("No intentes dividir entre 0")


funciones = {
    "suma": suma,
    "resta": resta,
    "mult": mult,
    "div": div,
}

if __name__ == "__main__":

    NUM_ARG = 4

    if len(sys.argv) != NUM_ARG:
         sys.exit("Error. Uso: python3 calculadora.py funcion operando1 operando2")
    
    try:
        op1 = float(sys.argv[2])
        op2 = float(sys.argv[3])
    except ValueError:
        print ("No es posible operar con chars")
        sys.exit()


    funcion = sys.argv[1]

    try:
        resultado = funciones[funcion](op1,op2)
    except KeyError:
        sys.exit("No existe la funcion "+ funcion)
    print(resultado)