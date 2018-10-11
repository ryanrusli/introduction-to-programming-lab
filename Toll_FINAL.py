#Ryan Rusli - 2201832446
#Assignment 4 - TOLL

#VERSION 4
#--------------------


class TollGate: # tollgate class
    def __init__(self,name,cprice,bprice,tprice):   #creates the name of the gate, and the prices for each category of car,bus,truck
        self.location = name
        self.carprice = cprice
        self.busprice = bprice
        self.truckprice = tprice

    def getgate(self):                          #returns the name of the gate
        return self.location

    def getcp(self):                            #returns the fee for the car
        return self.carprice

    def getbp(self):                            #returns the fee for the bus
        return self.busprice

    def gettp(self):                            #returns the fee for the truck
        return self.truckprice

    def header(self):
        print("================================================================================\n"
              "                               Toll Payment Systems                             \n"
              "                               PT Jasa Marga, Tbk.                              \n"
              "================================================================================\n"
              "                                  ",self.location,"Gate                            \n")                                  

    def totalgaterevenue(self,s1,s2,s3,s4,s5):          #calculates the total revenue of the gate
        total = s1+s2+s3+s4+s5

        
        return total

    
    def totalvehicles(self,v1,v2,v3,v4,v5):         #calculates the total number of vehicles in the gate
        total = v1+v2+v3+v4+v5
        print("The total amount of vehicles is ",total,"\n")
        return total
    

class Vehicles(TollGate):           #class for vehicles
    def __init__(self,name,cprice,bprice,tprice,vehicle):
        super().__init__(name,cprice,bprice,tprice)
        self.vehicle = int(vehicle)
	
    def identify(self):             #identifies what vehicle it is based on user input later in the code, and outputs the fee and makes an input for a payment method
        if self.vehicle == 1:       
            print("Fee is RP",self.carprice,"\n")
            pmethod = input("Would you like to pay in cash or card?\n")
		
        elif self.vehicle == 2:
            print("Fee is RP",self.busprice,"\n")
            pmethod = input("Would you like to pay in cash or card?\n")

		
        elif self.vehicle == 3:
            print("Fee is RP",self.truckprice,"\n")
            pmethod = input("Would you like to pay in cash or card?\n")




class TollBooth(TollGate):          #class for TollGate
    def __init__(self):
        self.carcount = 0
        self.buscount = 0
        self.truckcount = 0            
        
    def totalboothfares(self,cp,bp,tp):     #calculates the amount of money that specific toll booth makes, and returns the total
        total = ((self.carcount * cp)
                + (self.buscount * bp)
                + (self.truckcount * tp))
    	
        return total

    
    
    def printvehiclecount(self,y):                          #prints out the total amount of vehicles by category(car,bus,truck), and also the total number of vehicles for the booth
        amount = self.carcount + self.buscount + self.truckcount

        print("Car count for booth",y,"is",self.carcount,"\n")        
        print("Bus count for booth",y,"is",self.buscount,"\n")
        print("Truck count for booth",y,"is",self.truckcount,"\n")
        print("The total amount of vehicles is",amount,"\n")
    
    def gettotalvehiclecount(self):                             #returns the total amount of vehicles in a toll booth
        amount = self.carcount + self.buscount +self.truckcount
        return amount


        
    def getvehicledata(self,x,y):                           #function to update the count for each vehicle category
        if x == 1:
            self.carcount += 1
        elif x == 2:
            self.buscount += 1
        elif x == 3:
            self.truckcount += 1


# MAIN FUNCTION
newgate = True                      
summ = 0

