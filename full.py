#-----------------------------------------------------7.1--------------------------------------------------
"""
Aim: Online Shopping System: Develop classes for products, customers, and shopping carts. Include methods for adding items to the cart, calculating total costs, processing orders, and managing inventory.
"""
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

#-----------------------------------------------------7.2--------------------------------------------------
"""
Aim: Vehicle Rental System: Design a system using classes for vehicles, rental agencies, and rental transactions. Implemented methods to handle vehicle availability, rental periods, pricing, and customer bookings.
"""
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

#-----------------------------------------------------7.3--------------------------------------------------
"""
Aim: Area of Triangle: Write a Python class named polygon with two methods: input sides and display sides. Inherit a Class Triangle from the polygon and calculate the area of a triangle.
"""
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

#-----------------------------------------------------8.1--------------------------------------------------
"""
Aim: Online Course Management System: Consider an Online Course Management system with a base class named Student, which includes essential attributes such as name, age, and course to represent a student's basic details. From this base class, two specialized classes are derived:
UndergraduateStudent and PostgraduateStudent. 
The UndergraduateStudent class extends the functionality of the base class by adding a semester attribute, representing the current semester of study. Similarly, the PostgraduateStudent class introduces a thesis_topic attribute, which stores the research focus of the student.
Each of these subclasses overrides the display_info() method to include their additional attributes while still utilizing the base class’s functionality.
"""
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

#-----------------------------------------------------9.1--------------------------------------------------
"""
Aim: Write a Python program to extract all valid email addresses and phone numbers from a given text file using pattern-matching techniques with regular expressions.
"""

"""
data(exp9).txt:

Student Contact Information

Name: Rahul Sharma
Email: rahul@gmail.com
Phone: 9876543210

Name: Priya Singh
Email: priya.singh@yahoo.com
Phone: 9123456789

Name: Amit Kumar
Email: amit.kumar@outlook.com
Phone: 9988776655

Name: Sneha Patel
Email: sneha.patel@gmail.com
Phone: 8765432109

"""
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

#-----------------------------------------------------10.1--------------------------------------------------
"""
Aim: GUI for Developing Conversion Utilities: Develop a Python GUI application that performs various unit conversions such as currency (Rupees to Dollars),
temperature (Celsius to Fahrenheit), and length (Inches to Feet). The application should include input fields for the values, dropdown menus or buttons to select the type of conversion, and labels to display the results.
"""
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

#-----------------------------------------------------11.1--------------------------------------------------
"""
Aim: A meteorological department records temperature data in different cities. You need to store and analyze this data efficiently using NumPy arrays. Create 1D, 2D, and 3D NumPy arrays to store temperature data.
Perform reshaping, slicing, and indexing operations on the arrays. Consider a 1D array that represents daily temperature readings 2D array stores temperature 
readings for multiple cities, and a 3D array represents data for different weeks.
"""
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

#-----------------------------------------------------12.1--------------------------------------------------
"""
Aim: Using the Iris Data (https://www.kaggle.com/datasets/saurabh00007/iriscsv), perform the following tasks:
i) Read the first 8 rows of the dataset.
ii) Display the column names of the Iris dataset.
iii) Fill any missing data with the mean value of the
respective column.
iv) Remove rows that contain any missing values.
v) Group the data by the species of the flower.
vi) Calculate and display the mean, minimum, and maximum values of the Sepal length column.
"""

"""
Download iris.csv from:
https://www.kaggle.com/datasets/saurabh00007/iriscsv
"""
import pandas as pd

data = pd.read_csv("Iris.csv")

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