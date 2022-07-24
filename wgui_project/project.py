import pandas as pd


# checks if verified
verified = False

class info():
    account_no=int(input("Enter Account Number: "))
    password=int(input("Enter password: "))

    df=pd.read_csv(r'D:\OOP project\Kumail (2)\project.csv')
    # print(df)
        

class Entry(info):
    length=len(info.df)
    for i in range(length):
        if info.account_no==info.df.loc[i,"Acc. No"] and info.password==info.df.loc[i,"Password"]:
            print("Welcome ",(info.df.loc[i,"Name"]))
            print("Your Current Balance is: ",(info.df.loc[i,"Balance"]))
            new_balance=(info.df.loc[i,"Balance"])
            verified = True
            print("--------------------------------------------------")

            input=input("Press 1 for Saving Account and 2 for Current Account: ")
            if input=="1":
                print("Welcome to the Saving Account!")
            elif input=="2":
                print("Wecome to the Current Account!")
            else:
                print("You have entered the wrong number, Enter either 1 or 2! ")
                exit()
    if verified != True:
            print ("Account name or password is incorrect!")
            print ("--------------------------------------------------")
            exit()


def CashWithdrawal():
    amount=eval(input("Enter the amount you want to withdraw: "))
    if amount>Entry.new_balance:
        print("The Entered amount exceeds the current balance!")
        exit()
    
    elif amount>50000:
        print("The Maximum Amount to withdraw is 50,000")
        exit()
        
    elif amount<500:
        print("The Minimum Amount to withdraw is 500")
        exit()

    subtraction = Entry.new_balance-amount
    print("Money Withdrawn, New Balance is: ",subtraction)
    info.df.replace (to_replace= Entry.new_balance, value=subtraction, inplace=True)
    info.df.to_csv(r'D:\OOP project\Kumail (2)\project.csv', index=False)
    


def MoneyTransfer():
    amount=eval(input("Enter the amount to want to send: "))
    
    if amount>Entry.new_balance:
        print("You Don't have enough balance!")
        exit()
    
    elif amount>50000:
        print("The Maximum Amount to send is 50,000")
        exit()
        
    elif amount<500:
        print("The Minimum Amount to send is 500")
        exit()
    


    transfer = Entry.new_balance-amount
    person_acc=eval(input("Enter the Account number of the person you want to send money: "))
    person=input("Enter the name of the person: ")
    print("Money Transferred to" ,person, ",New Balance is: ",transfer)

    info.df.replace (to_replace= Entry.new_balance, value=transfer, inplace=True)
    info.df.to_csv(r'C:\Users\Abbas Haider\Desktop\Kumail\project2.csv', index=False)


def CashDeposit():
    amount=eval(input("Enter the amount you want to deposit: "))


    if amount>50000:
        print("The Maximum Amount to deposit is 50,000")
        exit()
        
    elif amount<500:
        print("The Minimum Amount to deposit is 500")
        exit()


    deposit=amount+Entry.new_balance
    print("Money Deposited Successfully, New balance is: ", deposit)

    info.df.replace (to_replace= Entry.new_balance, value=deposit, inplace=True)
    info.df.to_csv(r'C:\Users\Abbas Haider\Desktop\Kumail\project2.csv', index=False)






class Saving(Entry):
    print("--------------------------------------------------")
    print("What do you want to perform?")
    print("             -               ")
    print("Enter 1 for Cash Withdrawal")
    print("Enter 2 for Money Transfer")
    print("Enter 3 for Cash Deposit")
    print("Enter 4 for Balance Inquiry")
    print("--------------------------------------------------")

    input_saving=input("Enter the number here: ")
    if input_saving=="1":
        CashWithdrawal()

    elif input_saving=="2":
        MoneyTransfer()

    elif input_saving=="3":
        CashDeposit()


