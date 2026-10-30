
# Progressive Electricity Billing System Using Python

## 1. Problem Statement

Develop a Python program to calculate electricity bills based on consumption slabs, fixed charges, surcharges, and rebates. Compare bills across multiple months and identify unusual increases in electricity usage.

## 2. Algorithm

1. Start the program.
2. Enter the number of months.
3. Enter electricity units consumed each month.
4. Calculate charges using different slabs.
5. Add fixed charges and surcharges.
6. Apply rebates if applicable.
7. Calculate the final bill.
8. Compare monthly bills and identify unusual increases.
9. Display the bills.
10. Stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter monthly units/]
 B --> C[Calculate slab charges]
 C --> D[Add fixed charges and surcharge]
 D --> E[Apply rebate]
 E --> F[Calculate final bill]
 F --> G{More months?}
 G -- Yes --> B
 G -- No --> H[Compare monthly bills]
 H --> I[Identify unusual increases]
 I --> J[/Display bills/]
 J --> K([Stop])



```

## 5. Sample Input
Enter number of months: 3
Enter units consumed: 80
Enter units consumed: 150
Enter units consumed: 250

## 6. Sample Output
Month 1 Bill: Rs. 214.0
Month 2 Bill: Rs. 525.0
Month 3 Bill: Rs. 1050.0

Bill Comparison:
Month 2 : Unusual increase
Month 3 : Unusual increase