while newgate:          #loops while there still a new gate/location being added to the program
    
    place = input("Input location: ")       #input for the gate/location name
    cp = int(input("Input Car fee: RP"))
    bp = int(input("Input Bus fee: RP"))
    tp = int(input("Input Truck fee: RP"))
    print("\n")

    gate = TollGate(place,cp,bp,tp)

    run = True

    tb1 = TollBooth()
    tb2 = TollBooth()
    tb3 = TollBooth()
    tb4 = TollBooth()
    tb5 = TollBooth()           #initalises 5 different toll booths

    while run:      #loop to repeat input of vehicles
        print("Select your vehicle category.\n")
        print("     1.Car  ( RP",gate.getcp(),")\n",
              "    2.Bus  ( RP",gate.getbp(),")\n",
              "    3.Truck( RP",gate.gettp(),")\n")

        x = int(input(""))                  #x is an input for which vehicles is selected
        vehicle = Vehicles(place,cp,bp,tp,x)
        vehicle.identify()                  
        y = int(input("Select a booth.\n"           #y is an input for which booth is selected  
                      "Booth 1\n"
                      "Booth 2\n"
                      "Booth 3\n"
                      "Booth 4\n"
                      "Booth 5\n"
                      "Input a number."))
        if y == 1:
            gate.header() 
            tb1.getvehicledata(x,y)             #updates the counter for booth 1 based on the vehicle input in variable x

        elif y == 2:
            gate.header() 
            tb2.getvehicledata(x,y)             #updates the counter for booth 2 based on the vehicle input in variable x

        elif y == 3:
            gate.header() 
            tb3.getvehicledata(x,y)         #updates the counter for booth 3 based on the vehicle input in variable x

        elif y == 4:
            gate.header() 
            tb4.getvehicledata(x,y)             #updates the counter for booth 4 based on the vehicle input in variable x

        elif y == 5:
            gate.header() 
            tb5.getvehicledata(x,y)             #updates the counter for booth 5 based on the vehicle input in variable x


        running = input("Are there any other cars? [Y/N]\n")        #input to stop or continue input of cars
        if running.lower() == "n":
            run = False

    print("\nData has been successfully collected!")
    more = True

    s1 = tb1.totalboothfares(cp,bp,tp)
    s2 = tb2.totalboothfares(cp,bp,tp)
    s3 = tb3.totalboothfares(cp,bp,tp)
    s4 = tb4.totalboothfares(cp,bp,tp)
    s5 = tb5.totalboothfares(cp,bp,tp)          #calculates the total revenue for booths 1 to 5

    while more:
        print("What would you like to do?\n"
              "1.Get total revenue for one booth.\n"
              "2.Get total revenue for the gate.\n"
              "3.Get total number of each vehicle in a toll booth.\n"
              "4.Get total number of each vehicle in the gate.\n")

        info = int(input(""))
        
        if info == 1:
            Bno = int(input("Which booth would you like to access?\n"           #Bno stands for Booth Number
                            "Booth 1\n"
                            "Booth 2\n"
                            "Booth 3\n"
                            "Booth 4\n"
                            "Booth 5\n"))
            gate.header()
            

            if Bno == 1:
                print("The total revenue for this booth is RP",s1)
            elif Bno == 2:
                print("The total revenue for this booth is RP",s2)
            elif Bno == 3:
                print("The total revenue for this booth is RP",s3)
            elif Bno == 4:
                print("The total revenue for this booth is RP",s4)
            elif Bno == 5:
                print("The total revenue for this booth is RP",s5)     #prints out the statement with the revenue for the booth input in "Bno"         
                         
        elif info == 2:
            x = gate.totalgaterevenue(s1,s2,s3,s4,s5)       #calculates the sum of the revenue of all 5 booths
            gate.header()
            print("The total revenue for the gate is RP ",x,"\n")

        elif info == 3:
            Bno = int(input("Which booth would you like to access?\n"           #Bno stands for Booth Number
                            "Booth 1\n"
                            "Booth 2\n"
                            "Booth 3\n"
                            "Booth 4\n"
                            "Booth 5\n"))

            if Bno == 1:
                gate.header()

                tb1.printvehiclecount(Bno)
                
            elif Bno == 2:
                gate.header()
                tb2.printvehiclecount(Bno)

            elif Bno == 3:
                gate.header()
                tb3.printvehiclecount(Bno)

            elif Bno == 4:
                gate.header()
                tb4.printvehiclecount(Bno)

            elif Bno == 5:
                gate.header()
                tb5.printvehiclecount(Bno)              #prints out the number of each vehicle category and the total number of cars for the booth
                
        elif info == 4:
            t1 = tb1.gettotalvehiclecount()
            t2 = tb2.gettotalvehiclecount()
            t3 = tb3.gettotalvehiclecount()
            t4 = tb4.gettotalvehiclecount() 
            t5 = tb5.gettotalvehiclecount()             #gets the total number of vehicles for booths 1-5
            gate.header()
            gate.totalvehicles(t1,t2,t3,t4,t5)          #calculates the total number of vehicles for the gate/location
            



            
        continuee = input("Would you like to continue viewing data? [Y/N]\n")

        if continuee.lower() == "n":            #loop to continue checking other data
            more = False
    z = gate.totalgaterevenue(s1,s2,s3,s4,s5)   #re-obtains the total revenue for the gate
    summ += z                                   #adds the revenue for the gate/location to the grand total revenue of all the gates/locations
    print("GRAND TOTAL REVENUE: RP",summ)
    anothergate = input("Are there anymore gates?[Y/N]\n")        #if input is anything other than "n", creates a new gate/location
    if anothergate.lower() == "n":
        newgate = False
        
    
    
                 
                    







