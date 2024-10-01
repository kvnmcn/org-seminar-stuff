# Int
num1 = 5
num2 = 4
# String
name = "Kevin"
address = "davao city"
print(name.upper())
print(name.lower())

# Non-Primitive Data Types

# Lists
print("Lists")
toppings = ["teriyaki", "gravy", "original", "barbecue", "watermelon"]
print(toppings)
toppings.pop()
print(toppings)
toppings.append("durian")
print(toppings)
toppings.remove("durian")
print(toppings)

# Tuple
# Tuple is immutable
print("Tuples")
toppings2 = ("chili", "bbq")
toppings2 = list(toppings2)
# Unpack
flavor1, flavor2 = toppings2
print(flavor1)
print(flavor2)

student = ("1234", "John", "Doe")
id, *fullname = student
# fullname turns into a List
print(id)
print(fullname)
fullname[0] = "Nana"
print(fullname)

# Set
# Set cannot have multiple occurrences of the same element and store unordered values
print("Set")
orders = ["apple", "banana", "orange", "apple"]
print(orders)
orders = set(orders)
print(orders)

# Dictionary
student = {
    "id": "23475",
    "fname": "John",
    "lname": "Doe",
    "age": 30,
    "hobbies": ["volleyball", "python", "stan bini"]
}
print(student)

print(student["id"])
print(student.get("id"))
print(student["hobbies"][-1])
