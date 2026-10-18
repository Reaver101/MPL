#-------------------- Experiment 1.1 --------------------
"""Aim: Personalized Greeting Generator: Write a Python program to generate a personalized greeting."""
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello,", name + "!")
print("Welcome to Python Programming.")
print("You are", age, "years old.")
print("Have a great day and enjoy learning Python!")


#-------------------- Experiment 1.2 --------------------
"""Aim: Calculating Areas of Geometric Figures: Write a Python program to calculate the areas of a circle, rectangle, and triangle."""
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


#-------------------- Experiment 1.3 --------------------
"""Aim: Developing Conversion Utilities: Develop a temperature converter between Celsius and Fahrenheit."""
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit =", fahrenheit)

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius =", celsius)

else:
    print("Invalid choice!")


#-------------------- Experiment 1.4 --------------------
"""Aim: Calculating EMI: Develop a Python program to calculate the monthly EMI for a loan based on user input."""
principal = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (%): "))
time = int(input("Enter the loan tenure (in years): "))

monthly_rate = annual_rate / (12 * 100)
months = time * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("Monthly EMI =", round(emi, 2))


#-------------------- Experiment 2.1 --------------------
"""Aim: Fibonacci Sequence Generator: Print the Fibonacci sequence using a while loop."""
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

#-------------------- Experiment 2.2 --------------------
"""Aim: Factorial Generator: Compute the factorial of a given integer."""
n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial of", n, "is", factorial)


#-------------------- Experiment 2.3 --------------------
"""Aim: Multiplication Table Generator: Generate the multiplication table of a number using loops."""
num = int(input("Enter a number: "))

