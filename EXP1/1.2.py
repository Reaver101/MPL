print("Choose a shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius * radius
    print("Area of the Circle =", area)

elif choice == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("Area of the Rectangle =", area)

elif choice == 3:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print("Area of the Triangle =", area)

else:
    print("Invalid choice! Please enter a number between 1 and 3.")
