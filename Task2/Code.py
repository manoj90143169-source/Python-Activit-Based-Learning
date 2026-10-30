
bills = []
n = int(input("Enter number of months: "))

for i in range(n):
    units = int(input("Enter units consumed: "))

    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100*2 + (units-100)*3
    else:
        charge = 100*2 + 100*3 + (units-200)*5

    fixed = 50
    surcharge = charge * 0.05
    rebate = 20 if units < 100 else 0

    total = charge + fixed + surcharge - rebate
    bills.append(total)

    print("Month", i+1, "Bill: Rs.", round(total, 2))

print("\nBill Comparison:")
for i in range(1, n):
    increase = bills[i] - bills[i-1]

    if increase > bills[i-1] * 0.20:
        print("Month", i+1, ": Unusual increase")
    else:
        print("Month", i+1, ": Normal")

