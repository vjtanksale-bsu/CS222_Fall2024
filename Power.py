class Power(object):
    defaultExponent = 2
    def __init__(self, exponent=defaultExponent):
        self.exponent = exponent
    def of(self, x):
        if isinstance(self.exponent, int) or x >= 0:
            return x ** self.exponent
        raise ValueError("Fractional powers of negative numbers are imaginary")
def main():
    number0 = Power(3)
    number1 = Power(2.5)
    print(number1.of(1.2))
    
main()