def main():
    midterm = [70, 92, 100]
    try:
        print(midterm[2])
    except:
        print("Something went wrong")
    x = 1
    try:
        z = 10 / x
    except ZeroDivisionError:
        print("You are dividing by zero")
    except NameError:
        print("Name error")
    else:
        print("All good")
main()