"""
Exercício

Implementar uma calculadora com as quatro operações básicas (adição, subtraç, multiplicação e divisão) e escrever, para cada operação, 3 casos de testes.
Na divisão, incluir a divisão por zero.
"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b
