import random
import generator
from generator import GetNonRecentFromListGenerator as Gen

# for simplicity sake, I'm sticking with two genders
# people have a gender, a first name, a second name
# beyond that, they have a job, a hobby, an age, a disposition etc.

vehicleType = ["car","car","car","van","van","truck","pickup","hatchback"]
trafficType = ["car","van","truck"]
vehicleColour = ["white","white","red","red","black","blue","silver","dirty brown","pale green","pale yellow","grey"]
femaleGender = ["woman","girl","lady","lass"]
surnameGen = generator.GenerateFromFile( "lastnames.txt" )
maleNameGen = generator.GenerateFromFile( "firstnames_male.txt" )
femaleNameGen = generator.GenerateFromFile( "firstnames_female.txt" )
class Vehicle:
	def __init__(self,typelist):
		self.name = random.choice(typelist)
		self.colour = random.choice(vehicleColour)
	def populateParams(self, params, prefix):
		params[prefix+"Type"]=self.name
		params[prefix+"Col"]=self.colour
	def __repr__(self):
		return "Vehicle({} {})".format( self.colour, self.name )

def vehicleGen():
	return Vehicle(vehicleType)
def trafficGen():
	return Vehicle(trafficType)

if __name__=="__main__":
	print( "Vehicle module demo:")
	for x in range(8):
		print( "VEH> {}".format( repr(vehicleGen()) ) )

