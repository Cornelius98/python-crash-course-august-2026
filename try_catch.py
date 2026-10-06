import os

f = None
try:
    f = open('example.txt', 'w')
except FileNotFoundError:
    print("File does not exist")
else:
    result = f.write("Hello file, I am writing into example.txt file using python")
    if result:
        print("Success")
    else:
        print("Write Failed")
finally:
    if os.path.exists("example.txt"):
        f.close()
        print("File Closed")
    else:
        print("Operations failed")