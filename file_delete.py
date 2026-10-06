import os
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("File Deleted: ")
else:
    print("File not exist")
