#Calculator Class
#Ryan Rusli 2201832446

#---------------------

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        return result
    def subtract(self):
        result = self.num1 - self.num2
        return result
    def multiply(self):
        result = self.num1 * self.num2
        return result
    def divide(self):
        result = self.num1/self.num2
        return result
def main():
    run = True
    while run == True:
        num1 = int(input("input number 1: "))

        num2 = int(input("input number 2: "))

        op = input("Input operator: ")

        solution = Calculator(num1,num2)

          
        if op == "+":
            result = solution.add()      #adds a and b
            print(result)
        elif op == "-":
            result = solution.subtract() #subtracts a and b
            print(result)
        elif op == "*":
            result = solution.multiply()  #multiplies a and b
            print(result)
        elif op == "/":
            result = solution.divide()   #divides a by b
            print(result)

        continuE = input("Continue? [y/n] ")
        if continuE == "n":
            run = False

    
main()
