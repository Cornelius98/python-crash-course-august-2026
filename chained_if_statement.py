#Patient condition
pc = ""
temp = 40

if pc == "cough" and temp<= 37:
    print("cough")
elif pc == "cough" and temp>=38 and temp<=40:
    print("intense cough")
elif pc == "cough" and temp>=40 and temp<=50:
    print("COVID")
elif pc == "cough" and temp>=50 and temp<=60:
    print("Maleria")
else:
    print("Further test")

