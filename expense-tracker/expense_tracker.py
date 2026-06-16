expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nAll Expenses:")
            for expense in expenses:
                print(f"- {expense['category']}: ${expense['amount']}")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Total expenses: ${total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
