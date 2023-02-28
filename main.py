import discord
import os
import json
import requests
import random
from keep_alive import keep_alive
from discord.ext import commands
from discord import Member
import asyncio
#from typing import Optional
import time

animalwords = [
  "carnivore", "fly", "reptile", "frog", "hive", "sheep", "burrow", "crab", "shell", "turtle", "scales", "fur", "eggs", "fish", "den", "aquatic", "hibernation", "camel", "bull", "horse", "tail", "giraffe", "rooster", "feathers", "wings", "bee", "penguin", "pig", "bird", "octopus", "insect", "butterfly", "chaemeleon", "chrysalis", "rodent", "rabbit", "mouse", "predator", "prey", "frog", "deer", "shark", "elephant", "nest", "tusk", "beak"]
plants = ["oak", "flower", "sunflower", "evergreen", "pine", "redwood", "sequoia", "tulip", "rose", "daisy", "lily", "grass", "tree", "jasmine"]
clothingitems = ["pants", "shirt", "hat", "scarf", "gloves", "skirt", "dress", "suit", "shoes", "boots", "overalls", "skort", "socks", "jacket", "mittens", "belt"]
listoptions = [animalwords, plants, clothingitems]
listlabels = ["Animal Words", "Plants", "Items of Clothing"]
riddles = {"What has to be broken before you can use it?": "egg", "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle", "What is full of holes but still holds water?": "sponge", "What is always in front of you but can’t be seen?": "future", "What can you break, even if you never pick it up or touch it?": "promise", "What goes up but never comes down?": "age", "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?": "bald", "What gets wet while drying?": "towel", "What can’t talk but will reply when spoken to?": "echo", "The more of this there is, the less you see. What is it?": "darkness", "David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?": "david", "I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?": "shadow", "What has many keys but can’t open a single lock?": "piano", "What is black when it’s clean and white when it’s dirty?": "chalkboard", "I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?": "breath", "What gets bigger when more is taken away?": "hole", "Where does today come before yesterday?": "dictionary", "What invention lets you look right through a wall?": "window", "If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I?": "secret", "What goes up and down but doesn’t move?": "staircase", "If you’re running in a race and you pass the person in second place, what place are you in?": "second", "What has one eye, but can’t see?": "needle", "What has a mouth, but can't speak?": "river", "What has hands, but can’t clap?": "clock", "What can you catch, but not throw?": "cold", "What has many teeth, but can’t bite?": "comb"}

allwords = [
    "grandiloquence", "obstreperous", "querulous", "pareidolia", "glib",
    "idyllic", "boondoggle", "elan", "dilettante", "malaise", "cloying",
    "galvanizing", "conflagration", "myrmecophilous", "panacea",
    "blandishment", "emollient", "vociferous", "zephyr", "winsome", "toady",
    "torpid", "spurious", "misanthrope", "verisimilitude", "tryst", "turbid",
    "cynosure", "convivial", "insouciance", "adumbrate", "elicit"
]

try:
  f = open("wordlist.txt", "r")
  thewordlist = json.loads(f.read())
  allwords = thewordlist
  f.close()
except:
  pass

