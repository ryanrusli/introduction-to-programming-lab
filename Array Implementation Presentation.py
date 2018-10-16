
#5

arr = []
#initialises the array "arr"

x = input("Input Numbers\n"
          "Include spaces :\n")
#inputs the numbers for the array

arr = x.split(" ")
#splits the input x by each " " detected, and places each seperated input into the array

key = input("Input key: ") 3
#inputs the key

found = False
while found == False:                       #loops while found is False 
    for index in range(len(arr)):           #loops through while index is between 0 and the length of the array
        if arr[index] == key:               #checks if the the number in the array according to the index is equal to the key
            print("Found at index",index) 
            found = True                    #sets found to True, and ends the loop
            break

if found == False:                          #checks if found is False
    print("Not Found")


 
