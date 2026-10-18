n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial of", n, "is", factorial)
