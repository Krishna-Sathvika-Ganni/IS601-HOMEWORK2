'''Importing functions from operations file'''

from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation  # Operation function is stored

    def get_result(self):
        return self.operation(self.x, self.y) #Calling the stored operation with x and y

class Calculator:
    @staticmethod
    def add(x,y):
        calculation = Calculation(x, y, add) 
        # Passing the addition function from calculator.operations 
        return calculation.get_result()
    @staticmethod
    def subtract(x,y):
        calculation = Calculation(x, y, subtract)  
        # Passing the subtraction function from calculator.operations 
        return calculation.get_result()
    @staticmethod
    def multiply (x,y):
        calculation = Calculation(x, y, multiply) 
        # Passing the multiplication function from calculator.operations  
        return calculation.get_result()
    @staticmethod
    def divide(x,y):
        calculation = Calculation(x, y, divide) 
        # Passing the division function from calculator.operations  
        return calculation.get_result()
    
# End
