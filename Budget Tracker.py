#Budget Tracker Attempt

import pickle
import matplotlib.pyplot as plt

class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        return sum(t.amount for t in self.transactions)

    def get_expenses_by_description(self):
        descriptions = {}
        for t in self.transactions:
            if t.amount < 0:
                if t.description not in descriptions:
                    descriptions[t.description] = 0
                descriptions[t.description] += t.amount
        return descriptions

    def get_total_earnings(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    def generate_report(self):
        print("Balance:", self.get_balance())
        print("Expenses by description:")
        for description, total in self.get_expenses_by_description().items():
            print(f"{description}: {total}")

    def save_to_file(self, filename):  # we are using pickle to save our data.
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self.transactions, f)
            print(f"Data has been saved to '{filename}'.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def load_from_file(self, filename):  # loading our old data
        try:
            with open(filename, 'rb') as f:
                self.transactions = pickle.load(f)
        except FileNotFoundError:    # to fix file related issues.
            print("No previous data found. Starting fresh.")
        except pickle.PickleError:
            print("Error loading data. The file might be corrupted.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def reset(self):       # resets memory
        self.transactions = []
        print("All transactions have been reset.")

    def plot_expenses_pie_chart(self):   # pie chart so we get a clearer look at how we spent the money.
        expenses = self.get_expenses_by_description()
        total_earnings = self.get_total_earnings()
        total_expenses = sum(expenses.values())
        savings = total_earnings + total_expenses  # Expenses are negative, so we add them.  Earning + (-Expenses).


        if not expenses and savings == 0:
            print("No expenses or savings to display.")
            return

        if savings > 0:
            expenses["Savings"] = savings  # Remaining money shows up as savings.

        descriptions = list(expenses.keys())
        amounts = [abs(amount) for amount in expenses.values()]  # Use absolute values for display

        plt.figure(figsize=(10, 7))
        plt.pie(amounts, labels=descriptions, autopct=lambda p: f'{p:.1f}%\n({p*sum(amounts)/100:.2f})', startangle=140)
        plt.title('Expenses and Savings Breakdown')
        plt.show()

def main():
    tracker = BudgetTracker()

    # Load data from file
    tracker.load_from_file("budget_data.pkl")

    while True:
        print("\n1. Input Monthly Earnings")
        print("2. Input Expense")
        print("3. View Balance")
        print("4. Generate Report")
        print("5. Reset Data")
        print("6. Show Expenses Pie Chart")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter your monthly earnings: "))
                if amount <= 0:
                    print("Earnings should be a positive number.")
                    continue
                tracker.add_transaction(Transaction(amount, "Monthly Earnings"))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            try:
                amount = float(input("Enter expense amount (negative value): "))
                if amount >= 0:
                    print("Expense amount should be negative.")
                    continue
                description = input("Enter description of the expense: ")
                # User describes the expenses themselves.
                tracker.add_transaction(Transaction(amount, description))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            print("Balance:", tracker.get_balance()) # Prints balance
        elif choice == "4":
            tracker.generate_report()
        elif choice == "5":
            confirm = input("Are you sure you want to reset all data? (yes/no): ")
            if confirm.lower() == 'yes':
                tracker.reset()
                tracker.save_to_file("budget_data.pkl")
                print("Data has been reset and saved.")
            else:
                print("Reset operation canceled.")
        elif choice == "6":
            tracker.plot_expenses_pie_chart()
        elif choice == "7":
            tracker.save_to_file("budget_data.pkl")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# if user exits without choosing the Exit option, file doesn't save.