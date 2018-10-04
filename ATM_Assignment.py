#ATM Class and System
#Ryan Rusli 2201725411

#----------------------


import random
import os

class BankServices:     #class for all the function in a ATM
    def __init__(self,ID,balance):
        self.ID = str(ID)
        self.balance = int(balance)

    def checkBalance(self):
        print("Your balance is",self.balance)
        return self.balance
    
    def withdrawMoney(self,amount):     #removes money from the balance
        data = open("Accounts.txt", "r+")       #opens the text file to be read and written
        lines = data.readlines()
        found = False
        pin = input("Please reconfirm with your pin: ")
        for i in range(len(lines)-4):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            lines[i+3] = lines[i+3].rstrip("\n")
            lines[i+4] = lines[i+4].rstrip("\n")
            if self.ID == lines[i]:
                found = True
                if self.balance > amount:
                    new = self.balance - amount
                    old = str(self.balance)
                    print("Your balance has been decreased to",new)
                    new = str(new)
                elif amount > self.balance:
                    print("Insufficient balance!")
        data.seek(0)
        data.truncate()
        prevline =''
        for line in lines:
            if line == old and pin == prevline:
                data.write(new+"\n")
            else:
                data.write(line+"\n")
            prevline = line
    
    def depositMoney(self,amount):              #adds money to the balance
        data = open("Accounts.txt", "r+")       #opens the text file to be read and written
        lines = data.readlines()
        found = False
        pin = input("Please reconfirm with your pin: ")
        for i in range(len(lines)-4):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            lines[i+3] = lines[i+3].rstrip("\n")
            lines[i+4] = lines[i+4].rstrip("\n")
            if self.ID == lines[i]:
                found = True
                new = self.balance + amount
                old = self.balance
                print("Your new balance is",new)
                old = str(old)
                new = str(new)
        data.seek(0)
        data.truncate()
        prevline =''
        for line in lines:
            if line == old and pin == prevline:
                data.write(new+"\n")
            else:
                data.write(line+"\n")
            prevline = line
            
    def debit(self,amount):                     #removes money from the account to debit
        data = open("Accounts.txt", "r+")       #opens the text file to be read and written
        lines = data.readlines()
        found = False
        pin = input("Please reconfirm with your pin: ")
        for i in range(len(lines)-4):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            lines[i+3] = lines[i+3].rstrip("\n")
            lines[i+4] = lines[i+4].rstrip("\n")
            if self.ID == lines[i]:
                found = True
                if self.balance > amount:
                    new = self.balance - amount
                    old = self.balance
                    print("Your balance has been decreased to",new)
                    old = str(old)
                    new = str(new)
                elif amount > self.balance:
                    print("Insufficient balance!")
        data.seek(0)
        data.truncate()
        prevline =''
        for line in lines:
            if line == old and pin == prevline:
                data.write(new+"\n")
            else:
                data.write(line+"\n")
            prevline = line

    def TransferMoney(self,login,transferID):         #transfers money to another function
        data = open("Accounts.txt", "r+")       #opens the text file to be read and written
        lines = data.readlines()
        found = False
        for i in range(len(lines)-4):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            lines[i+3] = lines[i+3].rstrip("\n")
            lines[i+4] = lines[i+4].rstrip("\n")
            if transferID == lines[i]:
                amount = int(input("Input the amount you would like to transfer: "))
                pin = input("Input pin to confirm: ")
                if amount >= 0 and self.balance>amount:
                    found = True
                    transfer_oldbalance = self.balance
                    transfer_newbalance = transfer_oldbalance + amount
                    transferee = lines[i+3]
                    transfer_newbalance = str(transfer_newbalance)
                    transfer_oldbalance = str(transfer_oldbalance)
                    print("Amount successfully transferred to",transferee,".")
                else:
                    print("Insufficient amount or invalid amount!")
            elif login == lines[i]:
                my_oldbalance = self.balance
                my_newbalance = my_oldbalance - amount
                my_oldbalance = str(my_oldbalance)
                my_newbalance = str(my_newbalance)
        if found == False:
            print("Account ID not found")
        elif found ==True:
            data.seek(0)
            data.truncate()
            prevline =''
            for line in lines:
                if line == my_oldbalance and prevline == pin:
                    data.write(my_newbalance + "\n")
                elif line == transfer_oldbalance:
                    data.write(line.replace(transfer_oldbalance,transfer_newbalance)+ "\n")
                else:
                    data.write(line + "\n")
                prevline = line
                               
                    
            

class Account:                  #Account Class
    def createAccount(self):    #function to create account
        newID = ''
        count = 0
        balance = 0
        while count < 8:
            newID += str(random.randint(0,9))
            count += 1
        newID = int(newID)
        firstname = input("Please input your first name: ")
        lastname = input("Please input your last name: ")
        print("Your account ID is",newID,"\nPlease note it down.")
        confirmed = False
        while confirmed == False:
            pin = input("Please create a pin(6 digits): ")
            pincheck = input("Reconfirm your pin: ")
            if pin == pincheck:
                confirmed = True
                print("Pins are the same.")
                print("Account creation success!")
                print("Thank you for registering,",firstname)
                pin = int(pin)
            else:
                print("Pins are not the same, please recheck")
        return newID,pin,balance,firstname,lastname

    def checkcard(self,login):      #checks login credentials
        data = open("Accounts.txt", "rt")
        lines = data.readlines()
        found = False
        for i in range(len(lines)-4):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            lines[i+3] = lines[i+3].rstrip("\n")
            lines[i+4] = lines[i+4].rstrip("\n")
            if login == lines[i] :
                found = True
                pin = str(input("Input your pin: "))
                if pin == lines[i+1]:
                    print("Login successs!")
                    print("Good day,", lines[i+3])
                    return True
                    break
                else:
                    print("Incorrect PIN")
                    break
        if found == False:
            print("Account ID not found.")
            return False
                    
    def getBalance(self,login):     #collects the balance
        data = open("Accounts.txt", "rt")
        data = data.read()
        data = data.split()
        found = False
        for line in range(len(data)):
            if login == data[line]:
                balance = data[line+2]
                return balance

def main():     #main function
    f = open("Accounts.txt" , "a+")
    x = input("Is this your first time using this system? [y/n] ")
    start = Account()
    if x == "y":
        newAccount = start.createAccount()
        for i in newAccount:           
            f.write("%s\n"%i)

        f.flush()
        os.fsync(f.fileno())
        
    
    login = str(input("Input your login id: "))
    
    checked = start.checkcard(login)                    #checks login credentials, returns boolean value

    if checked:
        balance = start.getBalance(login)
        service = BankServices(login,balance)
        option = int(input("1.Withdraw\n2.Deposit\n3.Debit\n4.Transfer\n5.Check Balance\n"))     #services in the bank
        if option == 1:
            amount = int(input("Input withdraw amount: "))
            service.withdrawMoney(amount)
        elif option == 2:
            amount = int(input("Input deposit amount: "))
            service.depositMoney(amount)
        elif option == 3:
            amount = int(input("Input transfer amount: "))
            service.debit(amount)
        elif option == 4:
            transferID = input("Input the ID you are transferring to: ")
            service.TransferMoney(login,transferID)
        elif option == 5:
            service.checkBalance()

    
            

    f.flush()
    os.fsync(f.fileno())
    f.close()
