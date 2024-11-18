contacts = {}


def add_contact(name, phone, email):
    if name in contacts:
        print(f"Contact '{name}' already exists!")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' added successfully!")


def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts available!")


def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found!")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")


if __name__ == "__main__":
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")
