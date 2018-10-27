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

def P( *sentences ):
	sentence = random.choice(sentences)
	global para
	global params
	para.append( sentence.format(**params) )

def PushParagraph():
	global para
	para.append("\n")

#Story format:
# I went on a bit of a journey. Why?
# Start with home village, give a reason for just changing course.
P(
	"To be honest, I didn't know where I was going when I first set off, I just knew I had to leave.",
	"I don't recollect truly my reasons for starting this journey, but I know I had this great urge to do so.",
	"There was no good reason to begin it. I don't even think it did begin, it was just going to be a stroll.",
	"I was on my way to the shops, and they were closed, and I had my stuff, so I thought, I'll just go to the next town; make an adventure out of it, and it turned into this.",
	"I'd planned it for a while. Unsure what was really going to happen, but it was a planned thing.",
	"I'd been putting it off my whole life really. Never one for walking very far. But now seemed to be the right time.",
	"After they left, I felt like I had to leave as some point myself. And this was it.",
	)

# EX: when I left "name" - i "traveled" along the "road|track|path" I came across a "gap|field|meadow|lake"
P(
	"I left {ht} behind, travelling down hill, following the flow of the {hr}."
	)

# go via some lake or forest and remember looking after or being looked after by OTHER in such a place.
params["firstLoc"] = places.WoodsNameGen()
other = people.personGen()
other.populateParams(params,"o")

P(
	"It was nice out, and the going was easy. I should have realised that I would end up at {firstLoc}, but it came up on me by surprise. It jogged my memory of {oFN}. {oHe} loved climbing trees as a kid."
)
P(
	"{oHe} got stuck up a tree at one point, and I had to help {ohim} out. {oHe} was alright, but I think that was when {ohe} started really treating me like a big brother.",
	"{oHe} was stuck up a tree while I was nearby, and I tried to help {ohim} out. {oHe} landed on me and it was hilarious. Not at the time, but that's when {ohe} started really treating me like a big brother."
)
P(
	"{oFN} spent quite a bit of time in and around {firstLoc} when {ohe} was younger; there are still some carvings to prove it too."
)

PushParagraph()

# continue journey
P(
	"I made my way around the outskirts of {firstLoc} and found myself within sight of {v[0]}.",
	"When I found the other side of {firstLoc} I realised I would be soon coming across {v[0]}.",
	)

# find the first village, just in time, and meet someone.
P(
	"I'd been to {v[0]} before a while back, but couldn't remember much about it, so I was pleasantly surprised that as I approached, I was able to remember enough to find a place to get a bit to eat. I had remembered that the {pub[0]} was a nice place, so headed there.",
	"After that short trek, I needed some refreshment, so went in search of it. I stumbled across {pub[0]}, which was just the right kind of place.",
	)
people.personGen().populateParams(params,"p1")
P(
	"While waiting to be served, I met a nice {p1Pg} by the name of {p1FN}. {p1He} was just setting down to have some lunch {p1him}self.",
	"In there, I met a nice {p1Pg} who called {p1him}self {p1FN} {p1SN}.",
	"As I was sorting through my bits, a nice {p1Pg} introduced {p1him}self as {p1FN} and we started talking about {v[0]}.",
	)

# Met up with someone at the first village (PLACE1), and decided not to turn back.
P(
	"We chatted for a while, and I learned that {p1he} worked at {church[0]}, which was the local church for most of the people from {v[0]}. {p1He} mentioned that some of the congregation were originally from {ht}, and offered to take me home.",
	"It was nice to pass a little time. I learned that {p1he} regularly attended {church[0]} and how {p1he} had been roped into helping drive some of the congregation to {ht} on shopping trips. {p1He} then offered to take me back home.",
	)
P(
	"It was at precisely this point that I realised that I wasn't going back",
	"It took this offer to bring about the realisation that I was not going to return.",
	)
PushParagraph()

# Reminice about progressing once you have started.
P(
	"I finished up, said goodbye to {p1FN}, then left {pub[0]}. I walked through the village for a bit while my mind wandered.",
	)
P(
	"{oFN} was always doing this. {oHe} was always starting something, and just when you thought {ohe} would give up, {ohe} would change tactics, or redouble {ohis} efforts, and forge on.",
	)
P(
	"{oHe} always had a goal. A distant horizon to aim at. That was the main difference between us, I always thought. There {ohe} was, always taking steps towards a goal, and there was I, taking steps.",
	)
P(
	"Now, it's I taking the steps towards a goal. What that goal is, I wasn't sure at the time, but I knew it was away from {ht}, so I started by doing precisely that. Leaving by the opposite road out of the village of {v[0]}.",
	)
PushParagraph()

# Follow a natural formation, and meet another that leads to talking about OTHER
places.Landmark().populateParams(params,"nf");
P(
	"As you leave {v[0]}, you always have to travel the road that leads alongside {nfArticleName}. It's a pleasant {nfType}, but it's probably the reason why the village hasn't grown as much as it could.",
	"As I suspected, I quickly ran into a {nfType} locally known as {nfArticleName}, and had to retrace my steps a little. I found a {nfAvoid} and made progress.",
	"When you head this way from {v[0]}, you have to travel along {nfArticleName} road. It's a pleasant {nfType}, but many would need to use the {nfAvoid} if they wished to grow the village.",
	)
