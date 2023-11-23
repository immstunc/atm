print("Welcome to the ATM")
password = "2943"
balance = 1000
trial = 3
cardBankingActive = True
bankingStatusActive = True

while bankingStatusActive:
    inputPassword = input("Please enter your password: ")
    if inputPassword != password:
        print("Wrong try!!! Please try again..")
        trial -=1
        print(trial," trial left..")
        if trial == 0:
            print("Your card has been blocked because of overtry. Contact with the bank.")
            bankingStatusActive = False
    else:
        
        print("Login Successfull")
        print("""
        Select the proccess you want to make
        ************************************
            1- Withdrawal
            2- Lodgement
            3- Balance Inquiry
            4- Exit
            """)
        
        while cardBankingActive:
            choosenProccess = input("Type your proccess: ")
            if choosenProccess == "4":
                print("Exited.")
                bankingStatusActive = False
                cardBankingActive = False
            elif choosenProccess == "3":
                print("Your account balance: ", balance,"₺")
            elif choosenProccess == "2":
                lodgementAmount = int(input("Please enter lodgement amount: "))
                balance += lodgementAmount
                print("Lodgement is successfull")
            elif choosenProccess == "1":
                withdrawalAmount = int(input("Please enter withdrawal amount: "))
                if withdrawalAmount > balance:
                    print("Your balance not enough!!")
                else:
                    balance -=withdrawalAmount
                    print("Withdrawal successfull")
            else:
                print("Please enter a valid selection!!!")


