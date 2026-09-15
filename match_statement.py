#Patient condition
pc = ""
temp = 40
match pc, temp:
    case "cough", True if temp<= 37:
        print("cough")
    case "cough", True if temp>=38 and temp<=40:
        print("intense cough")
    case "cough", True if temp>=40 and temp<=50:
        print("COVID")
    case "cough", True if temp>=50 and temp<=60:
        print("Maleria")
    case _:
        print("Further test")


