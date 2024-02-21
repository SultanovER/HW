class Calculator:
    def __init__(self, numer):
        self.numer = numer

    def __add__(self, other):
        print(f'{self.numer}+{other.numer}={self.numer + other.numer}')

    def __sub__(self, other):
        print(f'{self.numer}-{other.numer}={self.numer - other.numer}')

    def __mul__(self, other):
        print(f'{self.numer}*{other.numer}={self.numer * other.numer}')

    def __truediv__(self, other):
        print(f'{self.numer}/{other.numer}={self.numer // other.numer}')


number1 = Calculator(10)
number2 = Calculator(5)
number1.__add__(number2)
number1.__sub__(number2)
number1.__mul__(number2)
number1.__truediv__(number2)

