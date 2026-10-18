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
