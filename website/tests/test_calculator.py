import pytest

class Calculator:
    def sum(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

def testar_soma_calculadora(): 
    calc = Calculator()

    resultado = calc.sum(1, 2)

    assert resultado != None

def test_soma_igual_a_2():
    # Arrange
    sut = Calculator()

    # Act
    result = sut.sum(sut.multiply(3, 2), 1)

    # Assert
    assert result == 7

def test_product_equals_4():
    # sut -> System Under Test
    sut = Calculator()

    # Act
    result = sut.multiply(2, 2)

    assert result == 4


def test_division_equals_4():
    # sut -> System Under Test
    sut = Calculator()

    result = sut.division(8, 2)

    assert result == 4

def test_division_by_zero_raises_error():
    # sut -> System Under Test
    sut = Calculator()

    with pytest.raises(ZeroDivisionError) as excinfo:  
        sut.division(8, 0)

    assert str(excinfo.value) == "division by zero"  
