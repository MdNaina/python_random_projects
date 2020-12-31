import time
customer_name = ""
acc_no = ""
bal = 500
while True:
    time.sleep(2.5)
    print('+------------------------------------+')
    print('| 1 - get the values                 |')
    print('| 2 - deposit to account             |')
    print('| 3 - withdraw in account            |')
    print('| 4 - show your profile              |')
    print('| 5 - to exit                        |')
    print('+------------------------------------+\n')
    choice = input('Enter you choice : ')
    if choice == '1':
        customer_name = input('\ntype a customer name?\n : ')
        acc_no = input('type a account number?\n : ')
        print("profile update\n")

    elif choice == '2':
        deposit = int(input('\nEnter the amount to deposit\n : '))
        bal += deposit
        print("updated")

    elif choice == '3':
        withdraw = int(input('\nEnter the withdrawal amount\n :'))
        bal -= withdraw
        print("updated")

    elif choice == '4':
        print('\nyou profile'.title())
        print(f"Costomor_Name : {customer_name}")
        print(f"Account_Number : {acc_no}")
        print(f"Balance : {bal}")
        print("This your account details\n")

    elif choice == '5':
        print("\nprogram is terminated")
        break

    else:
        print("I dont understand your command")
