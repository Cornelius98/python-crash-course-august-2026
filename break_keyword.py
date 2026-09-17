#break keyword - terminates a loop before it's condition is reached
for i in range(1, 101):
    #terminate on 20th iteration
    if i == 20:
        break
    else:
        #Printing iterations
        print("Loop ", i)