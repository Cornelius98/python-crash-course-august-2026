import os
if os.path.exists('example.txt'):
    f = open('example.txt', 'a')
    f.write("\nTesting to append to example.txt file using python")
    f.close()

else:
    print("File not exist")
