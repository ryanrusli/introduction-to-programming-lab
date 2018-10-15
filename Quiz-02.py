#Ryan Rusli - 2201832446
#Quiz 02 - Hotel System
#------------------------

import random
import sys

class Hotel:					#class for the hotel
	def __init__(self,name):	
		self.name = name
		self.doublerooms = []	#list for all the double rooms
		self.singlerooms = []	#list for all the single rooms

	def singles(self):			#function to add all the room numbers to single room list
		for i in range(1,21):
			i =  str(i)
			self.singlerooms.append(i)
		return self.singlerooms

	def doubles(self):			#function to add all the room numbers to double room list
		for i in range(21,41):
			i =  str(i)
			self.doublerooms.append(i)
		return self.doublerooms

	def getname(self):			#returns the name of the hote;
		return self.name




class Single:				#class for single bedrooms
	def __init__(self,nights):
		self.price = 50		#price for single room
		self.nights = nights

	def cost(self,extrab):	#total cost for all the nights, extrab is additional cost for extra bed, only used in double rooms
		if extrab == True:
			amount = (self.price + 25) * self.nights
		else:
			amount = self.price * self.nights
		print("Your cost of stay is $",amount)
		return amount

	def checkedin(self,listt,roomNo):			#adjusts the list for the room
		listt.remove(roomNo)
		print("Thank you for staying with us, your room number is",roomNo)
		return roomNo

	def random(self,singles,nights):		#randomly sets an unused room to the user, ends the code if all rooms taken
		global takenSingles
		found = False
		for i in singles:
			roomNo = random.choice(singles)
			print(roomNo)
			if str(roomNo) not in takenSingles:
				takenSingles.append(roomNo)		#adds the room number and nights stayed to a list declared below
				takenSingles.append(nights)
				found = True
				return roomNo
				break
		if found == False:
			print("We ran out of single rooms.")
			sys.exit()
	
	def checkedout(self,singles,roomNo):	#adjusts the room list for checkout
		singles.append(roomNo)
		print("Thank you for your visit, we hope to see you again!")





class Double(Single):		#inherited class for double rooms
	def __init__(self,nights):
		Single.__init__(self,nights)
		self.price = 85		#increased the price for double room

	def extrabed(self,takenDoubles):					#adds the to be declared taken doubles list, a boolean value for extra bed
		print("All right, the extra bed will be added.")# in the takendoubles list beside the room number and nights stayed
		takenDoubles.append(True)
		return self.price


	def drandom(self,doubles,nights):				#assigns a random room number for the double rooms, and adjussts the list
		global takenDoubles
		found = False
		for i in doubles:
			roomNo = random.choice(doubles)
			if str(roomNo) not in takenDoubles:
				takenDoubles.append(str(roomNo))
				takenDoubles.append(nights)
				found = True
				return roomNo
				break
		if found == False: 
			print("Ran out of rooms.")
			sys.exit()


# main function

hotel = Hotel('Marina Bay')		#initialises hotel name

singles = hotel.singles()		#creates the list for single rooms
doubles = hotel.doubles()		#creates the list for double rooms

takenSingles = []				#list to store all taken single rooms
takenDoubles = []				#list to store all taken double rooms
print("Welcome to Hotel",hotel.getname())

run = True 					#boolean value to continue loop
while run:


	print("What would you like to do?")		
	print("1.Check In\n"
		  "2.Check Out\n"
		  "3.Check Room\n")

	option = int(input(""))		# input for selecting an option



	if option == 1:
		print("Which room category would you like?\n"
			  "1.Singles\n2.Doubles\n")

		roomcat = int(input(""))		#requests input for room category

		print("How many nights are you staying?\n")
		nights = int(input(""))			#input for length of stay in nights
		if roomcat == 1:
			room = Single(nights)
			roomNo = room.random(singles,nights)
			roomNo = str(roomNo)
			room.checkedin(singles,roomNo)		



		elif roomcat == 2:			
			droom = Double(nights)
			roomNo = droom.drandom(doubles,nights)
			roomNo = str(roomNo)
			droom.checkedin(doubles,roomNo)
			print("Would you like an extra bed for that double room for an extra $ 25 per night? [y/n]\n")
			xtra = input("")		#input to ask if user wants an extra bed

			if xtra.lower() == "y":		
				droom.extrabed(takenDoubles)
			else:
				takenDoubles.append(False)

	elif option == 2:
		roomNo = input("What was your room number?\n")
		if int(roomNo) <= 20:
			for i in range(len(takenSingles)):	#checks the entire taken list for the room number
				if takenSingles[i] == roomNo:
					nightsStayed = takenSingles[i+1]	#collects the amount of nights stayed for the room
					room =  Single(nightsStayed)	
					room.checkedout(singles,roomNo)		
					room.cost(False)		#False is for no extra bed

		elif int(roomNo) <= 40:
			for i in range(len(takenDoubles)):
				if takenDoubles[i] == roomNo:
					nightsStayed = takenDoubles[i+1]	#collects nights stayed
					extrab = takenDoubles[i+2]			#collects if user has an extra bed in the room
					droom = Double(nightsStayed)
					droom.checkedout(doubles,roomNo)
					droom.cost(extrab)		

	elif option == 3:
		roomNo = input("What room number would you like to see if it's available?\n")
		foundd = False
		for i in (singles + doubles):		#loops through both and singles and doubles list
			if roomNo == str(i):			
				print("Room is available.")
				foundd = True 				#ends the loop if the room is found in the combined list
				break
		if foundd == False:
			print("Room is unavailable.")

	x = input("Would you like to continue using this system? [y/n]\n")	#input to continue looping or to end
	if x.lower() == "n":
		run = False









		








