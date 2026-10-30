
n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i+1)
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance (km): "))
    cls = input("Enter class (Sleeper/AC): ").lower()

    rate = 2 if cls == "sleeper" else 5
    fare = distance * rate

    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.5

    reservation = 50
    total = fare + reservation

    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = total * 0.20
        total -= penalty

    print("\n--- Railway Ticket ---")
    print("Passenger:", name)
    print("Fare: Rs.", fare)
    print("Reservation: Rs.", reservation)
    print("Final Fare: Rs.", round(total, 2))

