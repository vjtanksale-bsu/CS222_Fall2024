def multiply(x, y):
    return x * y

def factorial(n):
    if n < 0:
        raise ValueError("Factorial does not exist for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def IsEven(n):
    return n % 2 == 0