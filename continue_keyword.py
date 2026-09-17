#continue keyword - is used to skip iterations
for i in range(1, 11):
    #Skip 5th iteration
    if i>=3 and i<=8: #3 - 8
        continue
    else:
        #Printing iterations
        print("Loop number ", i)