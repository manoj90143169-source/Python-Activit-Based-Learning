
budget = float(input("Enter budget in INR: "))
n = int(input("Enter number of expenses: "))
expenses = {}

for i in range(n):
    category = input("Enter category: ")
    amount = float(input("Enter expense amount: "))
    rate = float(input("Enter exchange rate to INR: "))
    fee = float(input("Enter conversion fee percentage: "))

    total = amount * rate
    total += total * fee / 100

    expenses[category] = total
    print(category, "Cost: Rs.", round(total, 2))

total_cost = sum(expenses.values())
largest = max(expenses, key=expenses.get)

print("\n--- Travel Budget Report ---")
print("Total Expenses: Rs.", round(total_cost, 2))
print("Largest Expense:", largest)

if total_cost <= budget:
    print("Within Budget")
else:
    print("Over Budget by Rs.", round(total_cost-budget, 2))

