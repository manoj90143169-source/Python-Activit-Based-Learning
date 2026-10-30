#  Multi-Plan Telecommunications Cost Optimization Using Python

## 1. Problem Statement

Develop a Python program to compare different mobile plans based on data usage, validity, and budget. Calculate excess usage charges and identify the most economical eligible mobile plan.

## 2. Algorithm

1. Start the program.
2. Enter data usage, validity, and budget.
3. Enter mobile plan details.
4. Calculate excess charges.
5. Calculate total plan cost.
6. Check budget and validity conditions.
7. Select the cheapest eligible plan.
8. Display the result.
9. Stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter usage and budget/]
 B --> C[Enter mobile plan details]
 C --> D[Calculate total cost]
 D --> E{Within budget and validity?}
 E -- Yes --> F[Select cheapest plan]
 E -- No --> G[Reject plan]
 F --> H{More plans?}
 G --> H
 H -- Yes --> C
 H -- No --> I[/Display best plan/]
 I --> J([Stop])


```

## 5. Sample Input

Enter data usage (GB): 20
Enter required validity: 28
Enter budget: 500
Enter number of plans: 3

Plan name: Plan A
Plan price: 299
Data limit (GB): 15
Validity (days): 28
Extra charge per GB: 10

Plan name: Plan B
Plan price: 399
Data limit (GB): 25
Validity (days): 28
Extra charge per GB: 10

Plan name: Plan C
Plan price: 199
Data limit (GB): 10
Validity (days): 14
Extra charge per GB: 15

## 6. Sample Output

Best Plan: Plan B
Total Cost: Rs. 399.0


