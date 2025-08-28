import matplotlib.pyplot as plt

expenses = {}

while True:
    category = input("Enter expense category (or 'q' to quit'): ")
    if category.lower() == 'q':
        break
    amount = float(input("Enter amount: "))
    expenses[category] = expenses.get(category, 0) + amount

print("Expense Summary:", expenses)

# Bar chart
plt.bar(expenses.keys(), expenses.values())
plt.title("Expense Tracker - Bar Chart")
plt.show()

# Pie chart
plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
plt.title("Expense Tracker - Pie Chart")
plt.show()
