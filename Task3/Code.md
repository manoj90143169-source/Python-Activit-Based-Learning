# Hospital Billing and Patient Classification Using Python

## 1. Problem Statement

Develop a Python program to calculate hospital bills using consultation, diagnostic, and treatment charges. Apply concessions based on patient conditions, validate billing details, and classify patients according to their payment status.

## 2. Algorithm

1. Start the program.
2. Enter patient name and charges.
3. Calculate total bill.
4. Apply concession if eligible.
5. Validate charges.
6. Calculate final bill.
7. Classify patient as Fully Paid, Partially Paid, or Unpaid.
8. Display bill details.
9. Stop.
## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter patient charges and payment/]
 B --> C{Valid details?}
 C -- No --> D[Display Error]
 C -- Yes --> E[Calculate bill and concession]
 E --> F[Calculate balance]
 F --> G[Classify payment status]
 G --> H[/Display bill/]
 H --> I([Stop])
 D --> I
```



## 5. Sample Input
Enter patient name: Ravi
Consultation charges: 500
Diagnostic charges: 2000
Treatment charges: 4000
Enter payment amount: 3000


## 6. Sample Output

--- Hospital Bill ---
Patient: Ravi
Total Bill: 6500.0
Concession: 650.0
Final Bill: 5850.0
Payment: 3000.0
Balance: 2850.0
Classification: Partially Paid

