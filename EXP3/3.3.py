text = input("Enter a string: ")
text = text.lower()

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")
