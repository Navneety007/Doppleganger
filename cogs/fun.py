import asyncio
import discord
from discord.ext import commands
import random

roasts = ["I'd give you a nasty look but you've already got one",
"If you were going to be two-faced at least make one of them pretty",
"I love what you've done with your hair. How do you get it to come out of the nostrils like that",
"If laughter is the best medicine your face must be curing the world",
"The only way you'll ever get laid is if you crawl up a chicken's ass and wait",
"It looks like your face caught fire and someone tried to put it out with a hammer",
"I'd like to see things from your point of view... but I can't seem to get my head that far up your ass",
"I've seen people like you before but I had to pay admission",
"Scientists say the universe is made up of neutrons protons and electrons. They forgot to mention morons",
"You're so fat you could sell shade",
"Your lips keep moving but all I hear is Blah blah blah",
"Your family tree must be a cactus because everyone on it is a prick",
"You'll never be the man your mother is",
"I'm sorry was I meant to be offended? The only thing offending me is your face",
"Someday you'll go far... and I hope you stay there",
"Which sexual position produces the ugliest children? Ask your mother",
"Stupidity's not a crime so you're free to go",
"If I had a face like yours I'd sue my parents",
"Your doctor called with your colonoscopy results. Good news - they found your head",
"No those pants don't make you look fatter - how could they",
"Save your breath - you'll need it to blow up your date",
"You're not stupid you just have bad luck when thinking",
"If you really want to know about mistakes you should ask your parents",
"Please keep talking. I always yawn when I am interested",
"The zoo called. They're wondering how you got out of your cage",
"Whatever kind of look you were going for you missed",
"I was hoping for a battle of wits but you appear to be unarmed",
"Aww it's so cute when you try to talk about things you don't understand",
"I don't know what makes you so stupid but it really works",
"You are proof that evolution can go in reverse",
"Brains aren't everything. In your case they're nothing",
"I thought of you today It reminded me to take the garbage out",
"You're so ugly when you look in the mirror your reflection looks away",
"I'm sorry I didn't get that - I don't speak idiot",
"Quick - check your face! I just found your nose in my business",
"It's better to let someone think you're stupid than open your mouth and prove it",
"Hey your village called - they want their idiot back",
"Were you born this stupid or did you take lessons",
"I've been called worse by better",
"You're such a beautiful intelligent wonderful person. Oh I'm sorry I thought we were having a lying competition",
"I may love to shop but I'm not buying your bull",
"I'd slap you but I don't want to make your face look any better",
"Calling you an idiot would be an insult to all stupid people",
"I just stepped in something that was smarter than you... and smelled better too",
"You have the right to remain silent because whatever you say will probably be stupid anyway",
"Your so ugly Hello Kitty said goodbye to you",
"Could you take a couple steps back. I'm allergic to idiots",
"Your so big a picture of you would fall off the wall",
"You look like a before picture",
"You know that feeling when you step in gum... that's how i feel looking at you",
"You couldn't find logic if it hit you in the face",
"My phone battery lasts longer than your relationships",
"Oh you’re talking to me. I thought you only talked behind my back",
"Too bad you can’t count jumping to conclusions and running your mouth as exercise",
"If I wanted a bitch I would have bought a dog",
"My business is my business. Unless you’re a thong... get out of my ass",
"It’s a shame you can’t Photoshop your personality",
"Jealousy is a disease. Get well soon",
"When karma comes back to punch you in the face... I want to be there in case it needs help",
"You have more faces than Mount Rushmore",
"Maybe you should eat make-up so you’ll be pretty on the inside too",
"Whoever told you to be yourself gave you really bad advice",
"I thought I had the flu... but then I realized your face makes me sick to my stomach",
"You should try the condom challenge. If your gonna act like a dick then dress like one too",
"I’m jealous of people who don’t know you",
"You sound reasonable… Time to up my medication",
"Please say anything. It’s so cute when you try to talk about things you don’t understand",
"I suggest you do a little soul searching. You might just find one",
"You should try this new brand of chap stick. The brand is Elmer's",
"I'd smack you if it wasn't animal abuse",
"Why is it acceptable for you to be an idiot but not for me to point it out",
"If you’re offended by my opinion... you should hear the ones I keep to myself",
"If you’re going to be a smart ass... first you have to be smart. Otherwise you’re just an ass",
"I’m not an astronomer but I am pretty sure the earth revolves around the sun and not you",
"Keep rolling your eyes. Maybe you’ll find your brain back there",
"No no no. I am listening. It just takes me a minute to process that much stupidity", 
"Sorry... what language are you speaking. Sounds like Bullshit",
"Everyone brings happiness to a room. I do when I enter... you do when you leave",
"You’re the reason I prefer animals to people", 
"You’re not stupid; you just have bad luck when thinking",
"Please... keep talking. I always yawn when I am interested",
"Were you born this stupid or did you take lessons?",
"You have the right to remain silent because whatever you say will probably be stupid anyway",
"Hey you have something on your chin… no… the 3rd one down",
"You’re impossible to underestimate",
"You’re kinda like Rapunzel except instead of letting down your hair... you let down everyone in your life",
"You look like your father would be disappointed in you if he stayed",
"You look like you were bought on the clearance shelf", 
"Take my lowest priority and put yourself beneath it",
"You are a pizza burn on the roof of the world’s mouth",
"People like you are the reason God doesn’t talk to us anymore",
"You’re so dense that light bends around you",
"I don’t have the time or the crayons to explain anything to you",
"You’re not as dumb as you look. That's saying something",
"You’ve got a great body. Too bad there’s no workout routine for a face",
"You’re about as important as a white crayon",
"I fear no man. But your face... it scares me",
"We get straight to the point. We aren't Willy Wonka"]

