
n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Product name: ")
    category = input("Category (food/electronics): ").lower()
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    amount = price * qty

    tax_rate = 5 if category == "food" else 18
    tax = amount * tax_rate / 100

    print(name, "Amount:", amount, "Tax:", tax)
    total += amount + tax

discount = total * 0.10 if total >= 5000 else 0
discount = min(discount, 500)

final = total - discount

print("\n--- Retail Invoice ---")
print("Subtotal with tax:", round(total, 2))
print("Discount:", round(discount, 2))
print("Final Bill: Rs.", round(final, 2))

