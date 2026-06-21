def show_menu():
    print("\nContact Book")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    print("Contact added.")


def show_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
    else:
        print("\nYour contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']}: {contact['phone']}")


def search_contact(contacts):
    keyword = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True

    if not found:
        print("Contact not found.")


def delete_contact(contacts):
    if not contacts:
        print("No contacts to delete.")
        return

    show_contacts(contacts)

    try:
        number = int(input("Enter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        deleted_contact = contacts[number - 1]
        del contacts[number - 1]
        print(f"Deleted contact: {deleted_contact['name']}")

    except ValueError:
        print("Please enter a valid number.")


contacts = []

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")