class Fun(commands.Cog):
    """Fun commands for fun......obviously"""
    def __init__(self,bot):
        self.bot = bot
        self.colors = self.bot.colors


    @commands.command(aliases = ['kills'])
    async def kill(self,ctx,member : discord.Member):
        """Kill a member <a:evil_laugh:863004647333429269>"""
        killing =  [f"{member.name} was shot by {ctx.author.name} using <item>",
            f"{member.name} walked into a cactus whilst trying to escape {ctx.author.name}",
            f"{member.name} drowned whilst trying to escape {ctx.author.name}",
            f"{member.name} was fireballed by {ctx.author.name} using Catapult",
            f"{member.name} was killed by {ctx.author.name} using ShotGun",
            f"{member.name} walked into fire whilst fighting {ctx.author.name}",
            f"{member.name} tried to swim in lava to escape {ctx.author.name}",
            f"{member.name} walked on danger zone due to {ctx.author.name}",
            f"{member.name} was burnt to a crisp whilst fighting {ctx.author.name}",
            f"{member.name} was slain by {ctx.author.name} using Axe",
            f"{member.name} was pummeled by {ctx.author.name}",
            f"{member.name} fell off a ladder",
            f"{member.name} fell off some vines",
            f"{member.name} fell out of the water",
            f"{member.name} was doomed to fall by {ctx.author.name}",
            f"{member.name} was doomed to fall by {ctx.author.name} using Log",
            f"{member.name} fell too far and was finished by {ctx.author.name}",]

        await ctx.send(random.choice(killing))

    @commands.command()
    async def topic(self,ctx):
        """Get a topic to start a dead chat"""
        file = open('./Assets/text/questions.txt','r')
        topic = random.choice([i for i in file])
        await ctx.send(embed = discord.Embed(description = topic,color = random.choice(self.colors)))

    @commands.command()
    async def roast(self,ctx,member:discord.Member):
        """Roast a member"""
        if member.id==779743087572025354:
            await ctx.send("You trying to roast my owner!? give up alr baka :D")
            return
        roast = random.choice(roasts)
        await ctx.send(f"{member.name}, {roast}")

    @commands.command(aliases = ['cafe'])
    async def coffee(self, ctx, member: discord.Member =None):
        """Enjoy coffee with someone"""
        if member == ctx.author or not member:
            await ctx.send(embed=discord.Embed(description=f"☕ | {ctx.author.name} Enjoying Coffee alone :smirk: ", color=random.choice(self.colors)))
            return
        elif member == self.bot.user:
            await ctx.send(embed=discord.Embed(description="☕ | Don't worry I will drink coffee with you  *sips*", color=random.choice(self.colors)))
            return
        elif member.bot: return;

        coffee_offer = f"☕ | {member.mention}, you got a coffee offer from {ctx.author.name}"
        coffee_msg = await ctx.send(embed=discord.Embed(description=coffee_offer,color=random.choice(self.colors)))
        await coffee_msg.add_reaction('☕')

        def check(reaction, user):
            return user == member and str(reaction.emoji) == '☕'

        try:
            await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(embed=discord.Embed(description=f"Looks like {member.name} are busy", color=random.choice(self.colors)))
        else:
            await coffee_msg.delete()
            await ctx.send(embed=discord.Embed(description=f"☕ | Yay! {ctx.author.name} and {member.name} are enjoying coffee together!", color=random.choice(self.colors)))
    
    @commands.command(aliases = ['drink'])
    async def beer(self, ctx, member: discord.Member=None ):
        """Drink beer with someone"""
        if member == ctx.author or not member:
            await ctx.send(embed=discord.Embed(description=f"🍺 | {ctx.author.name} Party Time !! , *Enjoing Beer*", color=random.choice(self.colors)))
            return
        elif member == self.bot.user:
            await ctx.send(embed=discord.Embed(description="🍺 | Don't worry I will Enjoy beer with you  *brrr*", color=random.choice(self.colors)))
            return
        elif member.bot: return;

        coffee_offer = f"🍺 | {member.mention}, you got Beer Party offer from {ctx.author.name}"
        coffee_msg = await ctx.send(embed=discord.Embed(description=coffee_offer,color=random.choice(self.colors)))
        await coffee_msg.add_reaction('🍺')

        def check(reaction, user):
            return user == member and str(reaction.emoji) == '🍺'

        try:
            await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(embed=discord.Embed(description=f"Looks like {member.name} is busy", color=random.choice(self.colors)))
        else:
            await coffee_msg.delete()
            await ctx.send(embed=discord.Embed(description=f"🍺 | Yay! {ctx.author.name} and {member.name} are enjoying Beer Party!", color=random.choice(self.colors)))
    
def setup(bot):
    bot.add_cog(Fun(bot))
