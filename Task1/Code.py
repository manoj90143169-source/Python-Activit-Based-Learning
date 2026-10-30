
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = list(map(int, input("Enter 5 subject marks: ").split()))
    att = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    avg = sum(marks) / 5

    if avg >= 75 and min(marks) >= 60 and att >= 75 and income <= 250000:
        students.append((name, avg, att, income))

students.sort(key=lambda x: (-x[1], -x[2], x[3], x[0]))

print("\nEligible Students:")
for rank, s in enumerate(students, 1):
    print(rank, s)
    
if not students:
    print("No eligible students")

