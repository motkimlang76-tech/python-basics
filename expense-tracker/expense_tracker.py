import json

FILE_NAME = "expenses.json"

try:
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
except json.JSONDecodeError:
    expenses = []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=2)


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
        save_expenses()
        print("Expense added and saved.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nAll Expenses:")
            for expense in expenses:
                print(f"- {expense['category']}: ${expense['amount']:.2f}")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Total expenses: ${total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")