print("Multiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#-------------------- Experiment 2.4 --------------------
"""Aim: Automate Payroll System: Accept employee details, calculate gross salary, PF and tax, and display net salary."""
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

da = 0.80 * basic_salary
hra = 0.40 * basic_salary

gross_salary = basic_salary + da + hra

pf = 0.12 * basic_salary

if gross_salary > 50000:
    tax = 0.05 * gross_salary
else:
    tax = 0

net_salary = gross_salary - (pf + tax)

print("\n------ Employee Payroll ------")
print("Employee ID :", emp_id)
print("Employee Name :", name)
print("Basic Salary :", basic_salary)
print("DA :", da)
print("HRA :", hra)
print("Gross Salary :", gross_salary)
print("PF :", pf)
print("Tax :", tax)
print("Net Salary :", net_salary)

#-------------------- Experiment 3.1 --------------------
"""Aim: Average Speed of Runners: Calculate the average speed of ten runners and display runners whose speed exceeds 1.5 times the average."""
speeds = []

for i in range(10):
    speed = float(input("Enter speed of Runner " + str(i + 1) + ": "))
    speeds.append(speed)

average_speed = sum(speeds) / len(speeds)

print("\nAverage Speed =", average_speed)

print("\nQualified Runners:")

for i in range(10):
    if speeds[i] > 1.5 * average_speed:
        print("Runner", i + 1, "- Speed:", speeds[i])


#-------------------- Experiment 3.2 --------------------
"""Aim: Secure Transaction Records: Store immutable transaction details using a tuple and display the record."""
# Secure Transaction Records using Tuple

# Transaction details
transaction = (
    "TXN1001",      # Transaction ID
    "Inzamamul Haque Qureshi",        # Customer Name
    25000.00,       # Amount
    "Deposit",      # Transaction Type
    "15-07-2026"    # Date
)

# Display transaction details
print("Transaction Record")
print("Transaction ID :", transaction[0])
print("Customer Name  :", transaction[1])
print("Amount         :", transaction[2])
print("Transaction Type :", transaction[3])
print("Date           :", transaction[4])


#-------------------- Experiment 3.3 --------------------
"""Aim: Check if a String is a Palindrome: Determine whether an input string is a palindrome."""
text = input("Enter a string: ")
text = text.lower()

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")


#-------------------- Experiment 3.4 --------------------
"""Aim: Library Book Management System: Use a dictionary to add, update, search, and display book records."""
library = {}

while True:
    print("\n====== Library Book Management System ======")
    print("1. Add New Book")
    print("2. Update Book Information")
    print("3. Search Book by ID")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        B_Id = input("Enter Book ID: ")

        if B_Id in library:
            print("Book ID already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            copies = int(
                input("Enter Number of Available Copies you want to add: ")
            )

            library[B_Id] = {
                "Title": title,
                "Author": author,
                "Copies": copies,
            }

            print("Book added successfully!!!")

    elif choice == "2":
        B_Id = input("Enter Book ID you want to update: ")

        if B_Id in library:
            print("Enter new details:")
            ttl = input("Enter New Title: ")
            aut = input("Enter New Author: ")
            copy = int(input("Enter New Number of Copies: "))

            library[B_Id]["Title"] = ttl
            library[B_Id]["Author"] = aut
            library[B_Id]["Copies"] = copy

            print("Book information updated successfully!!!")
        else:
            print("Book not found!")

    elif choice == "3":
        B_Id = input("Enter Book ID to search: ")

        if B_Id in library:
            print("\nBook Details")
            print("Book ID :", B_Id)
            print("Title   :", library[B_Id]["Title"])
            print("Author  :", library[B_Id]["Author"])
            print("Copies  :", library[B_Id]["Copies"])
        else:
            print("Book not found!")

    elif choice == "4":
        if not library:
            print("No books available in the library.")
        else:
            print("\nLibrary Books")
            for B_Id, details in library.items():
                print("---------------------------------")
                print("Book ID :", B_Id)
                print("Title   :", details["Title"])
                print("Author  :", details["Author"])
                print("Copies  :", details["Copies"])

    elif choice == "5":
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")


#-------------------- Experiment 4.1 --------------------
"""Aim: Prime Number Analyzer: Use a function to determine whether an input number is prime."""
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a Prime Number.")
else:
    print(number, "is not a Prime Number.")

#-------------------- Experiment 4.2 --------------------
"""Aim: Developing Conversion Utilities: Convert a measurement in inches to centimeters using a function."""
def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter length in inches: "))

cm = inch_to_cm(inch)

print("Length in centimeters =", cm)

#-------------------- Experiment 4.3 --------------------
"""Aim: Convert Inches to Centimeters: Use the map() function to convert a list of measurements from inches to centimeters."""
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

#-------------------- Experiment 4.4 --------------------
"""Aim: Sum of Digits of a Number: Use reduce() from functools to calculate the sum of a number’s digits."""
from functools import reduce

num = input("Enter a number: ")

digits = list(map(int, num))

sum = reduce(lambda x, y: x + y, digits)

print("Sum of digits =", sum)

#-------------------- Experiment 5.1 --------------------
"""Aim: Basic Exception Handling: Demonstrate five types of exception handling in Python."""
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

#-------------------- Experiment 5.2 --------------------
"""Aim: Custom Exceptions: Simulate a banking withdrawal system with custom exceptions for invalid account numbers and insufficient funds."""
class InsufficientBalance(Exception):
    pass

class InvalidAccount(Exception):
    pass

account_no = 12345
balance = 10000

acc = int(input("Enter account number: "))
amount = int(input("Enter amount to withdraw: "))

try:
    if acc != account_no:
        raise InvalidAccount

    if amount > balance:
        raise InsufficientBalance

    balance = balance - amount

    print("Withdrawal Successful")
    print("Remaining Balance =", balance)

except InvalidAccount:
    print("Invalid Account Number")

except InsufficientBalance:
    print("Insufficient Balance")

#-------------------- Experiment 7.1 --------------------
"""Aim: Online Shopping System: Develop classes for products and shopping carts, including adding items and calculating total cost."""
class Product: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart: 
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print(product.name, "Added to cart.")

    def total_cost(self):
        total = 0

        for product, quantity in self.items:
            total = total + product.price * quantity

        return total

    def display_cart(self): 
        print("\nItems in cart: ")

        for product, quantity in self.items: 
            print(product.name, " ", quantity)

        print("Total Cost =", self.total_cost())

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)
p3 = Product("Keyboard", 500)

