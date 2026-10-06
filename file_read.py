import os
if os.path.exists('example.txt'):
    f = open('example.txt', 'r')
    fileContent = f.read()
    print("File Content: ", fileContent)
    f.close()
else:
    print("File doesn't exist")