P(
	"I wasn't carrying much, so the going was easy. I traveled for what must have been over a mile without meeting a single solitary soul.",
	"The walk was good and the going was easy as I was barely carrying anything. I must have been walking for nearly twenty minutes with nothing but the birds and crickets to keep me company.",
	)
people.personGen().populateParams(params,"p2")
P(
	"At some point, I saw a car coming the other way, and they stopped to see if I was alright. The {p2Pg} driving seemed to think I was lost. I assured {p2him} that I was fine, and they drove off.",
	"I walked past a little road side cafe at some point. The {p2Pg} at the counter asked if I was lost, but I assured them I was just taking a walk. {p2He} wished me well, and I continued on my way.",
	)
P(
	"I realised that {oFN} had asked me the same thing a number of times. Was I lost. Though {ohe} had asked it in a more philosphical way.",
	"As I continued I mulled over the words. Lost. I had been asked if I was lost by {oFN} a number of times. {oHe} had asked me if I felt that maybe I had lost my way in life.",
	)
PushParagraph()

# note the time and head to next village.
P(
	"The scenery was lovely, but the day was wearing on. I had enjoyed the walk, but I needed to find somewhere to stay for the night.",
	)
P(
	"When I got to the junction, I decided to make my way to {v[1]} as it wasn't too far and was still heading away from {ht}.",
	)
P(
	"It had been a long time since I had completed a trek as long as the one I was planning, so I was pleased to see that the village was furnished with a market street, which I would utilise in the morning in preparation for the rest of my trip.",
	"On approaching the village, I spotted a bunch of shops that would do the job of kitting me out for the rest of my adventure. I was please about this as I realised that it had been quite some time since I had attempted such a thing.",
	)

# Have a quick snack and talk with STAFF about staying in one place.
people.personGen().populateParams(params,"s1")
P(
	"I stopped at the {pub[1]}, as it seemed to be accommodating, and indeed it was, they had a room upstairs I could use that night.",
	"There weren't any obvious hotels, but when I asked at the {pub[1]}, they were surprised I didn't know they provided overnight stays. I wasn't sure, but took a room nonetheless.",
	)
P(
	"As it turns out, the {s1Pg} behind the bar was related to the {p2Pg} I met on the road. They had lived around this way for all their lives. Much like {oFN} and I, but they had never left {v[1]}."
	)
P(
	"{oFN} had been all over the world.",
	"{oFN} wasn't one for staying in one place very long.",
	"Sticking in one place never seemed likely for {oFN}",
	)
P(
	"{oHe} wasn't running away from anything though. That much was clear.",
	"It wasn't a fault though, it was a sense of adventure that drove {ohim}.",
	"Movement was a virtue to {ohim}, and staying in one place was always seen as a missed opportunity.",
	)
P(
	"I wasn't such a grand adventurer, but at least I had taken vacations abroad, and seen some of the different cultures.",
	"Though I was not such a wide and varied explorer, I had at least left home on holiday, or on business.",
	)

PushParagraph()
P(
	"The idea of staying in one place, forever, just felt like a waste of a life.",
	"One location, for all your days. That idea seemed as foreign to me as the great journey {ohe} had taken.",
	)
P(
	"I asked {s1FN}, the {s1Pg} behind the bar, why it was they never left.",
	"Curious to understand, I ventured the question of why to {s1FN}, the {s1Pg} behind the bar.",
	"{s1FN}, the {s1Pg} behind the bar, told me that people have asked why they never left {v[1]}.",
	)
P(
	"{s1He} said that there was always so much to do here, and not enough time to do it all, what was the point in going anywhere else?",
	"It wasn't that they wanted to stay, {s1he} said, but more that they didn't see a reason to go anywhere else.",
	)
P(
	"I wondered to myself if that's how {oFN} thought about me. Was that why {ohe} asked if I was lost? If you're lost, you don't know how to go anywhere.",
	"I thought about how this made me feel. I thought, maybe they didn't feel safe to travel, in case they couldn't find their way back. Maybe that's why {oFN} asked me if I was lost too.",
	)
P(
	"I continued to think about this, maybe a little too long, then made my way to my bed for the night.",
	)
PushParagraph()

# Wake ready, but aching, old bones.
P(
	"By morning, I was paying for the activities of the previous day. I knew that I had to pace myself.",
	"I wasn't early to rise. In fact, rising itself was a little painful after the exercise.",
	"My bones complained when the morning came. I tended to the act of getting up with some care.",
	)
P(
	"I had to go shopping, so I made my way down. There wasn't any breakfast put on in this place, so I found somewhere to eat before preparing for the day ahead with a little retail therapy.",
	"I knew I had to prepare for the day, so I made my way downstairs. They had put on a cereal breakfast, which was fair, so I ate, settled up, then went on my shopping trip.",
	"In spite of this, the smell of cooked breakfast was wafting into my room, and it was a good start to the day after all. With a full belly I ventured out and onto my first stop at the stores in order to make myself ready.",
	)
P(
	"I got myself a rucksack, nothing too large, I didn't want to overburden myself.",
	"I saw a few different bags, sacks, and other carriers, but given my plans, a simple backpack sufficed.",
	"I grabbed myself a simple backpack. Nothing too large, as I didn't want to carry too much."
	)

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


