#Ryan Rusli - 2201832446
#Assignment 4 - TOLL

#VERSION 1
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
              "================================================================================\n")
        
    

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


cp = 6000
bp = 8000
tp = 12000
print("\n")
gate = TollGate(cp,bp,tp)
gate.header()
run = True

while run:      #loop to repeat input of vehicles
    print("Select your vehicle category.\n")
    print("     1.Car  ( RP",gate.getcp(),")\n",
          "    2.Bus  ( RP",gate.getbp(),")\n",
          "    3.Truck( RP",gate.gettp(),")\n")
    
    x = int(input(""))
    vehicle = Vehicles(cp,bp,tp,x)
    vehicle.identify()
    continues = input("Continue? [y/n]\n")
    if continues.lower() == "n":
        run = False
