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
