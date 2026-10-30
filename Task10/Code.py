
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per person: "))
participants = int(input("Enter expected participants: "))

total = venue + equipment + catering + transport + certificates

shortfall = max(0, total - sponsorship)
contribution = shortfall / participants if participants > 0 else 0

if fee > 0:
    minimum = max(0, int((total - sponsorship + fee - 0.01) // fee))
else:
    minimum = 0 if sponsorship >= total else -1

print("\n--- Event Financial Report ---")
print("Total Cost: Rs.", total)
print("Sponsorship Shortfall: Rs.", shortfall)
print("Contribution per Participant: Rs.", round(contribution, 2))

if minimum >= 0:
    print("Minimum Registrations:", minimum)
else:
    print("Break-even not possible without registration fee")