cart = ShoppingCart()

cart.add_item(p1, 1)
cart.add_item(p2, 2)
cart.add_item(p3, 3)

cart.display_cart()


#-------------------- Experiment 7.2 --------------------
"""Aim: Vehicle Rental System: Use classes to manage vehicles, availability, rental pricing, and rental operations."""
class Vehicle: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.available = True

class RentalAgency: 
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(vehicle.name, "Added to agency")

    def display_vehicles(self):
        print("\nAvailable vehicles: ")

        for vehicle in self.vehicles:
            if vehicle.available:
                print(vehicle.name, "-", vehicle.price, "Per day")

    def rent_vehicle(self, vehicle, customer, days):
        if vehicle.available:
            vehicle.available = False

            total = vehicle.price * days

            print("\nRental Successful")
            print("Customer: ", customer)
            print("Vehicle: ", vehicle.name)
            print("Rental period:", days, " days")
            print("Total Price =", total)
        else: 
            print(vehicle.name, "is not available")

car1 = Vehicle("F1 Redbull", 1000000)
car2 = Vehicle("Ferrari carrera", 200000)
car3 = Vehicle("Porsche 911", 400000)
car4 = Vehicle("Lamborghini", 25)

agency = RentalAgency()

agency.add_vehicle(car1)
agency.add_vehicle(car2)
agency.add_vehicle(car3)
agency.add_vehicle(car4)

agency.display_vehicles()


#-------------------- Experiment 7.3 --------------------
"""Aim: Area of Triangle: Create a Polygon class to input and display sides, inherit Triangle from Polygon, and calculate the triangle’s area."""
class Polygon:
    def input_sides(self):
        self.sides = []
        n = int(input("Enter the number of sides: "))

        for i in range(n):
            side = float(input(f"Enter side {i + 1}: "))
            self.sides.append(side)

    def display_sides(self):
        print("Sides of the polygon are:", self.sides)


class Triangle(Polygon):
    def area(self):
        a, b, c = self.sides

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print("Area of the triangle:", area)


t = Triangle()

t.input_sides()
t.display_sides()
t.area()


#-------------------- Experiment 8.1 --------------------
"""Aim: Online Course Management System: Use a Student base class and Undergraduate/Postgraduate subclasses with overridden display_info() methods."""
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


class UgStudent(Student):
    def __init__(self, name, age, course, semester):
        super().__init__(name, age, course)
        self.semester = semester

    def display_info(self):
        super().display_info()
        print("Semester:", self.semester)


class PgStudent(Student):
    def __init__(self, name, age, course, thesis_topic):
        super().__init__(name, age, course)
        self.thesis = thesis_topic

    def display_info(self):
        super().display_info()
        print("Thesis Topic:", self.thesis)


student1 = UgStudent(
    "Shinchan",
    20,
    "B.Tech Data Science",
    4
)

student2 = PgStudent(
    "Nobita",
    21,
    "B.Tech Computer Engineering",
    "Artificial Intelligence"
)


print("Undergraduate students:")
student1.display_info()

print("\nPostgraduate Student:")
student2.display_info()



#-------------------- Experiment 9.1 --------------------
"""Aim: Use regular expressions to extract email addresses and ten-digit phone numbers from a text file."""
import re 

file = open("EXP9/data(exp9).txt", "r")

text = file.read()

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

phone_numbers = re.findall(r'\b\d{10}\b', text)

print("Email Addresses: ")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phone_numbers:
    print(phone)

