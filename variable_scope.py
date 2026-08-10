#Variable scope (Visibility)
#local scope
def findSum():
    quantity = 100
    result = quantity * 5
    print("Local scope: ", result)

findSum()
#print(quantity) - Undefined in global scope

#Global scope
isCustomerID = 1234
def buyNow():
    print("Customer check out ID: ", isCustomerID)

buyNow()

print("Customer ID below function: ", isCustomerID)