
name = input("Enter patient name: ")

consult = float(input("Consultation charges: "))
diagnostic = float(input("Diagnostic charges: "))
treatment = float(input("Treatment charges: "))
payment = float(input("Enter payment amount: "))

if min(consult, diagnostic, treatment, payment) < 0:
    print("Invalid billing details")

else:
    total = consult + diagnostic + treatment

    # Apply 10% concession for bills above Rs. 5000
    discount = total * 0.10 if total > 5000 else 0

    final = total - discount

    if payment > final:
        print("Invalid payment amount")
    else:
        balance = final - payment

        if balance == 0:
            status = "Fully Paid"
        elif payment > 0:
            status = "Partially Paid"
        else:
            status = "Unpaid"

        print("\n--- Hospital Bill ---")
        print("Patient:", name)
        print("Total Bill:", total)
        print("Concession:", discount)
        print("Final Bill:", final)
        print("Payment:", payment)
        print("Balance:", balance)
        print("Classification:", status)

