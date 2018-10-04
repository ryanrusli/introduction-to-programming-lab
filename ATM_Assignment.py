#ATM Class and System
#Ryan Rusli 2201725411

#----------------------


import random
import os

class ATM:
    def __init__(self,ID,balance,wallet):
        self.ID = str(ID)
        self.balance = int(balance)
        self.wallet = int(wallet)
                 
    def withdrawMoney(self,amount):
        data = open("Accounts.txt", "r+")
        lines = data.readlines()
        found = False
        pin = input("Please reconfirm with your pin: ")
        for i in range(len(lines)-2):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            if self.ID == lines[i]:
                found = True
                if self.balance > amount:
                    new = self.balance - amount
                    self.wallet += amount
                    old = lines[i+2]
                    print("Your balance has been decreased to",new)
                    print("Wallet =",self.wallet)
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

    def depositMoney(self,amount):
        data = open("Accounts.txt", "r+")
        lines = data.readlines()
        found = False
        pin = input("Please reconfirm with your pin: ")
        for i in range(len(lines)-2):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            if self.ID == lines[i]:
                found = True
                if self.wallet >= amount:
                    new = int(lines[i+2]) + amount
                    self.wallet -= amount
                    old = lines[i+2]
                    print("Your new balance is",new)
                    new = str(new)
                    print("Wallet:",self.wallet)
                elif self.wallet < amount:
                    print("Not enough cash!")
        data.seek(0)
        data.truncate()
        prevline =''
        for line in lines:
            if line == old and pin == prevline:
                data.write(new+"\n")
            else:
                data.write(line+"\n")
            prevline = line
            
    def debit(self,amount):
        data = open("Accounts.txt", "r+")
        lines = data.readlines()
        found = False
        pin = input("Please reconfirm with your pin: ")
        for i in range(len(lines)-2):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            if self.ID == lines[i]:
                found = True
                if self.balance > amount:
                    new = self.balance - amount
                    old = lines[i+2]
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

    def TransferMoney(self,transferID):
        data = open("Accounts.txt", "r+")
        lines = data.readlines()
        found = False
        for line in range(len(data)):
            if transferID == line:
                amount = int(input("Input the amount you would like to transfer: "))
                if amount >=0:
                    found = True
                    data[line+2] += amount
                    print("Amount successfully transferred.")
                else:
                    print("Invalid amount!")
        if found == False:
            print("Account ID not found")

class Account:        
    def createAccount(self):
        newID = ''
        count = 0
        balance = 0
        while count < 8:
            newID += str(random.randint(0,9))
            count += 1
        newID = int(newID)
        print("Your account ID is",newID,"\nPlease note it down.")
        confirmed = False
        while confirmed == False:
            pin = input("Please create a pin(6 digits): ")
            pincheck = input("Reconfirm your pin: ")
            if pin == pincheck:
                confirmed = True
                print("Pins are the same.")
                print("Account creation success!")
                pin = int(pin)
            else:
                print("Pins are not the same, please recheck")
        return newID,pin,balance

    def checkcard(self,login):
        data = open("Accounts.txt", "rt")
        lines = data.readlines()
        found = False
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip("\n")
            lines[i+1] = lines[i+1].rstrip("\n")
            lines[i+2] = lines[i+2].rstrip("\n")
            if login == lines[i] :
                found = True
                pin = str(input("Input your pin: "))
                if pin == lines[i+1]:
                    print("Login successs!")
                    print(lines[i+1])
                    return True
                    break
                else:
                    print("Incorrect PIN")
                    print(lines[i+1])
        if found == False:
            print("Account ID not found.")
            return False
                    
    def getBalance(self,login):
        data = open("Accounts.txt", "rt")
        data = data.read()
        data = data.split()
        found = False
        for line in range(len(data)):
            if login == data[line]:
                balance = data[line+2]
                return balance

def main():
    f = open("Accounts.txt" , "a+")
    x = input("Is this your first time using this system? [y/n] ")
    start = Account()
    if x == "y":
        newAccount = start.createAccount()
        f.flush()
        os.fsync(f.fileno())
        for i in newAccount:           
            f.write("%s\n"%i)
        
    
    login = str(input("Input your login id: "))
    
    
    checked = start.checkcard(login)
    if checked:
        balance = start.getBalance(login)
        wallet = int(input("Input wallet amount: "))
        service = ATM(login,balance,wallet)
        option = int(input("1.Withdraw\n2.Deposit\n3.Debit\n4.Transfer\n"))
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
            TransferMoney(transferID)

    
            

    f.flush()
    os.fsync(f.fileno())
    f.close()
    
    
        
main()
    
