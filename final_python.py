from abc import ABC
import random


class Bank:
    def __init__(self):
        self.accounts = []  
        self.total_loan_amount = 0  
        self.balance = 0 
        self.loan_feature_enabled = True 
        



class User(ABC):
    def __init__(self,name,email,addres):
        self.name=name
        self.email=email
        self.addres=addres



class Acount_Holder(User):
    def __init__(self, name, email, addres,account_type):
        super().__init__(name, email, addres)
        self.balance = 0
        self.transaction_history = [] 
        self.loan_count = 0
        self.account_type=account_type
        self.account_number = str(random.randint(1000000, 9999999))


    def create_account(self,bank):
        bank.accounts.append(self)
        print(f"Account created for {self.name} and account number: {self.account_number}")



    def deposite(self,bank,amount):
        if amount>0:
            self.balance +=amount
            bank.balance += amount
            self.transaction_history.append({
                'type': 'deposite',
                'amount': amount,
                'Current_blance': self.balance
            })
            print(f"Deposite: {amount}\nNew balance: {self.balance}")
        else:
            print("You should Deposite more than 0 taka")



    def withdraw(self,bank,amount):
        if amount<self.balance:
            if bank.balance<amount:
                print("Bank is bankcrupt")
                return
            else:
                bank.balance -= amount
            self.balance -=amount
            self.transaction_history.append({
                'type': 'withdraw',
                'amount': amount,
                'Current_blance': self.balance
            })
            print(f"Withdraw: {amount}\nNew balance: {self.balance}")
        else:
            print("Withdrawal Amount Exceeded")



    def check_balance(self):
        print(f"Current Balance: {self.balance}")




    def check_transaction_history(self):
        for i in self.transaction_history:
            print(f"{i['type']}\t{i['amount']}\t{i['Current_blance']}")



    def request_loan(self, bank, amount):
        if self.loan_count >= 2:
            print("Maximum loan taken.") 
        else:
            self.balance += amount
            bank.balance -= amount 
            self.loan_count += 1
            self.transaction_history.append({
                'type': 'loan',
                'amount': amount,
                'Current_blance': self.balance
            })
            bank.total_loan_amount += amount  
            print(f"You get loan of {amount} Taka.\n Your Current balance: {self.balance}")


    def transfer(self, bank, account_number, amount):
        f = 0
        for i in bank.accounts:
            if account_number == i.account_number:
               f =1
        if f==0:
            print("Account does not exist")
        else:
            if amount > self.balance:
                print("Insufficient Balance.")

            else:
                self.balance -= amount
                bank.balance -= amount 
                for i in bank.accounts:
                    if i.account_number==account_number:
                        i.balance += amount
                bank.balance += amount 
                self.transaction_history.append({
                    'type': 'transfer',
                    'amount': amount,
                    'Current_blance': self.balance,
                    'account': account_number
                })
                print(f"Transferred Amount {amount} Taka To Acount No. {account_number}.\nCurrent balance: {self.balance}")






class Admin(User):
    def __init__(self, name, email, addres):
        super().__init__(name, email, addres)
    
    def create_account(self, bank, name, email, address, account_type):
        new_account = Acount_Holder(name, email, address, account_type)
        bank.accounts.append(new_account)
        print(f"Account created for {name} and account number: {new_account.account_number}")

    def delete_account(self, bank, account_number):
        f = 0
        for i in bank.accounts:
            if account_number == i.account_number:
                print(f"Deleted account of {i.name} acc no. {i.account_number}")
                f=1
                bank.accounts.remove(i)
                break
        if f ==0:
            print("Account Number does not Exist")     


    def view_all_accounts(self, bank):
        for i in bank.accounts:
            print("name:\t Email:\t Addres:\t Account_type: ")
            print(f"{i.name}\t {i.email}\t {i.addres}\t {i.account_type}")
        


    def check_total_bank__balance(self, bank):
        print(f"Total available balance of the bank: {bank.balance}") 
    

    def check_total_loan_amount(self, bank):
        print(f"Total loan amount of the bank: {bank.total_loan_amount}")


    def loan_feature_ON_OFF(self, bank, f):
        if f =='on':
            bank.loan_feature_enabled == True
            print('loan feature on')
        else:
            bank.loan_feature_enabled == False
            print('loan feature off')

        
bank=Bank()

admin = Admin('meher',"meher@gmail.com","bogura",)
user= Acount_Holder('fariha',"fariha@gmail.com","rajshahi","current")





while True:

    
    print("WelCome To BMS")
    

    print("1. USER")
    print("2. ADMIN")
    print("3. Exit")

    choice2=int(input())
    if choice2 == 1:
        
        while True:
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Widthdraw Money")
            print("4. Check Avilable Balance")
            print("5. Check transaction history")
            print("6. Take a loan")
            print("7. Transfer Money")
            print("8. Exit")
            choice2=int(input())
            if choice2 == 1:
                name = input("please Enter name: ")
                email = input("please Enter email: ")
                addres = input("please Enter addres: ")
                account_type = input("please Enter account_type: ")
                user = Acount_Holder(name,email,addres,account_type)
                user.create_account(bank)

            elif choice2 == 2:
                amount =int(input("Enter Amount: "))
                user.deposite(bank,amount)
            elif choice2 == 3:
                amount =int(input("Enter Amount: "))
                user.withdraw(bank,amount)
            elif choice2 == 4:
                user.check_balance()
            elif choice2 == 5:
                user.check_transaction_history()
            elif choice2 == 6:
                amount =int(input("Enter Amount: "))
                user.request_loan(bank,amount)
            elif choice2 == 7:
                account_number =input("Enter Account Number: ")
                amount =int(input("Enter Amount: "))
                user.transfer(bank,account_number,amount)
            elif choice2 == 8:
                break
            else:
                print("Invalid Choice")
    elif choice2 == 2:
        
        print(f"WelCome To Banking System {admin.name}")
        
        while True:
            print("1. Create An Account")
            print("2. Delete Any User Account")
            print("3. See All User Accounts List")
            print("4. Check the total available balance of the bank")
            print("5. Check the total loan Amount")
            print("6. Loan feature of the bank(on or of)")
            print("7. Exit")
            choice1=int(input())
            if choice1 == 1:
                name = input("please Enter name: ")
                email = input("please Enter email: ")
                addres = input("please Enter addres: ")
                account_type = input("please Enter account_type: ")
                admin.create_account(bank,name,email,addres,account_type)
            elif choice1 == 2:
                account_number=input("Enter account number: ")
                admin.delete_account(bank,account_number)
            elif choice1 == 3:
                admin.view_all_accounts(bank)

            elif choice1 == 4:
                admin.check_total_bank__balance(bank)

            elif choice1 == 5:
                admin.check_total_loan_amount(bank)

            elif choice1 == 6:
                f=input("Type (on or off): ")
                admin.loan_feature_ON_OFF(bank,f)
            elif choice1 == 7:
                break
            else:
                print("Invalid Choice")
    elif choice2 == 3:
        break
    else:
        print("invalid number")