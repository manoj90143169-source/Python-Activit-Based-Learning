
usage = float(input("Enter data usage (GB): "))
days = int(input("Enter required validity: "))
budget = float(input("Enter budget: "))

plans = []
n = int(input("Enter number of plans: "))

for i in range(n):
    name = input("Plan name: ")
    price = float(input("Plan price: "))
    data = float(input("Data limit (GB): "))
    validity = int(input("Validity (days): "))
    extra = float(input("Extra charge per GB: "))

    excess = max(0, usage - data)
    total = price + excess * extra

    if total <= budget and validity >= days:
        plans.append((name, total))

if plans:
    best = min(plans, key=lambda x: x[1])
    print("\nBest Plan:", best[0])
    print("Total Cost: Rs.", best[1])
else:
    print("No eligible plan found")

