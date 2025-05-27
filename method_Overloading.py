class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))       # Single argument
print(calc.add(2, 3))    # two arguments
print(calc.add(2, 3, 4)) # three arguments