#Test variables
face_id = 2
finger_print = 1

#and (&&) operator
if face_id == 1 and finger_print == 1:
    #Tenant identified
    print("Door opens and welcomes tenant")
else:
    #Tenant unrecognized
    print("Lock house entries and sound alarm")


#or () operator
if face_id == 1 or finger_print == 1:
    #Tenant identified
    print("Door opens and welcomes tenant")
else:
    #Tenant unrecognized
    print("Lock house entries and sound alarm")
