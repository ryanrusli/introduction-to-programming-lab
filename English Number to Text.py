x = int(input("Input number: "))
        
numlist = ('','one','two','three','four','five','six','seven',
           'eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
           'sixteen','seventeen','eighteen','nineteen')
tens = ('','','twenty-','thirty-','fourty-','fifty-','sixty-','seventy-','eighty-','ninety-')
if x <= 19:
    print(numlist[x])
elif x < 30:
    x = str(x)
    a = int(x[-1])
    print("twenty " + numlist[a])
elif x < 40:
    x = str(x)
    a = int(x[-1])
    print("thirty " + numlist[a])
elif x <= 99:
    x = str(x)
    a = int(x[-1])
    b = int(x[0])
    print(tens[b] + numlist[a])
elif x <= 999:
    x = str(x)
    if int(x[1:]) < 20:
        b = int(x[1:])
        a = int(x[0])
        print(numlist[a] + " hundred " + numlist[b])
    else:
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])
        print(numlist[a] + " hundred " + tens[b] + numlist[c])
  

