import random
import places
import textwrap
import people

villages = [places.VillageNameGen() for x in range(3)]
rivers = [places.RiverNameGen() for x in range(3)]
pubs = [places.PubNameGen() for x in range(3)]
churches = [places.ChurchNameGen() for x in range(3)]
lakes = [places.LakeNameGen() for x in range(3)]
woods = [places.WoodsNameGen() for x in range(3)]
params = {
	"v":villages,
	"r":rivers,
	"pub":pubs,
	"church":churches,
	"lake":lakes,
	"wood":woods
	}

#Story format:
# I went on a bit of a journey. Why?
leaveReasons = [
	"To be honest, I didn't know where I was going when I first set off, I just knew I had to leave.",
	"I don't recollect truly my reasons for starting this journey, but I know I had this great urge to do so.",
	"There was no good reason to begin it. I don't even think it did begin, it was just going to be a stroll.",
	"I was on my way to the shops, and they were closed, and I had my stuff, so I thought, I'll just go to the next town; make an adventure out of it, and it turned into this.",
	"I'd planned it for a while. Unsure what was really going to happen, but it was a planned thing.",
	"I'd been putting it off my whole life really. Never one for walking very far. But now seemed to be the right time.",
	"After they left, I felt like I had to leave as some point myself. And this was it.",
	]

# Start with home village, give a reason for just changing course.
hr = places.RiverNameGen() # home river
ht = places.VillageNameGen(hr) # home town
params["ht"]=ht
params["hr"]=hr
para = [random.choice(leaveReasons).format(**params)]


course = [
	"I left {ht} behind, travelling down hill, following the flow of the {hr}."
	]
para.append( random.choice(course).format(**params))

# go via some lake or forest and remember looking after or being looked after by OTHER in such a place.
params["firstLoc"] = places.WoodsNameGen()
params["oFN"]=people.maleNameGen();
params["oSN"]=people.surnameGen();

reminisce1 = [
	"It was nice out, and the going was easy. I should have realised that I would end up at {firstLoc}, but it came up on me by surprise. It jogged my memory of {oFN}. He loved climbing trees as a kid."
]
reminisce2 = [
	"He got stuck up a tree at one point, and I had to help him out. He was alright, but I think that was when he started really treating me like a big brother.",
	"He was stuck up a tree while I was nearby, and I tried to help him out. He landed on me and it was hilarious. Not at the time, but that's when he started really treating me like a big brother."
]
reminisce3 = [
	"{oFN} spent quite a bit of time in and around {firstLoc} when he was younger; there are still some carvings to prove it too."
]

para.append( random.choice(reminisce1).format(**params))
para.append( random.choice(reminisce2).format(**params))
para.append( random.choice(reminisce3).format(**params))

para.append("\n")

# continue journey
continue1 = [
	"I made my way around the outskirts of {firstLoc} and found myself within sight of {v[0]}.",
]
para.append( random.choice(continue1).format(**params))

# Met up with someone at the first village (PLACE1), and decided not to turn back.
# Reminice about progressing once you have started.
# Follow a natural formation, and meet another that leads to talking about OTHER
# note the time and head to next village.
# Have a quick snack and talk with STAFF about staying in one place.
# Wake ready, but aching, old bones.
# Decide to head to DEST, and need to travel by the old VIA
# pack a few THINGS, and set off.
# on way, meet someone
# make progress and come across PLACE2 never seen before.
# stop for refreshments and strike up with PERSON about the history of PLACE2.
# Reminice about history of OTHER, and how they got on with their life.
# Look about the village, take a little time, but move on.
# Make progress and end up in PLACE3 just as the light is making the place look cosy / idylic.
# Stay at the restaurant hotel
# Have a meal and meet a couple, and remember OTHER's first meeting with their love.
# 
# "OTHER would have liked this place. The view out to sea is refreshing."
# My journey was not done. I had more steps to take. I said goodbye to OTHER that day.

# OTHER's first job.
# OTHER's marriage
# OTHER's child
# OTHER's death

#formatting with order / keyword lookup formatting
#formatting post hoc, replace lookups after generating structure
#"At the pub, met this fellow, a bricklayer I believe, think his name was Tom" vs "At the pub, I met this fellow named Tom, said he was a bricklayer." "Met an <age> looking chap called <CH3> who said he worked as a <CH3.job>."
#reminice layer
#framing to make it more believable

leaveReason = random.choice(leaveReasons)

if __name__=="__main__":

	para.append( "After a short trek, I needed some refreshment, and found it at {pub[0]} where I met a nice fellow.".format(**params) )
	para.append( "We chatted for a while, and I learned that they worked at {church[0]}, the local church for {v[0]}.".format(**params) )
	para.append( "He mentioned that some of the congregation were originally from {ht}, and offered to take me home.".format(**params) )
	para = " ".join( para )
	para = para.split("\n")
	para = [textwrap.fill(textwrap.dedent(x)) for x in para]
	para = "\n\n".join( para )
	print( para )


