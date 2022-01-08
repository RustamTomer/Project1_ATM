#customer care system
print ("Thank you for ordering")
print("1. Issue with the item delievered")
print("2. Download the invoice")
print("3. Talk to customer care")
c = input("Please specify your issue: ")
if(c=="1") :
    print("1. Refund")
    print("2. Replace")
    a = input("Please choose below: ")
    if(a=="1"):
        print("Refund Initiated.")
    elif(a=="2"):
        print("Replacing your product.")
    else :
        print("Invalid choice")
elif(c=="2") :
    print("Invoice downloaded SUCCESSFULLY!! ")
elif(c=="3") :
    print("1. English")
    print("2. Hindi")
    l = input("Please specify the language: ")
    if(l=="1") :
        print("Called in ENGLISH! ")
    elif(l=="2") :
        print("Called in HINDI! ")
    else :
        print("SORRY! Invalid choice. ")
else :
    print("SORRY! Invalid choice. ")
print("Thank you! Visit again")
    
