#Lambda Calculator
#Ryan Rusli 2201832446

#----------------------

#definition of each operator

add = lambda a,b : a+b

subtract = lambda a,b : a-b

multiply = lambda a,b : a*b

divide = lambda a,b : a/b

#main function
def main():
    run = True
    a = int(input("Input num1: "))
    while run == True:
        
        
        b = int(input("Input num2: "))
        op = input("Input the operator, or 'q' if you want to stop: ")

        
        if op == "+":
            result = add(a,b)       #adds a and b
            print(result)
        elif op == "-":
            result = subtract(a,b)  #subtracts a and b
            print(result)
        elif op == "*":
            result = multiply(a,b)  #multiplies a and b
            print(result)
        elif op == "/":
            result = divide(a,b)    #divides a by b
            print(result)
        elif op == "q":             #checks if the operator is equal to q
            run = False
            print("The final answer is ",result)
            break               # ends the while loop
            

                                   #updates the value of a to result
        a = result 

        
        
        
main()
