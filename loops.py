# while loop
# implementing a value
numbers = 5
while numbers <= 10:
    print(numbers)
    numbers = numbers + 1

# decrementing a value
num = 105
while num >= 100:
    print(num)
    num = num - 1

# break statement
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1

# continue
count = 19
while count < 25:
    count = count + 1
    if count == 23:
        continue
    print(count)

# For loop
languages = ['Python', 'Java', 'C', 'C++', 'Kotlin']
for lang in languages:
    print(lang)

# range
for z in range(6):
    print(z)

for y in range(20, 31):
    print(y)

for i in range(30, 41, 2):
    print(i)

k = "innovation"
for k in "innovation":
    print(k)
