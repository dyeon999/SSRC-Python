fruits = ["APPLE", "BANANA", "ORANGE"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "안녕", 3.14, True]
# Declare Lists

print(f"fruit list : {fruits}")
print()

print("type of fruits: ", type(fruits))
print()

print(f"the first fruit : {fruits[0]}")
print(f"the second fruit : {fruits[1]}")
print(f"the third fruit : {fruits[2]}")
print()

print('"Print "Fruits List" By Using "for" Loop')
for fruit in fruits:
    print(f"fruit: {fruit}")
"""
for i in range(3):
    print(f"fruit: {fruits[i]}")

for i in range(len(fruits)):
    print(f"fruit: {fruits[i]}")
"""
print()

for i, fruit in enumerate(fruits):
    print(f"{i+1}번째 과일: {fruit}")
'''
for i in range(len(fruits)):
    print(f"{i+1}번째 과일: {fruits[i]}")
'''