atm_card = 1234
password = 1030

#Check if card accepted
if atm_card == 1234 and password == 1010:
    #Proceed to withdraws
    print("Welcome to banking menu")
    withdraw_amount = 100
    available_amount = 20000

    #Check if requested amount is available
    if withdraw_amount <= available_amount:
        print("You are withdrawing: ", withdraw_amount)
    else:
        print("Insufficient funds")
else:
    #Declined card
    print("Card declined")

    ask_help = True
    if ask_help == True:
        print("Card declined, contacting nearest branch")
    else:
        print("Card declined, try next time")