newwords = [
    "abject", "aberration", "abjure", "abnegation", "abrogate", "abscond",
    "abstruse", "accede", "accost", "accretion", "acumen", "adamant",
    "admonish", "adumbrate", "adverse", "advocate", "affluent", "aggrandize",
    "alacrity", "alias", "ambivalent", "amenable", "amorphous",
    "anachronistic", "anathema", "annex", "antediluvian", "antiseptic",
    "apathetic", "antithesis", "apocryphal", "approbation", "arbitrary",
    "arboreal", "arcane", "archetypal", "arrogate", "ascetic", 
    "assiduous", "atrophy", "bane", "bashful", "beguile", "bereft", "bilk", "bombastic", "cajole", "callous", "calumny",
    "camaraderie", "candor", "capitulate", "carouse", "carp", "caucus",
    "cavort", "circumlocution", "circumscribe", "circumvent", "clamor",
    "cleave", "cobbler", "cogent", "cognizant", "commensurate", "complement",
    "compunction", "concomitant", "conduit", "congruity",
    "connive", "consign", "constituent", "construe", "contusion", "contrite",
    "contentious", "contravene", "convivial", "corpulence", "covet",
    "cupidity", "dearth", "debacle", "debauch", "debunk", "defunct",
    "demagogue", "denigrate", "derivative", "despot", "diaphanous", "didactic",
    "dirge", "disaffected", "discomfit", "disparate", "dispel", "disrepute",
    "divisive", "dogmatic", "dour", "duplicity", "duress", "eclectic", "edict", "egregious", "elegy", "embezzlement", "emend", 
    "empirical", "emulate", "enervate", "enfranchise", "engender", "ephemeral",
    "epistolary", "equanimity", "equivocal", "espouse", "evanescent", "evince",
    "exacerbate", "exhort", "execrable", "exigent", "expedient", "expiate",
    "expunge", "extraneous", "extol", "extant", "expurgate", "fallacious",
    "fatuous", "fetter", "flagrant", "foil", "forbearance", "fortuitous",
    "fractious", "garrulous", "gourmand", "grandiloquent", "gratuitous",
    "hapless", "hegemony", "heterogenous", "iconoclast", "idiosyncratic",
    "impecunious", "impetuous", "impinge", "impute", "inane", "inchoate",
    "incontrovertible", "incumbent", "inexorable", "inimical", "injunction",
    "inoculate", "insidious", "instigate", "insurgent", "interlocutor",
    "intimation", "inure", "invective", "intransigent", "inveterate",
    "irreverence", "knell", "laconic", "largesse", "legerdemain",
    "libertarian", "licentious", "linchpin", "litigant", "maelstrom",
    "maudlin", "maverick", "mawkish", "maxim", "mendacious", "modicum",
    "morass", "mores", "munificent", "multifarious", "nadir", "negligent",
    "neophyte", "noisome", "noxious", "obdurate", "obfuscate", "officious",
    "onerous", "ostensible", "ostracism", "palliate", "panacea", "paradigm",
    "pariah", "partisan", "paucity", "pejorative", "pellucid", "penchant",
    "penurious", "pert", "pernicious", "pertinacious", "phlegmatic",
    "philanthropic", "pithy", "platitude", "plaudit", "plenitude", "plethora",
    "portent", "potentate", "preclude", "predilection", "preponderance",
    "presage", "probity", "proclivity", "profligate", "promulgate",
    "proscribe", "protean", "prurient", "puerile", "pugnacious", "pulchritude",
    "punctilious", "quaint", "quixotic", "quandary", "recalcitrant",
    "redoubtable", "relegate", "remiss", "reprieve", "reprobate", "rescind",
    "requisition", "rife", "sanctimonious", "sanguine", "scurrilous",
    "semaphore", "serendipity", "sobriety", "solicitous", "solipsism",
    "spurious", "staid", "stolid", "subjugate", "surfeit", "surreptitious",
    "swarthy", "tangential", "tome", "travesty", "trenchant", "trite",
    "truculent", "turpitude", "ubiquitous", "umbrage", "upbraid",
    "utilitarian", "veracity", "vestige", "vicissitude", "vilify", "virtuoso",
    "vitriolic", "vituperate", "wanton", "winsome", "yoke", "wily"
]

try:
	f = open("newwordlist.txt", "r")
	newwordlist = json.loads(f.read())
	newwords = newwordlist
	f.close()
except:
	print("didn't work")
	pass

letters = ["a. ", "b. ", "c. ", "d. "]
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

listofpictures = [
  'https://art.pixilart.com/6685336733192ec.png','https://art.pixilart.com/2616c25e935f463.png', 'https://art.pixilart.com/b1f475d4e5c5c29.png','https://art.pixilart.com/0dff72fc49ae52d.png','https://art.pixilart.com/d6555ff39e34f5b.png','https://art.pixilart.com/df945390d3ed976.png','https://art.pixilart.com/4a83832ee9ee0c6.png']
dexc = "Try to guess the word!"

pointdict = {}
yesno = ['yes', 'y', 'no', 'n']

class Users:
  def __init__(self, name, points):
    self.name = name
    self.points = points


intents=discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=['w!', 'W!'], case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def define(ctx, arg):
	"defines a given word!"
	url = requests.get(
	    "https://dictionaryapi.com/api/v3/references/collegiate/json/" + arg +
	    "?key=REPLACE_WITH_YOUR_API_KEY")
	url_json = url.json()
	try:
		ourdef = url_json[0].get("shortdef")
		wholedef = "\n".join(ourdef)
		#joins whole definition separated by a) line
		await ctx.send(arg.lower())
		#sends the word
		await ctx.send(wholedef)
	except:
		await ctx.send("Cannot find definition for '" + arg.lower() + "'. Make sure the word is spelled correctly.")


