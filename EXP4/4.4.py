from functools import reduce

num = input("Enter a number: ")

digits = list(map(int, num))

sum = reduce(lambda x, y: x + y, digits)

print("Sum of digits =", sum)