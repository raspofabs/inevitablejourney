import random

def GetNonRecentFromListGenerator( theList ):
	localList = theList[:]
	random.shuffle( localList )
	maxItem = int(len(localList) * 0.666)
	def generateOne():
		selected = random.randint(0,maxItem)
		value = localList.pop( selected )
		localList.append(value)
		return value
	return generateOne

def GenerateConstant( value ):
	def generateOne():
		return value
	return generateOne

def GenerateFromFile( filename ):
	f = open( filename, "rt" )
	if f:
		lines = f.read().split("\n")
		names = []
		for line in lines:
			if len(line) > 0:
				names.append(line)
		g = GetNonRecentFromListGenerator(names)
		f.close()
		return g
	return GenerateConstant( "F:"+filename+" Failed to load" )

if __name__=="__main__":
	print( "Generator module demo:")
	a = range(1,6)
	print(a)
	g = GetNonRecentFromListGenerator( a )
	b = [g() for x in range(10)]
	print(b)
