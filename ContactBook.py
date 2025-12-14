contacts = []

def add_contact():
    print("\n------------ADD NEW CONTACT-------------")
    name = input("NAME: ")
    phone = input("PHONE NUMBER: ")
    email = input("EMAIL: ")
    address = input("ADDRESS: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("\nContact added successfully!")
    input("\nPress Enter to return to menu...")

def view_contacts():
    print("\n--------------CONTACT LIST-------------")
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} - {c['phone']}")
    input("\nPress Enter to return to menu...")

def search_contact():
    print("\n-------------SEARCH CONTACT--------------")
    search = input("Enter name or phone to search: ").lower()
    found = False

    for c in contacts:
        if search in c['name'].lower() or search in c['phone']:
            print("\nContact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True

    if not found:
        print("Contact not found.")

    input("\nPress Enter to return to menu...")

def update_contact():
    print("\n---------------- UPDATE CONTACT-----------------")
    phone = input("Enter phone number of contact to update: ")

    for c in contacts:
        if c['phone'] == phone:
            print("Leave blank to keep current value")

            name = input(f"New Name ({c['name']}): ")
            email = input(f"New Email ({c['email']}): ")
            address = input(f"New Address ({c['address']}): ")

            if name:
                c['name'] = name
            if email:
                c['email'] = email
            if address:
                c['address'] = address

            print("\nContact updated successfully!")
            input("\nPress Enter to return to menu...")
            return

    print("Contact not found.")
    input("\nPress Enter to return to menu...")

def delete_contact():
    print("\n---------------DELETE CONTACT-----------------")
    phone = input("Enter phone number of contact to delete: ")

    for c in contacts:
        if c['phone'] == phone:
            contacts.remove(c)
            print("\nContact deleted successfully!")
            input("\nPress Enter to return to menu...")
            return

    print("Contact not found.")
    input("\nPress Enter to return to menu...")

def menu():
    while True:
        print("\n============= Contact Management System =============")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\nExiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

menu()
