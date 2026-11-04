a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
   result = a + b
   print("Result:", result)
elif operation == "-":
   result = a - b
   print("Result:", result)
elif operation == "*":
   result = a * b
   print("Result:", result)
elif operation == "/":
   if b != 0:
       result = a / b
       print("Result:", result)
   else:
       print("Error: Cannot divide by zero!")
else:
   print("Invalid operation!")