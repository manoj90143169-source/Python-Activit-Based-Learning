# Retail Billing with Multiple Discount Rules Using Python

## 1. Problem Statement

Develop a Python program to process multiple products, calculate quantities and category-specific taxes, apply threshold discounts and maximum concession limits, and generate an itemized invoice.

## 2. Algorithm

1. Start the program.
2. Enter the number of products.
3. Enter product name, category, price, and quantity.
4. Calculate subtotal and category tax.
5. Apply threshold discount.
6. Apply maximum concession limit.
7. Calculate final bill.
8. Display itemized invoice.
9. Stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter product details/]
 B --> C[Calculate subtotal and tax]
 C --> D[Apply discount rules]
 D --> E[Calculate final bill]
 E --> F{More products?}
 F -- Yes --> B
 F -- No --> G[/Display invoice/]
 G --> H([Stop])


```

## 5. Sample Input
Enter number of products: 2

Product name: Rice
Category: food
Price: 1000
Quantity: 2

Product name: Mobile
Category: electronics
Price: 10000
Quantity: 1

## 6. Sample Output

Rice Amount: 2000.0 Tax: 100.0
Mobile Amount: 10000.0 Tax: 1800.0

--- Retail Invoice ---
Subtotal with tax: 13900.0
Discount: 500.0
Final Bill: Rs. 13400.0


