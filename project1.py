import pandas as pd
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import Canvas, Text
# calling recogniser from face_recog for login
from recoginiser import *
from PIL import ImageTk,Image
import os

root = ctk.CTk()
root.title("ATM System Project")

canvas = tk.Canvas(root, height=700,width=700,bg='#212325')
canvas.pack()
df=pd.read_csv(r'D:\OOP project\OOP Project ATM\project.csv')


class Pin:
    def pinLogin():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter ID and PIN", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()

        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        

        player_name = Entry(frame)
        player_name.pack(pady=20)
        Label(frame,text="ID", pady=10, fg='white',bg='#2a2d2e').pack()

        player_name2 = Entry(frame)
        player_name2.pack(pady=20)
        Label(frame,text="PIN", pady=10, fg='white',bg='#2a2d2e').pack()
        

        def LoginFile():
            verified=False
            id = int(player_name.get())
            pin = int(player_name2.get())

            for i in range(5):
                if id==df.loc[i,"Acc. No"] and pin==df.loc[i,"Password"]:
                    print("Welcome ",(df.loc[i,"Name"]))
                    global balance

                    balance=(df.loc[i,"Balance"])
                    
                    verified = True
                    
                    

            if verified != True:
                print("Id and Password doesn't match!")
                exit()
                    

            canvas.delete('all')
            canvas.create_text(300, 40, text="Press Continue", fill="#b2bec3", font=('Symbola 20 bold'))
            canvas.pack()

            frame = tk.Frame(root, bg='#2a2d2e')
            frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

            ctk.CTkButton(frame,text="Continue", padx=10, pady=15,command=pageThree.ThirdPage).pack()
        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=LoginFile).pack()






class Process:
    def Login():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter ID", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()

        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        

        player_name = Entry(frame)
        player_name.pack(pady=50)

        

        def LoginFile():
            verified=False
            pin = int(player_name.get())
            for i in range(5):
                if pin==df.loc[i,"Acc. No"]:
                    print("Welcome ",(df.loc[i,"Name"]))
                    global balance

                    balance=(df.loc[i,"Balance"])
                    
                    verified = True
                    
                    

            if verified != True:
                print("Id Doesn't Exist!")
                exit()
                    
            
            recognise.login()
            canvas.delete('all')
            canvas.create_text(300, 40, text="Press Continue", fill="#b2bec3", font=('Symbola 20 bold'))
            canvas.pack()

            frame = tk.Frame(root, bg='#2a2d2e')
            frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

            ctk.CTkButton(frame,text="Continue", padx=10, pady=15,command=pageThree.ThirdPage).pack()
        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=LoginFile).pack()
    


class Withdrawing(Process):
    def withdrawAmount():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
        def withdraw():
            pname = int(player_name.get())
            if pname>=500:
                Label(frame, text=f'{pname}rs Withdrawn!', pady=20, fg='white',bg='#2a2d2e').pack()
                new_balance=balance-pname
                df.replace (to_replace= balance, value=new_balance, inplace=True)
                df.to_csv(r'D:\OOP project\OOP Project ATM\project.csv', index=False)
                

            else:
                Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()

                
            
            

        player_name = Entry(frame)
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=withdraw).pack()

class Transfering(Process):
    def moneyTransfer():

        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
        def transfer():
            pname = int(player_name.get())
            if pname>=500:
                Label(frame, text=f'{pname}rs Transferred!', pady=20, fg='white',bg='#2a2d2e').pack()
                new_balance=balance-pname
                df.replace (to_replace= balance, value=new_balance, inplace=True)
                df.to_csv(r'D:\OOP project\OOP Project ATM\project.csv', index=False)
                

            else:
                Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()

                
            
            

        player_name = Entry(frame)
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=transfer).pack()



class Depositing(Process):
    def moneyDeposit():

        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
        def transfer():
            pname = int(player_name.get())
            if pname>=500:
                Label(frame, text=f'{pname}rs Transferred!', pady=20, fg='white',bg='#2a2d2e').pack()
                new_balance=balance+pname
                df.replace (to_replace= balance, value=new_balance, inplace=True)
                df.to_csv(r'D:\OOP project\OOP Project ATM\project.csv', index=False)
                

            else:
                Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()

                
            
            

        player_name = Entry(frame)
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=transfer).pack()


class Balance(Process):
    def balanceInquiry():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        Label(frame,text='Current Balance is: ' + str(balance), pady=20, fg='white',bg='#2a2d2e').pack()




    
# defining page four

def PageFour():
    canvas.delete('all')
    canvas.create_text(300, 40, text="Select The Action You Want To Perform", fill="#b2bec3", font=('Symbola 20 bold'))
    canvas.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    withdrawButton = ctk.CTkButton(frame, text="Cash Withdrawal",pady=30, padx=10 , bg="#16a085", command=Withdrawing.withdrawAmount)
    withdrawButton.pack()


    transferButton = ctk.CTkButton(frame, text="Transfer Money",pady=30, padx=10 , bg="#16a085", command=Transfering.moneyTransfer)
    transferButton.pack()


    depositButton = ctk.CTkButton(frame, text="Deposit Money",pady=30, padx=10 , bg="#16a085", command=Depositing.moneyDeposit)
    depositButton.pack()


    balanceButton = ctk.CTkButton(frame, text="Balance inquiry",pady=30, padx=10 , bg="#16a085", command=Balance.balanceInquiry)
    balanceButton.pack()







# defining page one

class PageOne:
    canvas.create_text(300, 40, text="Choose Login Method", fill="#b2bec3", font=('Symbola 25 bold'))
    canvas.pack()
    
    my_img= ImageTk.PhotoImage(Image.open("D:\OOP project\OOP Project ATM\logo.jpg"))
    my_label= Label(image=my_img)
    my_label.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    PinButton = ctk.CTkButton(frame, text="PIN", pady=10, padx=10 , bg="#16a085", command=Pin.pinLogin)
    PinButton.place(x=100 ,y=130)



    FaceButton = ctk.CTkButton(frame, text="Biometric",pady=10, padx=10 , bg="#16a085", command=Process.Login)
    FaceButton.place(x=100,y=200)

# defining page three

class pageThree:
    def ThirdPage():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Choose Your Account Type", fill="#b2bec3", font=('Symbola 25 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



        savingButton = ctk.CTkButton(frame, text="Saving Account", pady=10, padx=10 , bg="#16a085", command=PageFour)
        savingButton.place(x=100 ,y=130)


        currentButton = ctk.CTkButton(frame, text="Current Account",pady=10, padx=10 , bg="#16a085", command=PageFour)
        currentButton.place(x=100,y=200)


root.mainloop()



