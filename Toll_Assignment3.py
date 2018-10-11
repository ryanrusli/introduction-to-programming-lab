#Ryan Rusli - 2201832446
#Assignment 4 - TOLL

#VERSION 3
#--------------------



class TollGate: # tollgate class
    def __init__(self,cprice,bprice,tprice):   #creates the name of the gate, and the prices for each category of car,bus,truck
        self.carprice = cprice
        self.busprice = bprice
        self.truckprice = tprice

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


class Vehicles(TollGate):           #class for vehicles
    def __init__(self,cprice,bprice,tprice,vehicle):
        super().__init__(cprice,bprice,tprice)
        self.vehicle = int(vehicle)
	
    def identify(self):             #identifies what vehicle it is based on user input later in the code, and outputs the fee 
        if self.vehicle == 1:       
            print("Fee is RP",self.carprice,"\n")
		
        elif self.vehicle == 2:
            print("Fee is RP",self.busprice,"\n")

		
        elif self.vehicle == 3:
            print("Fee is RP",self.truckprice,"\n")

class TollBooth(TollGate):          #class for TollGate
    def __init__(self):
        self.carcount = 0
        self.buscount = 0
        self.truckcount = 0            
        
    def totalboothfares(self,cp,bp,tp):     #calculates the amount of money that specific toll booth makes, and returns the total
        total = ((self.carcount * cp)
                + (self.buscount * bp)
                + (self.truckcount * tp))
        print("GRAND TOTAL REVENUE: RP",total)
        return total

    
    
    def printvehiclecount(self):                          #prints out the total amount of vehicles by category(car,bus,truck), and also the total number of vehicles for the booth
        amount = self.carcount + self.buscount + self.truckcount

        print("Car count for the booth is",self.carcount,"\n")        
        print("Bus count for booth is",self.buscount,"\n")
        print("Truck count for booth is",self.truckcount,"\n")
        print("The total amount of vehicles is",amount,"\n")

    def getvehicledata(self,x):                           #function to update the count for each vehicle category
        if x == 1:
            self.carcount += 1
        elif x == 2:
            self.buscount += 1
        elif x == 3:
            self.truckcount += 1
def main():
    gate = TollGate(place,cp,bp,tp)
    gate.header()
    run = True
    booth = TollBooth()
    while run:      #loop to repeat input of vehicles
        print("Select your vehicle category.\n")
        print("     1.Car  ( RP",gate.getcp(),")\n",
              "    2.Bus  ( RP",gate.getbp(),")\n",
              "    3.Truck( RP",gate.gettp(),")\n")

        x = int(input(""))
        vehicle = Vehicles(cp,bp,tp,x)
        vehicle.identify()
        booth.getvehicledata(x)
        continues = input("Any more vehicles? [y/n]\n")
        if continues.lower() == "n":
            gate.header()
            print("LOCATION: ",place)
            booth.printvehiclecount()
            booth.totalboothfares(cp,bp,tp)
            run = False
#main function

moregates = True
while moregates:
    place = input("Input location: \n")
    cp = int(input("Input car price: \n"))
    bp = int(input("Input bus price: \n"))
    tp = int(input("Input truck price: \n"))

    main(place,cp,bp,tp)

    continues = input("Are there anymore gates?[y/n]\n")
    if continues.lower() == "n":
        moregates = False
        
    





         
   
