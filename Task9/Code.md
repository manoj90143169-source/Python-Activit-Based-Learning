# Multi-Currency Travel Budget Analysis Using Python

## 1. Problem Statement

Develop a Python program to calculate travel expenses in different currencies using supplied exchange rates. Include conversion fees, compare total spending against the budget, and identify the largest expense category.

## 2. Algorithm

1. Start the program.
2. Enter travel budget in INR.
3. Enter expense categories and amounts.
4. Enter currency and exchange rate.
5. Convert expenses into INR.
6. Add currency conversion fees.
7. Calculate total expenses.
8. Identify the largest expense category.
9. Compare expenses with budget.
10. Display the report and stop.

## 3. Flowchart 
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter budget and expenses/]
 B --> C[Convert currency and add fees]
 C --> D[Calculate total expenses]
 D --> E[Find largest expense]
 E --> F{Within budget?}
 F --> G[/Display report/]
 G --> H([Stop])



```

## 5. Sample Input
Enter budget in INR: 100000
Enter number of expenses: 3

Enter category: Hotel
Enter expense amount: 300
Enter exchange rate to INR: 85
Enter conversion fee percentage: 2

Enter category: Food
Enter expense amount: 100
Enter exchange rate to INR: 85
Enter conversion fee percentage: 2

Enter category: Transport
Enter expense amount: 200
Enter exchange rate to INR: 85
Enter conversion fee percentage: 2

## 6. Sample Output

Hotel Cost: Rs. 26010.0
Food Cost: Rs. 8670.0
Transport Cost: Rs. 17340.0

--- Travel Budget Report ---
Total Expenses: Rs. 52020.0
Largest Expense: Hotel
Within Budget


