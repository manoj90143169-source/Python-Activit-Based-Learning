
name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentive = float(input("Enter incentives: "))

gross = basic + allowance + overtime + incentive
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = 20000*0.05 + (gross-20000)*0.10
else:
    deduction = 20000*0.05 + 20000*0.10 + (gross-40000)*0.15

net = gross - deduction

print("\n--- Salary Statement ---")
print("Employee:", name)
print("Gross Salary: Rs.", gross)
print("Deduction: Rs.", deduction)
print("Net Salary: Rs.", net)

