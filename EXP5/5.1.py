try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division =", a / b)

    l = [10, 20, 30]
    print(l[5])

    print(x)

    c = "Hello" + 10
    print(c)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter only numbers.")

except IndexError:
    print("List index is out of range.")

except NameError:
    print("Variable is not defined.")

except TypeError:
    print("Cannot perform operation on different data types.")