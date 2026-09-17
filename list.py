#List operations
fruits = [
    "apple",
    "banana",
    "cherry",
    "strawberry"
]
#Access item from list
print(fruits[0])

#Update item
fruits[0] = "Mango"
fruits[1] = "Guava"
print(fruits)

#Add item to list
fruits.insert(4, "Paw Pawn")
print(fruits)
fruits.append("Coconut")
fruits.append("Pineapple")
print(fruits)

#Remove item
fruits.remove("Pineapple")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.clear()
print(fruits)

