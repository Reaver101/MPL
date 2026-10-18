n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Sequence:")

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1