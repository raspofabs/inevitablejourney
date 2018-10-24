import random
import generator
from generator import GetNonRecentFromListGenerator as Gen

# for simplicity sake, I'm sticking with two genders
# people have a gender, a first name, a second name
# beyond that, they have a job, a hobby, an age, a disposition etc.

maleGender = ["man","boy","lad","gent"]
femaleGender = ["woman","girl","lady","lass"]
surnameGen = generator.GenerateFromFile( "lastnames.txt" )
maleNameGen = generator.GenerateFromFile( "firstnames_male.txt" )
femaleNameGen = generator.GenerateFromFile( "firstnames_female.txt" )

if __name__=="__main__":
	print( "Place module demo:")
	print( " Villages:")
	for x in range(10):
		print( "VIL> " + VillageNameGen())
	for x in range(10):
		print( "RIV> " + VillageNameGen( "Thames" ))
	print( " Churches:")
	for x in range(10):
		print( "CHU> " + ChurchNameGen())


