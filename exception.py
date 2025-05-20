def main():
    midterm = [70, 92, 100]
    try:
        print(midterm[3])
    except:
        print("Something went wrong")
    x = 0
    try:
        z = 10 / x
    except ZeroDivisionError:
        print("You are dividing by zero")
    except NameError:
        print("Name error")
    else:
        print("All good")
main()