''' Calculator test'''

from calculator.operations import add, multiply, subtract, divide

def test_addition(): # Addition function     
    assert add(3,4) == 7

def test_subtraction():  #Subtraction function 
    assert subtract(3,2) == 1

def test_multiplication():   # Multiplication function
    assert multiply(3,3) == 9

def test_division():  # Division function
    assert divide(4,2) == 2