file.close()


#-------------------- Experiment 9.2 --------------------
"""Aim: Use the re module to find lines beginning with This, case-insensitive matches, occurrences of te, words starting with s and ending with e, and dates in the specified format."""
import re

file = open("EXP9/text.txt", "r")
lines = file.readlines()

print("1. Lines starting with This:")
for line in lines:
    if re.search(r'^This', line):
        print(line.strip())

print("\n2. Lines starting with This or this:")
for line in lines:
    if re.search(r'^this', line, re.IGNORECASE):
        print(line.strip())

print("\n3. Lines containing consecutive te:")
for line in lines:
    if re.search(r'te', line):
        print(line.strip())

print("\n4. Words starting with s and ending with e:")
for line in lines:
    words = re.findall(r'\bs\w*e\b', line, re.IGNORECASE)
    for word in words:
        print(word)

print("\n5. Dates:")
for line in lines:
    dates = re.findall(r'\b\d{1,2}\.\d{1,2}\.\d{2}\b', line)
    for date in dates:
        print(date)

file.close()


#-------------------- Experiment 10.1 --------------------
"""Aim: GUI for Developing Conversion Utilities: Develop a GUI for currency, temperature, and length conversions."""
import tkinter as tk

def convert():
    value = float(entry.get())
    choice = conversion.get()

    if choice == "Rupees to Dollars":
        result = value / 85
        label_result.config(text="Result = " + str(result) + " Dollars")

    elif choice == "Celsius to Fahrenheit":
        result = (value * 9 / 5) + 32
        label_result.config(text="Result = " + str(result) + " Fahrenheit")

    elif choice == "Inches to Feet":
        result = value / 12
        label_result.config(text="Result = " + str(result) + " Feet")


window = tk.Tk()
window.title("Conversion Utilities")
window.geometry("400x300")

label_title = tk.Label(window, text="Conversion Utilities")
label_title.pack()

label_value = tk.Label(window, text="Enter value:")
label_value.pack()

entry = tk.Entry(window)
entry.pack()

conversion = tk.StringVar()
conversion.set("Rupees to Dollars")

option = tk.OptionMenu(
    window,
    conversion,
    "Rupees to Dollars",
    "Celsius to Fahrenheit",
    "Inches to Feet"
)
option.pack()

button = tk.Button(window, text="Convert", command=convert)
button.pack()

label_result = tk.Label(window, text="Result = ")
label_result.pack()

window.mainloop()

#-------------------- Experiment 10.2 --------------------
"""Aim: College Admission Registration Form: Create a GUI form to collect and display students’ personal, educational, and contact information."""
import tkinter as tk

def submit():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()
    email = entry_email.get()
    phone = entry_phone.get()

    result = "Name: " + name
    result = result + "\nAge: " + age
    result = result + "\nCourse: " + course
    result = result + "\nEmail: " + email
    result = result + "\nPhone: " + phone

    label_result.config(text=result)


window = tk.Tk()
window.title("College Admission Registration")
window.geometry("450x450")

tk.Label(window, text="College Admission Registration").pack()

tk.Label(window, text="Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Age:").pack()
entry_age = tk.Entry(window)
entry_age.pack()

tk.Label(window, text="Course:").pack()
entry_course = tk.Entry(window)
entry_course.pack()

tk.Label(window, text="Email:").pack()
entry_email = tk.Entry(window)
entry_email.pack()

tk.Label(window, text="Phone:").pack()
entry_phone = tk.Entry(window)
entry_phone.pack()

button = tk.Button(window, text="Submit", command=submit)
button.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()

#-------------------- Experiment 11.1 --------------------
"""Aim: Meteorological Temperature Data: Create 1D, 2D, and 3D NumPy arrays and perform indexing, slicing, and reshaping."""
import numpy as np

daily_temp = np.array([30, 32, 31, 33, 34, 32, 35])

