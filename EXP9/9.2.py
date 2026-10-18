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
