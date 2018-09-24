for i in range(1,6):
    print("*"*i)                    #normal right angle triangle
print("\n")


for i in range(1,6):
    print(" "*(6-i), "*"*i)        #mirrored triangle
print("\n")


for i in range(5,0,-1):
    print("*"*i)                    #upside down right angle triangle
print("\n")


s = 0                               #s is a counter for the number of spaces
for i in range(1,6):    
    print((s)*(" "), "*"*(6-i))     #mirrored upside down triangle
    s += 1              
print("\n")

for i in range(1,6):
    print(" "*(6-i), "*"*(i*2-1))  #full triangle/pyramid
print("\n")

for i in range(1,6):
    print(" "*(5-i), "*"*(i*2-1))   #this creates the upwards triangle
for q in range(1,5):
    print(" "*(q), "*"*(2*(5-q)-1))  #this creates the downwards triangle
                                    #diamond