print("1D Array - Daily Temperature:")
print(daily_temp)

print("\nTemperature on 3rd day:", daily_temp[2])

print("Temperature from 2nd to 5th day:", daily_temp[1:5])


city_temp = np.array([
    [30, 32, 31, 33, 34],
    [25, 27, 26, 28, 29],
    [35, 36, 34, 37, 38]
])

print("\n2D Array - Temperature of Cities:")
print(city_temp)

print("\nTemperature of first city on 2nd day:", city_temp[0][1])

print("Temperature readings of first city:", city_temp[0, :])


reshaped = city_temp.reshape(5, 3)

print("\nReshaped 2D Array:")
print(reshaped)


weekly_temp = np.array([
    [
        [30, 31, 32],
        [25, 26, 27]
    ],
    [
        [33, 34, 35],
        [28, 29, 30]
    ]
])

print("\n3D Array - Temperature for Different Weeks:")
print(weekly_temp)

print("\nTemperature:", weekly_temp[0][1][2])

print("Temperature data of first week:")
print(weekly_temp[0])

new_shape = weekly_temp.reshape(3, 2, 2)

print("\nReshaped 3D Array:")
print(new_shape)

#-------------------- Experiment 11.2 --------------------
"""Aim: Create a weekly calendar containing seven entries, each with the day, date, and activity."""
calendar = []

calendar.append({
    "Day": "Monday",
    "Date": 1,
    "Activity": "Python Lab"
})

calendar.append({
    "Day": "Tuesday",
    "Date": 2,
    "Activity": "Data Structures"
})

calendar.append({
    "Day": "Wednesday",
    "Date": 3,
    "Activity": "DBMS"
})

calendar.append({
    "Day": "Thursday",
    "Date": 4,
    "Activity": "Statistics"
})

calendar.append({
    "Day": "Friday",
    "Date": 5,
    "Activity": "FDS Lab"
})

calendar.append({
    "Day": "Saturday",
    "Date": 6,
    "Activity": "Python Practice"
})

calendar.append({
    "Day": "Sunday",
    "Date": 7,
    "Activity": "Holiday"
})

print("Weekly Calendar")

for day in calendar:
    print("----------------------")
    print("Day:", day["Day"])
    print("Date:", day["Date"])
    print("Activity:", day["Activity"])


#-------------------- Experiment 12.1 --------------------
"""Aim: Using the Iris dataset: display the first eight rows and column names, fill missing values with column means, remove rows with missing values, group by species, and calculate mean, minimum, and maximum sepal length."""
import pandas as pd

data = pd.read_csv("EXP12/Iris.csv")

print("First 8 rows:")
print(data.head(8))


print("\nColumn Names:")
print(data.columns)


data_filled = data.copy()

data_filled["SepalLengthCm"] = data_filled["SepalLengthCm"].fillna(
    data_filled["SepalLengthCm"].mean()
)

data_filled["SepalWidthCm"] = data_filled["SepalWidthCm"].fillna(
    data_filled["SepalWidthCm"].mean()
)

data_filled["PetalLengthCm"] = data_filled["PetalLengthCm"].fillna(
    data_filled["PetalLengthCm"].mean()
)

data_filled["PetalWidthCm"] = data_filled["PetalWidthCm"].fillna(
    data_filled["PetalWidthCm"].mean()
)

print("\nData after filling missing values:")
print(data_filled)


data_removed = data.dropna()

print("\nData after removing rows with missing values:")
print(data_removed)


grouped_data = data.groupby("Species")

print("\nData grouped by Species:")
for species, group in grouped_data:
    print("\n", species)
    print(group)


mean_value = data["SepalLengthCm"].mean()
min_value = data["SepalLengthCm"].min()
max_value = data["SepalLengthCm"].max()

print("\nSepal Length Statistics:")
print("Mean =", mean_value)
print("Minimum =", min_value)
print("Maximum =", max_value)