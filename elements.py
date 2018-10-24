import random

import places


#named after events "millers crossing"
#churches names "St Whatevers"
#woods, and wood names "Barrow Woods" "Witches Woods" "Green Forest" -> "Witchesgate" "Woodside"
#lakes and pond names "Lake Henry" "Heron's lake" "Leg of mutton pond" "Fishing pond" "Mill pond" "Long pond" "Shining lake" "Bright lake" "High lake."
#formatting with order / keyword lookup formatting
#formatting post hoc, replace lookups after generating structure
#"At the pub, met this fellow, a bricklayer I believe, think his name was Tom" vs "At the pub, I met this fellow named Tom, said he was a bricklayer." "Met an <age> looking chap called <CH3> who said he worked as a <CH3.job>."
#reminice layer
#framing to make it more believable

if __name__=="__main__":
	print "Module demo:"
	for x in range(20):
		print "PUB> " + places.PubNameGen()
	for x in range(20):
		print "WOO> " + places.WoodsNameGen()
	for x in range(20):
		print "LAK> " + places.LakeNameGen()


