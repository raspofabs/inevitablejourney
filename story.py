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
hr = places.RiverNameGen() # home river
ht = places.VillageNameGen(hr) # home town
params = {
	"ht":ht,
	"hr":hr,
	"v":villages,
	"r":rivers,
	"pub":pubs,
	"church":churches,
	"lake":lakes,
	"wood":woods
	}
para = []

def Push( sentence ):
	global para
	global params
	para.append( sentence.format(**params) )

def PushParagraph():
	global para
	para.append("\n")

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
Push(random.choice(leaveReasons))

# EX: when I left "name" - i "traveled" along the "road|track|path" I came across a "gap|field|meadow|lake"
course = [
	"I left {ht} behind, travelling down hill, following the flow of the {hr}."
	]
Push( random.choice(course) )

# go via some lake or forest and remember looking after or being looked after by OTHER in such a place.
params["firstLoc"] = places.WoodsNameGen()
other = people.personGen()
other.populateParams(params,"o")

Push( random.choice([
	"It was nice out, and the going was easy. I should have realised that I would end up at {firstLoc}, but it came up on me by surprise. It jogged my memory of {oFN}. {oHe} loved climbing trees as a kid."
]))
Push( random.choice([
	"{oHe} got stuck up a tree at one point, and I had to help {ohim} out. {oHe} was alright, but I think that was when {ohe} started really treating me like a big brother.",
	"{oHe} was stuck up a tree while I was nearby, and I tried to help {ohim} out. {oHe} landed on me and it was hilarious. Not at the time, but that's when {ohe} started really treating me like a big brother."
]))
Push( random.choice([
	"{oFN} spent quite a bit of time in and around {firstLoc} when {ohe} was younger; there are still some carvings to prove it too."
]))

PushParagraph()

# continue journey
Push( random.choice([
	"I made my way around the outskirts of {firstLoc} and found myself within sight of {v[0]}.",
	"When I found the other side of {firstLoc} I realised I would be soon coming across {v[0]}.",
	]))

# find the first village, just in time, and meet someone.
Push( random.choice([
	"I'd been to {v[0]} before a while back, but couldn't remember much about it, so I was pleasantly surprised that as I approached, I was able to remember enough to find a place to get a bit to eat. I had remembered that the {pub[0]} was a nice place, so headed there.",
	"After that short trek, I needed some refreshment, so went in search of it. I stumbled across {pub[0]}, which was just the right kind of place.",
	]))
people.personGen().populateParams(params,"p1")
Push( random.choice([
	"While waiting to be served, I met a nice {p1Pg} by the name of {p1FN}. {p1He} was just setting down to have some lunch {p1him}self.",
	"In there, I met a nice {p1Pg} who called {p1him}self {p1FN} {p1SN}.",
	"As I was sorting through my bits, a nice {p1Pg} introduced {p1him}self as {p1FN} and we started talking about {v[0]}.",
	]))

# Met up with someone at the first village (PLACE1), and decided not to turn back.
Push( random.choice([
	"We chatted for a while, and I learned that {p1he} worked at {church[0]}, which was the local church for most of the people from {v[0]}. {p1He} mentioned that some of the congregation were originally from {ht}, and offered to take me home.",
	"It was nice to pass a little time. I learned that {p1he} regularly attended {church[0]} and how {p1he} had been roped into helping drive some of the congregation to {ht} on shopping trips. {p1He} then offered to take me back home.",
	]))
Push( random.choice([
	"It was at precisely this point that I realised that I wasn't going back",
	"It took this offer to bring about the realisation that I was not going to return.",
	]))
PushParagraph()

# Reminice about progressing once you have started.
Push( random.choice([
	"I finished up, said goodbye to {p1FN}, then left {pub[0]}. I walked through the village for a bit while my mind wandered.",
	]))
Push( random.choice([
	"{oFN} was always doing this. {oHe} was always starting something, and just when you thought {ohe} would give up, {ohe} would change tactics, or redouble {ohis} efforts, and forge on.",
	]))
Push( random.choice([
	"{oHe} always had a goal. A distant horizon to aim at. That was the main difference between us, I always thought. There {ohe} was, always taking steps towards a goal, and there was I, taking steps.",
	]))
Push( random.choice([
	"Now, it's I taking the steps towards a goal. What that goal is, I wasn't sure at the time, but I knew it was away from {ht}, so I started by doing precisely that. Leaving by the opposite road out of the village of {v[0]}.",
	]))
PushParagraph()

# Follow a natural formation, and meet another that leads to talking about OTHER
places.Landmark().populateParams(params,"nf");
Push( random.choice([
	"As you leave {v[0]}, you always have to travel the road that leads alongside {nfArticleName}. It's a pleasant {nfType}, but it's probably the reason why the village hasn't grown as much as it could.",
	"As I suspected, I quickly ran into a {nfType} locally known as {nfArticleName}, and had to retrace my steps a little. I found a {nfAvoid} and made progress.",
	]))
Push( random.choice([
	"I wasn't carrying much, so the going was easy. I traveled for what must have been over a mile without meeting a single solitary soul.",
	"The walk was good and the going was easy as I was barely carrying anything. I must have been walking for nearly twenty minutes with nothing but the birds and crickets to keep me company.",
	]))
people.personGen().populateParams(params,"p2")
Push( random.choice([
	"At some point, I saw a car coming the other way, and they stopped to see if I was alright. The {p2Pg} driving seemed to think I was lost. I assured {p2him} that I was fine, and they drove off.",
	"I walked past a little road side cafe at some point. The {p2Pg} at the counter asked if I was lost, but I assured them I was just taking a walk. {p2He} wished me well, and I continued on my way.",
	]))
Push( random.choice([
	"I realised that {oFN} had asked me the same thing a number of times. Was I lost. Though {ohe} had asked it in a more philosphical way.",
	"As I continued I mulled over the words. Lost. I had been asked if I was lost by {oFN} a number of times. {oHe} had asked me if I felt that maybe I had lost my way in life.",
	]))

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

if __name__=="__main__":

	para = " ".join( para )
	para = para.split("\n")
	para = [textwrap.fill(textwrap.dedent(x)) for x in para]
	para = "\n\n".join( para )
	print( para )


