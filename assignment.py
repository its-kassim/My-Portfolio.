# Python program to make a simple calculator

# Take inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation
print("Operation: +, -, *, /")
select = input("Select operations: ")

# Check operations and display result
if select == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif select == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif select == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif select == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid input")