@bot.command()
async def quiz(ctx):
	"quizzes users on word definitions!"
	randomword = allwords[random.randrange(0, len(allwords))]
	await ctx.send("Time for a quiz! What does '" + randomword + "' mean?")

	answerchoices = random.sample(allwords, 3)
	answerchoices.insert(random.randrange(0, 3), randomword)

	for g in range(len(answerchoices)):
		url = requests.get(
		    "https://dictionaryapi.com/api/v3/references/collegiate/json/" +
		    answerchoices[g] + "?key=REPLACE_WITH_YOUR_API_KEY")
		url_json = url.json()
		ourdef = url_json[0].get("shortdef")

		wholedef = "\n".join(ourdef)
		# for t in ourdef)
		# joins every item in ourdef, separated by a new line
		await ctx.send(">>> **" + letters[g].upper() + "**" + wholedef)
		#if it's the first line it will print the letter of the word we're on (g)

	def check(msg):
		return msg.content.lower().rstrip(".") + ". " in letters

	msg = await bot.wait_for("message", check=check)
	if answerchoices.index(randomword) == letters.index(
	    msg.content.lower().rstrip(".") + ". "):
		await ctx.send(ctx.author.mention + " Correct!")
	else:
		await ctx.send(ctx.author.mention + " Sorry, that's not right. The correct answer was **" + letters[answerchoices.index(randomword)].upper() + "**")


@bot.command()
async def wordlist(ctx):
	"sends wordlist!"
	f = open("wordlist.txt", "r")
	thewordlist = json.loads(f.read())
	await ctx.send(thewordlist)
	f.close()


@bot.command()
async def add(ctx, arg):
  "adds a word to the wordlist!"
  f = open("wordlist.txt", "w")
  allwords.append(arg.lower())
  f.write(json.dumps(allwords))
  f.close()
  await ctx.send("'" + arg.lower() + "' has been added.")
  print("added " + arg)


@bot.command()
async def remove(ctx, arg):
  "removes a word from the wordlist!"
  if arg not in allwords:
    await ctx.send("You must provide a word that is already in the wordlist.")
  f = open("wordlist.txt", "w")
  allwords.remove(arg.lower())
  f.write(json.dumps(allwords))
  f.close()
  print("removed " + arg)
  await ctx.send("'" + arg.lower() + "' has been removed.")


@bot.command()
async def giveword(ctx):
	"gives a new word of the day!"
	todaysword = newwords[random.randrange(0, len(newwords))]
	f = open("wordlist.txt", "w")
	allwords.append(todaysword)
	f.write(json.dumps(allwords))
	f.close()

	f = open("newwordlist.txt", "w")
	newwords.remove(todaysword)
	f.write(json.dumps(newwords))
	f.close()

	await ctx.send("Today's word of the day is: " + todaysword + "!")
	await ctx.invoke(bot.get_command('define'), arg=todaysword)


