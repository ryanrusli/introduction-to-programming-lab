import matplotlib.pyplot as plt
from operator import itemgetter
from collections import OrderedDict

sortedvalues = []
sortedkeys = []  

maxi = 0

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


wordlist = OrderedDict(sorted(wordlist.items(), key=itemgetter(1)))

for item in wordlist.values():
    sortedvalues.append(item)
for item in wordlist.keys():
    sortedkeys.append(item)

    
sortedkeys = sortedkeys[-1:-11:-1]

sortedvalues = sortedvalues[-1:-11:-1]

plt.plot(sortedkeys,sortedvalues,"o")

plt.show()

