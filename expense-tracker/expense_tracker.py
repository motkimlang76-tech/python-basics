expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. Show total")
    print("3. Exit")

    choice = input("Choose an option:")

    if choice == '1':
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added.")

    elif choice == '2':
        total = sum(expenses)
        print(f"Total expenses: ${total}")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")