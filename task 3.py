n = int(input("Enter the number of grades: "))
total = 0
for i in range(n):
   grade = float(input("Enter grade: "))
   total = total + grade
average = total / n
print("Average:", average)
if average >= 3.0:
   print("The student passed.")
else:
   print("The student failed.")