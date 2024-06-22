def add_contact(phone_book, name, phone_number, email):
    if name in phone_book:
        print(f"Contact {name} already exists.")
    else:
        phone_book[name] = {'phone_number': phone_number, 'email': email}
        print(f"Contact {name} added.")

def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def search_contact(phone_book, name):
    if name in phone_book:
        contact = phone_book[name]
        print(f"Contact found: {name} -> Phone: {contact['phone_number']}, Email: {contact['email']}")
    else:
        print(f"Contact {name} not found.")

def display_contacts(phone_book):
    if phone_book:
        print("\n\nPhone Book Contacts:\n")
        print("{:<20} {:<15} {:<30}".format('Name', 'Phone Number', 'Email'))
        print("="*65)
        for name, details in phone_book.items():
            print("{:<20} {:<15} {:<30}".format(name, details['phone_number'], details['email']))
    else:
        print("Phone book is empty.")

def phone_book_app():
    # Initialize phone book with some pre-existing contacts
    phone_book = {
        'Alice': {'phone_number': '123-456-7890', 'email': 'alice@example.com'},
        'Bob': {'phone_number': '234-567-8901', 'email': 'bob@example.com'},
        'Charlie': {'phone_number': '345-678-9012', 'email': 'charlie@example.com'}
    }
    
    # Display initial contacts
    print("\n\n\t\tInitial Phone Book Contacts\n\n")
    display_contacts(phone_book)
    
    while True:
        print("\n\nPhone Book Menu:\n")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("\n\nEnter your choice : ")
        
        if choice == 'add':
            name = input("Enter name : ")
            phone_number = input("Enter phone number : ")
            email = input("Enter email : ")
            add_contact(phone_book, name, phone_number, email)
        elif choice == 'delete':
            name = input("Enter name to delete : ")
            delete_contact(phone_book, name)
        elif choice == 'search':
            name = input("Enter name to search : ")
            search_contact(phone_book, name)
        elif choice == 'display':
            display_contacts(phone_book)
        elif choice == 'exit':
            print("Exiting phone book application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the phone book application
phone_book_app()

