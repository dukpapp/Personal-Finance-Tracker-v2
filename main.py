from matplotlib import pyplot as plt
from database import add_transaction, get_transaction_data, get_transactions
from data_entry import get_amount, get_category, get_date, get_description

def add():
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    add_transaction(date, amount, category, description)

def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions within a date range")
        print("3. Visualize transactions")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1": 
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            get_transactions(start_date, end_date)
        elif choice == "3":
            plot_transactions()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")

def plot_transactions():
    data = get_transaction_data()
    
    if not data:
        return

    dates = data["dates"]
    amounts = data["amounts"]
    categories = data["categories"]

    income = [amounts[i] if categories[i] == "Income" else 0 for i in range(len(dates))]
    expenses = [amounts[i] if categories[i] == "Expense" else 0 for i in range(len(dates))]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, income, label="Income", color="green", marker="o")
    plt.plot(dates, expenses, label="Expenses", color="red", marker="o")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
