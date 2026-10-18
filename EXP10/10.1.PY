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