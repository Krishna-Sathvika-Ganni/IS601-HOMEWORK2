'''Calculator Test'''

from calculator import Calculator

def test_addition(): # Addition function    
    assert Calculator.add(3,4) == 7

def test_subtraction(): # Subtraction function    
    assert Calculator.subtract(3,2) == 1

def test_multiply(): # Multiplication function    
    assert Calculator.multiply(3,3) == 9

def test_divide():  # Division function    
    assert Calculator.divide(4,2) == 2