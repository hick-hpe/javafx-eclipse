from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(1, 2) == 3
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 0) == 0
    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5
    assert multiplicar(0, 10) == 0

def test_dividir():
    assert dividir(6, 2) == 3
    assert dividir(-10, 2) == -5
    try:
        dividir(5, 0)
    except ZeroDivisionError as e:
        assert str(e) == "Divisão por zero não é permitida."

