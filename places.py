import random
import generator
from generator import GetNonRecentFromListGenerator as Gen

prefixList = ['D','Dr','W','B','H','L','M','N','P','R','St','T','C','Cr']
midfixList = ['aun','ow','ud','id','od']
suffixList = [
	'indle','undle','oddle','intle','obble','en','ound','ow','old',
	'iddle','amble',
	'ang','ee','eedle','endle','aggle','ump']
shortSuffixList = [
	'en','ound','ow','old','amble','ang','ee','endle','ump','ant']
lateSuffixList = [ 'ing','ham' ]
finalSuffixList = [ 'ton','ing','ham','den','ingham','church','stead','stanton','wood','wich','well','by','ley','bury','worth','moore','cross' ]
finalSuffixList = [ 'port','mouth','end','landing' ]
riverVillageSuffixList = [ 'ford','bridge','side','brook', 'pool' ]
overallPrefixList = [ 'Little','Greater','Upper','Lower','Lesser']

prefixGen = Gen( prefixList )
midfixGen = Gen( midfixList )
suffixGen = Gen( suffixList )
shortSuffixGen = Gen( shortSuffixList )
lateGen = Gen( lateSuffixList )
finalGen = Gen( finalSuffixList )
overallPrefixGen = Gen( overallPrefixList )
riverVillageSuffixGen = Gen( riverVillageSuffixList )

def RiverNameGen():
	return prefixGen() + suffixGen()
def HillNameGen():
	return prefixGen() + shortSuffixGen()

class CVillageNameGen:
	def VillageNameGen1(self):
		return prefixGen() + suffixGen() + finalGen()
	def VillageNameGen2(self):
		return prefixGen() + midfixGen() + lateGen()
	def VillageNameGen3(self):
		return self.RiverGen() + riverVillageSuffixGen()
	def VillageNameGen4(self):
		return prefixGen() + suffixGen() + " on the " + self.RiverGen()
	def __init__(self):
		self.villageNameGenGen = Gen([self.VillageNameGen1,self.VillageNameGen2,self.VillageNameGen3, self.VillageNameGen4])
		self.RiverGen = RiverNameGen
	def Gen(self):
		return self.villageNameGenGen()()

	
def VillageNameGen( riverHint = None ):
	vgen = CVillageNameGen()
	if riverHint != None:
		vgen.RiverGen = generator.GenerateConstant( riverHint )
	prename = ""
	if random.randint(0,5) > 3:
		prename = overallPrefixGen() + " "
	return prename + vgen.Gen()

saintNames = ['David','Matthew','Mark','Luke','John','Bartholemew','Stephen']
churchSuffix = ['Fellowship','Church','Community Church','Hall']
saintGen = Gen( saintNames )
churchSuffixGen = Gen( churchSuffix )
def ChurchNameGen():
	# St Whatevers
	name = "St " + saintGen() + "'s"
	# + Fellowship / Church / Community / Hall
	if random.randint(0,5) > 3:
		name = name + " " + churchSuffixGen()
	return name

animal = ['Lion','Goose','Dog','Duck','Rabbit','Hound','Swan','Hart','Hare','Cock','Bull']
animalGen = Gen( animal )
colour = ['Red','Blue','Yellow','Black','White','Royal']
colourGen = Gen( colour )
objects = ['Crown','Tree','Rock','House','Flag','Bell','Plough','Rose','Oak']
objectGen = Gen( objects )
regency = ['King','Queen','Prince']
regencyGen = Gen( regency )
bodypart = ['Head','Arms','']
regencyGen = Gen( regency )
def ColourAnimal():
	return colourGen() + " " + animalGen()
def ColourObject():
	return colourGen() + " " + animalGen()

pubnameGen = generator.GenerateFromFile( "pubnames.txt" )
def PubNameGen():
	name = "The "+pubnameGen()
	return name

woodsnameGen = generator.GenerateFromFile( "woodsnames.txt" )
def WoodsNameGen():
	return woodsnameGen()

lakesnamesGen = generator.GenerateFromFile( "lakesnames.txt" )
def LakeNameGen():
	return lakesnamesGen()

class Landmark:
	def __init__(self):
		self.nType = random.choice(["woods","lake","river","hill"])
		if self.nType == "woods":
			self.name = woodsnameGen()
			self.article = self.name
			self.avoid = "path through it"
		if self.nType == "lake":
			self.name = lakesnamesGen()
			self.article = self.name
			self.avoid = "path around it"
		if self.nType == "river":
			self.name = RiverNameGen()
			self.article = "the "+self.name
			self.avoid = "bridge over it"
		if self.nType == "hill":
			self.name = HillNameGen()
			self.article = self.name+" hill"
			self.avoid = "gentle path over it"
	def populateParams(self, params, prefix):
		params[prefix+"Type"]=self.nType
		params[prefix+"Name"]=self.name
		params[prefix+"ArticleName"]=self.article
		params[prefix+"Avoid"]=self.avoid
	def __repr__(self):
		return "Landmark({}:{})".format( self.nType, self.name )

#woods, and wood names "Barrow Woods" "Witches Woods" "Green Forest" -> "Witchesgate" "Woodside"
#lakes and pond names "Lake Henry" "Heron's lake" "Leg of mutton pond" "Fishing pond" "Mill pond" "Long pond" "Shining lake" "Bright lake" "High lake."

if __name__=="__main__":
	print( "Place module demo:")
	print( " Villages:")
	for x in range(5):
		print( "VIL> " + VillageNameGen())
	for x in range(5):
		print( "RIV> " + VillageNameGen( "Thames" ))
	print( " Churches:")
	for x in range(5):
		print( "CHU> " + ChurchNameGen())
	for x in range(5):
		print( "LMK> " + repr(Landmark()))


