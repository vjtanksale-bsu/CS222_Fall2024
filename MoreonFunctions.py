def LetterGrade(average = 0):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
print(LetterGrade())

def foo(z, x = 10, y = 5):
    return x + y + z

print(foo(3))

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))

