# Railway Fare and Reservation Calculator Using Python

## 1. Problem Statement

Develop a Python program to calculate railway fares for multiple passengers based on distance slabs, travel classes, age-based concessions, reservation fees, and cancellation penalties.

## 2. Algorithm

1. Start the program.
2. Enter the number of passengers.
3. Enter passenger age, distance, and travel class.
4. Calculate fare using distance slabs.
5. Apply age-based concessions.
6. Add reservation fees.
7. Calculate cancellation penalty if applicable.
8. Display the final fare.
9. Stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter passenger details/]
 B --> C[Calculate distance and class fare]
 C --> D[Apply age concession]
 D --> E[Add reservation fee]
 E --> F{Ticket cancelled?}
 F -- Yes --> G[Deduct cancellation penalty]
 F -- No --> H[Calculate final fare]
 G --> H
 H --> I[/Display fare/]
 I --> J([Stop])



```

## 5. Sample Input
Enter number of passengers: 2

Passenger 1
Enter name: Ravi
Enter age: 65
Enter distance (km): 500
Enter class (Sleeper/AC): sleeper
Cancel ticket? (yes/no): no

Passenger 2
Enter name: Kumar
Enter age: 30
Enter distance (km): 500
Enter class (Sleeper/AC): AC
Cancel ticket? (yes/no): yes

## 6. Sample Output
--- Railway Ticket ---
Passenger: Ravi
Fare: Rs. 500.0
Reservation: Rs. 50
Final Fare: Rs. 550.0

--- Railway Ticket ---
Passenger: Kumar
Fare: Rs. 2500.0
Reservation: Rs. 50
Final Fare: Rs. 2040.0



Note: The fare rates, concessions, and penalties used here are assumed values for a Python programming exercise, not actual railway tariff rules.
