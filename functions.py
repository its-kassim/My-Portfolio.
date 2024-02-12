# inbuilt functions
y = max(67, 56, 54, 34, 89)
print(y)

x = max(67, 56, 54, 34)
print(x)

z = pow(2, 3)
print(z)


# user define function
def details():
    print("bethwel")


details()  # calling a function


# Parameter and argument
def details(name, age, course):
    print(name, age, course)


details("bethwel", 30, "Python")
details("kassim", 18, "java")


def employee(name, id, position, age, salary):
    print(name, id, position, age, salary)


employee("Bethwel Komen", 117663304, "CEO", 20, 4567565)
employee("Daniel Kochei", 31883828, "Receptionist", 15, 3456756)
employee("Shadrack Kome", 24223545, "Ass Chairman", 18, 23456756)
employee("Kochen Brian", 3453678, "Chairman", 24, 23456678)
employee("Korir Shaddy", 2345656, "doctor", 19, 12345678)
