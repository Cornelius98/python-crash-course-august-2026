#List of customer purchases
numbers = [1, 2, 3, 4, 5]

#For Loop - used to iterate list
# 1. Display items
# 2. Perform operations on items in array
for numberInList in numbers:
    numberInList *= 2
    print(numberInList)


#While loop, looping through list
fruits = ["apple", "banana", "cherry"]
print(fruits)
count = 0
while count < len(fruits):
    # Change item
    fruit = fruits[count]
    if fruit == "apple":
        fruits[count] = "Guava"
    else:
        print(fruits[count])
    count+=1

print(fruits)
