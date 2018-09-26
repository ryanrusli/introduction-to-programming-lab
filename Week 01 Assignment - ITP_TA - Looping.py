for i in range(1,6):                #i is a loop for the number of rows, and continues looping while the number of rows is less than 6
    print("*"*i)                    #prints an "*" on the line multiplied by the current row numbre
print("\n")                         #creates a new line to seperate this triangle from the next
                                    #this creates a right angle triangle



for i in range(1,6):                #i is a loop for the number of rows, and continues looping while the number of rows is less than 6
    print(" "*(6-i), "*"*i)         #prints a space multiplied by (6 subtracted by the current row number) followed by printing an "*" on the line multiplied by the row number it is on
print("\n")                         #creates a new line to seperate this triangle from the next
                                    #this creates a mirrored right angle triangle


for i in range(5,0,-1):             #i is a loop for the number of rows, and loops downwards from 5 to 1
    print("*"*i)                    #prints an "*" on the line multiplied by the current row number
print("\n")                         #creates a new line to seperate this triangle from the next
                                    #this creates an upside down right angle triangle


s = 0                               #initialises s, s is a counter for the number of spaces
for i in range(1,6):                #i is a loop for the number of rows, and continues looping while the number of rows is less than 6 
    print((s)*(" "), "*"*(6-i))     #prints " " by the number of spaces 's', followed by printing a n"*" multiplied by (6 subtracted by the current row number)
    s += 1                          #increments the value of s by 1
print("\n")                         #creates a new line to seperate this triangle from the next
                                    #this creates a mirrored upside down right angle triangle



for i in range(1,6):                #i is a loop for the number of rows, and continues looping while the number of rows is less than 6 
    print(" "*(6-i), "*"*(i*2-1))   #prints a " " multiplied by (6 subtracted by the current row number), followed by an "*" multiplied by 2 and the current row number, 
                                    #then subtracted by one to prevent the pyramid from having an even number of stars on each line 
print("\n")                         #creates a new line to seperate this triangle from the next
                                    #this creates a pyramid

    
    
for i in range(1,6):                #i is a loop for the number of rows of the pyramid, and continues looping while the number of rows is less than 6 
    print(" "*(5-i), "*"*(i*2-1))   #prints a " " multiplied by (5 subtracted by the current row number), followed by an "*" multiplied by 2 and the current row number, 
                                    #and subtracted by one to prevent the pyramid from having an even number of stars on each line 
                                    #this creates the upwards pyramid
            
for q in range(1,5):                #q is a loop for the number of rows of the downwards pyramid, and continues looping while the number of rows is less than 5
    print(" "*(q), "*"*(2*(5-q)-1)) #prints a " " multiplied by the current row number of the downwards pyramid, followed by an "*" multiplied by 2 and (5 subtracted by the current row number)
                                    #and subtracted by 1 again to prevent an even number of "*" on the line
                                    #this creates the downwards pyramid
                                       
                                    #the two previous loops will form a diamond
