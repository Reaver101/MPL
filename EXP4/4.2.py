def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter length in inches: "))

cm = inch_to_cm(inch)

print("Length in centimeters =", cm)