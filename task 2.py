choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ")
if choice == "C" or choice == "c":
   celsius = float(input("Enter temperature in Celsius: "))
   fahrenheit = (celsius * 1.8) + 32
   print("Temperature in Fahrenheit:", fahrenheit, "°F")
elif choice == "F" or choice == "f":
   fahrenheit = float(input("Enter temperature in Fahrenheit: "))
   celsius = (fahrenheit - 32) / 1.8
   print("Temperature in Celsius:", celsius, "°C")
else:
   print("Invalid choice!")