@bot.command()
async def hangman(ctx, pass_Context=True):
  "play a hangman game!"
  hangmanword = allwords[random.randrange(0, len(allwords))]
  lettersinword = []
  alldashes = []
  lettersused = []
  lettersguessed = 0
  bodyparts = 0
  for dashes in range(len(hangmanword)):
    alldashes.append("...")
		#adds every dash as ... to the list
    lettersinword.append(hangmanword[dashes])
		#adds every letter to lettersinword
  print(hangmanword)
  embed=discord.Embed(title="**Hangman**", description="Try to guess the word!", color=discord.Color.blue())
  embed.set_thumbnail(url=listofpictures[bodyparts])
  embed.add_field(name="Your Word", value="   ".join(alldashes), inline=False)
  embed.add_field(name="Letters Used", value="** **", inline=False)
  embed.set_footer(text="Please type in a letter.")
  await ctx.send(embed=embed)

  def checkletter(msg):
    return msg.content.lower() in alphabet

  while lettersguessed < len(lettersinword) and bodyparts < 6:
    msg = await bot.wait_for("message", check=checkletter)
    if msg.content.lower() in lettersused:
      await ctx.send("You have already guessed that letter.")
    else:
      if msg.content.lower() in lettersinword:
        indexes = []
        while msg.content.lower() in lettersinword:
          whichletter = lettersinword.index(msg.content.lower())
					#index of what they said in list lettersinword
					#this is the first time msg.content appears in letters inword
          lettersinword.pop(whichletter)
          lettersinword.insert(whichletter, "8")
					#inserts the number 8 in place of the letter that used to be there
          indexes.append(whichletter)
        for n in range(len(indexes)):
					#n is the index of indexes, indexes[n] is the number we are popping and inserting because that is the letter's position
          alldashes.pop(indexes[n])
          alldashes.insert(indexes[n], msg.content.lower())
          lettersguessed += 1
        lettersused.append(msg.content.lower())
        embed.set_field_at(0, name="Your Word", value="   ".join(alldashes), inline=False)
        embed.set_field_at(1, name="Letters Used", value=", ".join(["`"+ character + "`" for character in lettersused]), inline=False)
        embed.set_thumbnail(url=listofpictures[bodyparts])
        await ctx.send(embed=embed)
        await ctx.send("Correct!")
      else:
        lettersused.append(msg.content)
        bodyparts += 1

        embed.set_field_at(0, name="Your Word", value="   ".join(alldashes), inline=False)
        embed.set_field_at(1, name="Letters Used", value=", ".join(["`"+ character + "`" for character in lettersused]), inline=False)
        embed.set_thumbnail(url=listofpictures[bodyparts])
        await ctx.send(embed=embed)
        await ctx.send("Nope, that's not right.")
  if lettersguessed == len(lettersinword):
    await ctx.send(ctx.message.author.mention + " Congrats! You won!")
  elif bodyparts == 6:
    await ctx.send(ctx.message.author.mention + " Sorry, you lost. The word was " + hangmanword + ".")

@bot.command()
async def leaderboard(ctx, pass_Context=True):
  "displays leaderboard!"

  pointdict.clear()

  allmembers = list(filter(lambda m: not m.bot, ctx.guild.members))
  embed=discord.Embed(title="**Leaderboard for " + ctx.guild.name + "!**",color=0xfaba0a)
  for oneuser in allmembers:
    thevalue = random.randrange(1,1000)
    #picks a random value
    pointdict[oneuser.name + "#" + oneuser.discriminator] = thevalue
    #assigns that value to a user in pointdict dictionary
  pointvalues = sorted(pointdict, key=pointdict.get, reverse=True)
  #this is the keys (greatest to least)
  place = 1
  for everyvalue in pointvalues:
    if pointdict[everyvalue] == 1:
      embed.add_field(name="**" + str(place) + ". **" + everyvalue,value=":worm: `" + str(pointdict[everyvalue]) + " point`")
    else:
      embed.add_field(name="**" + str(place) + ". **" + everyvalue,value=":worm: `" + str(pointdict[everyvalue]) + " points`", inline=False)
    place += 1
  
  await ctx.send(embed=embed) 

