# importing libs
import discord
from discord.ext import commands
import nekos

# initializing cog
class nsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() # sends random anime feet image
    @commands.is_nsfw()
    async def feet(self, ctx):
        feetimg = nekos.img("feet")
        await ctx.send(feetimg)

    @commands.command() # sends random anime yuri image
    @commands.is_nsfw()
    async def yuri(self, ctx):
        yuriimg = nekos.img("yuri")
        await ctx.send(yuriimg)

    @commands.command() # sends random anime trap image
    @commands.is_nsfw()
    async def trap(self, ctx):
        trapimg = nekos.img("trap")
        await ctx.send(trapimg)

    @commands.command() # sends random anime futa image
    @commands.is_nsfw()
    async def futa(self, ctx):
        futaimg = nekos.img("futanari")
        await ctx.send(futaimg)

    @commands.command() # sends random anime cum image
    @commands.is_nsfw()
    async def cum(self, ctx):
        cumimg = nekos.img("cum")
        await ctx.send(cumimg)

    @commands.command() # sends random anime blowjob image
    @commands.is_nsfw()
    async def bj(self, ctx):
        bjimg = nekos.img("bj")
        await ctx.send(bjimg)

    @commands.command() # sends random gasm image
    async def gasm(self, ctx):
        gasmimg = nekos.img("gasm")
        await ctx.send(gasmimg)

    @commands.command() # sends random anime anal image
    @commands.is_nsfw()
    async def anal(self, ctx):
        analimg = nekos.img("anal")
        await ctx.send(analimg)

    @commands.command() # sends random anime hentai image
    @commands.is_nsfw()
    async def hentai(self, ctx):
        hentaiimg = nekos.img("hentai")
        await ctx.send(hentaiimg)

    @commands.command() # sends random anime pussy image
    @commands.is_nsfw()
    async def pussy(self, ctx):
        pussyimg = nekos.img("pussy")
        await ctx.send(pussyimg)

    @commands.command() # sends random anime tits image
    @commands.is_nsfw()
    async def tits(self, ctx):
        titsimg = nekos.img("tits")
        await ctx.send(titsimg)

    @commands.command() # sends random anime kiss image
    @commands.is_nsfw()
    async def kiss(self, ctx):
        kissimg = nekos.img("kiss")
        await ctx.send(kissimg)

    @commands.command() # sends random anime femdom image
    @commands.is_nsfw()
    async def femdom(self, ctx):
        femdomimg = nekos.img("femdom")
        await ctx.send(femdomimg)
    
    @commands.command() # sends random anime spank image
    @commands.is_nsfw()
    async def spank(self, ctx):
        spankimg = nekos.img("spank")
        await ctx.send(spankimg)
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send("This command cannot be used outside of a NSFW channel.")

# makes the cog be recognized by the bot
def setup(bot: commands.Bot):
    bot.add_cog(nsfwCog(bot))

