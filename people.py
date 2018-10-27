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
class Person:
	def __init__(self, gender = None):
		if gender == None:
			gender = random.randint(0,5) > 2
		if gender:
			self.fname = maleNameGen()
			self.pronouns = ("he","him","his")
			self.gender = random.choice(maleGender)
		else:
			self.fname = femaleNameGen()
			self.pronouns = ("she","her","her")
			self.gender = random.choice(femaleGender)
			if random.randint(0,8) > 6:
				self.nee = surnameGen()
		self.sname = surnameGen()
	def populateParams(self, params, prefix):
		params[prefix+"FN"]=self.fname
		params[prefix+"SN"]=self.sname
		params[prefix+"Pp"]=self.pronouns[0]
		params[prefix+"Pt"]=self.pronouns[1]
		params[prefix+"Po"]=self.pronouns[2]
		params[prefix+"PP"]=self.pronouns[0].capitalize()
		params[prefix+"PT"]=self.pronouns[1].capitalize()
		params[prefix+"PO"]=self.pronouns[2].capitalize()
		params[prefix+"Pg"]=self.gender
	def __repr__(self):
		if hasattr(self,"nee"):
			return "Person({} {} (nee {}), {} is a {})".format( self.fname, self.sname, self.nee, self.pronouns[0], self.gender )
		else:
			return "Person({} {}, {} is a {})".format( self.fname, self.sname, self.pronouns[0], self.gender )

class Couple:
	def __init__(self):
		self.m = Person(True)
		self.f = Person(False)
		self.f.nee = self.f.sname
		self.f.sname = self.m.sname
	def __repr__(self):
		return "{} and {} {}".format( self.m.fname, self.f.fname, self.m.sname )

def personGen():
	return Person()
def coupleGen():
	return Couple()

if __name__=="__main__":
	print( "People module demo:")
	for x in range(4):
		print( "MALE> {} {}".format( maleNameGen(), surnameGen() ) )
		print( "FEMA> {} {}".format( femaleNameGen(), surnameGen() ) )
	for x in range(8):
		print( "Person> " + repr( personGen() ) )
	for x in range(3):
		print( "Couple> " + repr( coupleGen() ) )


