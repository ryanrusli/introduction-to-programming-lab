x = int(input("Input number: "))
        
numlist = ('','one','two','three','four','five','six','seven',
           'eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
           'sixteen','seventeen','eighteen','nineteen')
tens = ('','','twenty-','thirty-','fourty-','fifty-','sixty-','seventy-','eighty-','ninety-')

if x <= 19:     #checks if the x is less than or equal to 19
    print(numlist[x])   #prints the text in numlist according to the index "x"(the input)

elif x < 30:            #checks if the x is less than 30
    x = str(x)        #converts to string so it can be sliced      
    a = int(x[-1])     #slices and takes the last digit in variable x, and converts it to a integer             
    print("twenty " + numlist[a])   #prints out "twenty" adds the string with a text in the num list to the index

elif x < 40:                   #checks if the x is less than 40
    x = str(x)        
    a = int(x[-1])      #slices and takes the last digit in variable x, and converts it to a integer
    print("thirty " + numlist[a])   #prints out "thirty" adds the string with a text in the num list to the index

elif x <= 99:                  #checks if the x is less than or equal to 99
    x = str(x)  
    a = int(x[-1])      #slices and takes the last digit in variable x, and converts it to a integer
    b = int(x[0])       #slices and takes the first digit in variable x, and converts it to a integer
    print(tens[b] + numlist[a]) #prints the text in the "tens" tuple according to the first digit of variable x, and adds it to the text in the --
                                #->numlist tuple according to the last digit in variable x

elif x <= 999:                 #checks if the x is less than or equal to 999
    x = str(x)
    if int(x[1:]) < 20: #checks if the last two digits combined in x are below 20
        b = int(x[1:])  #slices and takes the last two digits in x
        a = int(x[0])   #takes the first digit in x
        print(numlist[a] + " hundred " + numlist[b])# prints out the text according to index a(first digit in x) in numlist, which is the first digit in variable x,
                                                    #add it to the string " hundred ", and the index b(last two digits in x) in numlist 
                                                    
    else:
        a = int(x[0])   #slices the first digit in variable x
        b = int(x[1])   #slices the second digit in variable x
        c = int(x[2])   #slices the third digit in variable x
        print(numlist[a] + " hundred " + tens[b] + numlist[c]) #prints out the text according to index a(first digit in x) in numlist, added to the string " hundred "
                                                                #and added to index b(second digit in x) in the "tens" tuple also added to
                                                                #index c(third digit in x) in numlist
                                  

