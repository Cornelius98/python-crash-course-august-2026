import os
#Check if exists, does then write to file, if not create file
if os.path.exists('example.txt'):
    #Open file in write mode
    f = open('example.txt', 'w')

    #Write to file
    result = f.write("Hello file, I am writing into example.txt file using python")
    if result:
        print("Success")
    else:
        print("Write Failed")

    #Close file
    f.close()
else:
    #Creat file, if does not exist
    f = open('example.txt', 'x')

    #close file
    f.close