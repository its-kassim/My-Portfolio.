# Exceptions


try:
    print(x)

except:
    print("An error occurred")

num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("An error occurred")
finally:
    print("success")

# User defined functions
try:
    def multiply(number1, number2):
        print(number1 * number2)
except:
    print("An error occurred")

finally:
    print("success")



