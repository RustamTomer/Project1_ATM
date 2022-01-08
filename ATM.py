print("WELCOME TO EMZERR BANK")
menu = ('Y')
attempts=4
balance=100000.00
while attempts >= 0:
    pin = int(input("Enter Your Pin :"))
    if pin == (0000):
        print("Pin entered by you is correct.")
        while menu not in ('n', 'N', "No", "no"):
            print("1 for Balance Enquiry")
            print("2 For Cash Withdrawl")
            print("3 to use EMZERR PAY")
            print("4 to Return Card")
            option=int(input("What would you like to chooose?"))
            if option == 1:
                print("Your Balance is Rs.", balance)
                menu=input("Would you like to go back? (Y/N)")
                if menu in ('n', 'N', "No", "no"):
                    print("THANK YOU FOR USING EMZERR BANKING ATM")
                    quit()
            elif option == 2:
                withdrawl = float(input("How much would you like to withdraw? Rs. 100/Rs. 500/Rs. 2000/Rs. 5000/Rs. 10000"))
                if withdrawl in [100,500,2000,5000,10000]:
                    balance = balance - withdrawl
                    print("Reamaining Balance in your account is", balance)
                    menu = input("Would you like to go back? (Y/N)")
                    if menu in ('n', 'N', "No", "no"):
                        print("THANK YOU FOR USING EMZERR BANKING ATM")
                        quit()
                elif withdrawl != [100,500,2000,5000,10000]:
                    print("INVALID AMOUNT, RE-TRY")
                    menu = ('Y')
                elif withdrawl == 1:
                    withdrawl=float(input("Enter Amount:"))
            elif option == 3:
                Pay = float(input("Enter amount to pe paid:"))
                balance = balance - Pay
                print("Reamaining Balance in your account is", balance)
                menu = input("Would you like to go back? (Y/N)")
                if menu in ('n', 'N', "No", "no"):
                    print("THANK YOU FOR USING EMZERR BANKING SERVICES")
                    quit()
            elif option == 4:
                print("Please wait returning in process")
                print("THANK YOU FOR USING EMZERR BANKING SERVICES")
                exit()
            else:
                print("Please enter a correct no.")
                menu=('Y')
    elif pin != (0000):
        print("INCORRECT PIN")
        attempts = attempts - 1
        if attempts == 0:
            print("Card Blocked")
            break
