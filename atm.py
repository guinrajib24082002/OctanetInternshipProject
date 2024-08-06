import time

print("please insert your card")
time.sleep(5)

password=1234
pin=int(input("enter your atm pin"))

balance=5000
transaction_history=[]

if pin==password:
    while True:
        print("""
        1==balance
        2==withdraw_balance
        3==deposit_balance
        4==change pin
        5==show transaction history
        6==exit
        """
        )
    

        try:
            option =int(input("please enter your choice"))
        except:
            print("please enter valid option")

        if option==1:

            print(f"your current balance is{balance}")
            transaction_history.append(f"checked balance is:{balance}")

        elif option==2:

            withdraw_amount=int(input("please enter withdraw_amount"))
            if withdraw_amount>balance:
                print("insufficient balance")
                transaction_history.append(f"failed withdrawl of {withdraw_amount}due to insufficient balance")
            else:    
                balance=balance-withdraw_amount
                print(f"{withdraw_amount} is debited from your account")

                print(f"your current balance is{balance}")
                transaction_history.append(f"withdrew {withdraw_amount},new balance is:{balance}")

        elif option==3:

            deposit_amount=int(input("please enter your deposit_amount"))  
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited in your account") 
            print(f"your updated account balance is{balance}")
            transaction_history.append(f"deposited {deposit_amount},new balance is:{balance}")

        elif option==4:
            old_pin=int(input("please enter your old pin:"))
            if old_pin==password:
                new_pin=int(input("please enter your new pin:"))
                confirm_new_pin=int(input("please confirm your new pin:"))
                if new_pin==confirm_new_pin:
                    password=new_pin
                    print("your pin has been successfully changed!")
                    transaction_history.append("pin changed successfully")
                else:
                    print("new pin and confirm pin do not match,please try again later!")
                    transaction_history.append("failed pin change due to mismatch!!")
            else:
                print("incorrect old pin,try again later!!")
                transaction_history.append("failed pin change due to incorrect old pin")

        elif option==5:
            print("transaction history:")
            for transaction in transaction_history:
                print(transaction)

        elif option==6:
            print("thank you for using our services,visit again")
            break     


        else:
         print("wrong pin,please try again")
