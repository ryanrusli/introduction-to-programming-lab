#Ryan Rusli - 2201832446

#------------------------------
import matplotlib.pyplot as plt
import math as m
import numpy as np
import sys
#------------------------------

def plotpointer(v,theta):   #function to plot the points individually
    r = theta * (m.pi/180)  #converts degrees to radian
    g = 9.8                 #gravity constant
    maxy = v*m.sin(r)       #calculates max y
    maxt = maxy*2/g         #calculates the time
    xmax = 0
    ymax = 0
    t = np.linspace(0, maxt, num=1000)   #time is divided into 1000 points
    xAX = []
    yAX = []
    for k in t:         #loops for every point in the 1000 points
        xcoo = ((v*k)*m.cos(r))
        ycoo = ((v*k)*m.sin(r))-((0.5*g)*(k**2))
        xAX.append(xcoo)    #adds it to the x points list
        yAX.append(ycoo)    #adds it to the y points list

    plt.plot(xAX,yAX,label = str(v) + " m/s, " + str(theta) + " degrees")
    #plots the graph and labels it with the speed and angle input
    

# main function
try:
    trnum = int(input("Input number of trajectories: "))    
except ValueError:  # in the case of a wrong input
    print("Invald Input!")
    sys.exit()      #ends the code
for count in range(0,trnum):
    try:
        print("Input initial velocity (m/s)",count+1,":",end = " ")
        v = int(input(""))
        print("Input angle of projection (degrees)",count+1,":",end = " ")
        theta = int(input(""))
        plotpointer(v,theta)
        
    except ValueError:
        print("There was an invalid input!")
        sys.exit()  


plt.xlabel("X Distance Travelled",fontsize = 11)
plt.ylabel("Y Distance Travelled", fontsize = 11)
plt.legend()
plt.show()  




