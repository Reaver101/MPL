def convert(x):
    return x * 2.54

n = int(input("Enter the number of measurements: "))

inch = []

for i in range(n):
    value = float(input("Enter measurement in inches: "))
    inch.append(value)

cm = list(map(convert, inch))

print("Measurements in centimeters:")
print(cm)