@bot.command()
async def challenge(ctx, target:Member, pass_Context=True):
  "challenge another user!"
  await ctx.send(target.mention + ", would you like to participate in `" + ctx.author.name + "`'s challenge?")
  def checkresponse(rsp):
    return rsp.author == target and rsp.content.lower() in yesno
  try:
    rsp = await bot.wait_for("message", check=checkresponse, timeout=12.0)
  except asyncio.TimeoutError:
    await ctx.send(ctx.author.mention + " Sorry, it looks like `" + target.name + "` doesn't want to be challenged right now.")

  if rsp.content.lower() == 'yes' or rsp.content.lower() == 'y':
    await ctx.send(ctx.author.mention + " Your competitor said yes!")
    player1 = ctx.author
    player2 = target
    randomlist = list(random.choice(listoptions))
    print(listlabels[listoptions.index(randomlist)])
    randomword = random.choice(randomlist)
    print(randomword)
    url = requests.get("https://dictionaryapi.com/api/v3/references/collegiate/json/" + randomword + "?key=REPLACE_WITH_YOUR_API_KEY")
    url_json = url.json()
    ourdef = url_json[0].get("shortdef")
    embed=discord.Embed(title="**Challenge!**", description=f"**Category:** {listlabels[listoptions.index(randomlist)]}", color=0xce0909)
    embed.set_author(name=f"{player1.name} vs. {player2.name}")
    embed.add_field(name="Which word has the meaning:", value="`" + ourdef[0] + "`", inline=False)
    embed.set_footer(text="Respond with a word or type HINT | 60 seconds remaining")
    await ctx.send(embed=embed)
    def checkanswer(rsp):
      return (rsp.author == player1 or rsp.author == player2) and ' ' not in rsp.content
    try:
      starttime = time.time()
      askedhint=False
      print(rsp.author)
      yourpoints = (round(60 - (time.time() - starttime))/60)*1000 - int(askedhint)*100
      correctansweryet = False

      while time.time()-starttime <= 60 and not correctansweryet:
        rsp = await bot.wait_for("message", check=checkanswer, timeout=60.0)
        if rsp.content == "HINT":
          if askedhint:
            await ctx.send("You can't ask for another hint.")
          else:
            askedhint=True
            answeroptions = random.sample(randomlist, 3)
            answeroptions.insert(random.randrange(0, 3), randomword)
            hintembed=discord.Embed(title="**Challenge!**", color=0xce0909)
            hintembed.add_field(name="Hint:",value=f"The word is either `{answeroptions[0]}`, `{answeroptions[1]}`, `{answeroptions[2]}`, or `{answeroptions[3]}`.")
            hintembed.set_footer(text=f"Respond with a word | {round(60 - (time.time() - starttime))} seconds remaining")
            await ctx.send(embed=hintembed)
        else:
          if rsp.content == randomword:
            correctansweryet=True
            yourpoints = round((round(60 - (time.time() - starttime))/60)*100 - int(askedhint)*15)
            await ctx.send(f"{rsp.author.mention} Correct! `{rsp.author.name}` wins :worm: `{yourpoints}` points!")
          else:
            await ctx.send(f"{rsp.author.mention} No, that's not the right word.")
      if time.time()-starttime > 60 and not correctansweryet:
        await ctx.send("No one gave the correct answer. The word was " + randomword + ". You both will lose :worm: `100` points.")
    except asyncio.TimeoutError:
      await ctx.send("You guys ran out of time! No one responded. The word was " + randomword + ".")
  else:
    #they said no or n
    await ctx.send(ctx.author.mention + " Sorry, it looks like `" + target.name + "` doesn't want to be challenged right now.")

@bot.command()
async def updates(ctx):
  "displays daily developmental updates!"

  aprileleventh = ["`w!quiz` now mentions users, added exclamation point in `w!giveword`", "added `w!riddle`"]
  marchthirtieth = ["Now there are three categories in `w!challenge`"]
  marchtwentyninth = ["major improvements to `w!challenge`- all words are now in category: animal words- new categories to be added soon"]
  marchtwentyeighth = ["improved `w!challenge`"]
  marchtwentyseventh = ["changed wordlist for `w!challenge`", "improved `w!challenge`"]
  marchtwentysixth = ["`w!hangman` now accepts uppercase responses","improved `w!challenge`", "added error message for `w!remove` if argument is not already in wordlist"]

  fullupdates = {"**Sunday, April Eleventh**": aprileleventh, "**Tuesday, March 30**": marchthirtieth, "**Monday, March 29**": marchtwentyninth, "**Sunday, March 28**": marchtwentyeighth,"**Saturday, March 27**": marchtwentyseventh,"**Friday, March 26:**": marchtwentysixth}

  embed=discord.Embed(title="**Updates!**", color=0x188525)
  for day in fullupdates:
    embed.add_field(name=day, value="-" + "\n-".join(fullupdates.get(day)), inline=False)
  embed.set_footer(text="word of the day bot daily updates")
  await ctx.send(embed=embed)

@bot.command()
async def riddle(ctx):
  "answer riddles! (one word answers)"

  randomriddle = random.choice(list(riddles.keys()))
  print(randomriddle)
  await ctx.send(f"Riddle me this! {randomriddle}")
  def check(msg):
    return (" " not in msg.content) and (msg.author == ctx.author)
  msg = await bot.wait_for("message", check=check)
  if msg.content.lower() == riddles.get(randomriddle):
    await ctx.send(f"{ctx.author.mention} That's right! Good job!")
  else:
    await ctx.send(f"{ctx.author.mention} Sorry, that's not right. The correct answer is {riddles.get(randomriddle)}.")



@bot.event
async def on_message(message):
    # do some extra stuff here
    if message.content.lower() == "goodnight":
       await message.channel.send("goodnight!")
    await bot.process_commands(message)

@challenge.error
async def challenge_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You must mention the person you want to want to challenge.")

@define.error
async def define_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You must say what word you want me to define.")

@add.error
async def add_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You must say what word you want me to add.")

@remove.error
async def remove_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You must say what word you want me to remove.")



keep_alive()
bot.run(os.getenv('TOKEN'))
