import matplotlib.pyplot as plt
from operator import itemgetter
from collections import OrderedDict

sortedvalues = []
sortedkeys = []  

x = open("Robinhood.txt","r")   #opens the Robinhood text to be read
x = x.read()        #copies the file contents and inputs it in x
y = []
wordlist = {}       #dictionary to list all the word
x = x.lower()       #lowercases all the letters

x = (x.replace(","," ").replace('"'," ").replace("-"," ").replace("\""," ").replace("_"," ").replace('\"' ," ")
     .replace("."," ").replace(":"," ").replace(";"," ").replace("/"," ").replace("("," ").replace(")"," ")
     .replace("!"," ").replace("?"," "))
#removes all the unused characters for the word count to be more accurate

y = x.split()

#splits the words after a space and appends it in array y

maxdict = {}



for word in y:                  #for each word in the array y
    if word in wordlist:        #checks if the word is already in the dictionary
        wordlist[word] += 1   #if it is, increases the count of the word by 1
    else:
        wordlist[word] = 1#if not, sets the word count to one and adds the word to the dictionary


wordlist = OrderedDict(sorted(wordlist.items(), key=itemgetter(1))) #orders the values of the dictionary in ascending order

for item in wordlist.values():     #loops through every single value in the dictionary
    sortedvalues.append(item)       #appends each value in ascending order
for item in wordlist.keys():        #loops through every single key in the dictionary
    sortedkeys.append(item)         #appends each key according to the value of it in ascenfing order

    
sortedkeys = sortedkeys[-1:-11:-1] #takes the last 10 keys in the list, which has the highest value number for the respective keys

sortedvalues = sortedvalues[-1:-11:-1] #takes the last 10 values in the list, which is the highest in value number

plt.plot(sortedkeys,sortedvalues,"o")   #plots the graph with the keys in the x axis, values in the y axis, uses a dot to represent the values

plt.show()          #outputs the graph

