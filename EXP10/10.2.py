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