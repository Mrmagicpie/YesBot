#
#           YesBot utils.py | Copyright (c) 2020 Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    #
    @commands.command()
    @commands.cooldown(1, 1, type=BucketType.user)
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, o: discord.Member = None, *, reason = None):

        if o == None:

            embed = discord.Embed(
                title="Ban usage",
                description=f"""
YesBot Ban Usage:

``{ctx.prefix}ban (member)``
                """,
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(
                icon_url=self.bot.user.avatar_url,
                text="YesBot Moderation"
            )
            await ctx.send(embed=embed)

        else:

            if reason == None:

                reason = "No reason specified."


            embed = discord.Embed(
                title=f"Ban {o.display_name}?",
                description=f"""
React with ✅ to ban this user for ``{reason}``!
                """,
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(
                icon_url=self.bot.user.avatar_url,
                text="YesBot Moderation"
            )
            msg = await ctx.send(embed=embed)

            await msg.add_reaction('✅')

            def ok(reaction, user):

                if ctx.author.id == user.id:
                    return str(reaction.emoji) == "✅"

            reaction, user = await self.bot.wait_for("reaction_add", check=ok)

            if str(reaction.emoji) == "✅":

                await msg.clear_reactions()

                rip = discord.Embed(
                    title=f"You have been banned from {ctx.guild.name}!",
                    description=f"""
You have been banned from {ctx.guild.name} for:
```
{reason}
```
                    """,
                    colour=discord.Colour.red(),
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(
                    icon_url=self.bot.user.avatar_url,
                    text="YesBot Moderation"
                )
                oop = discord.Embed(title=f"Banning {o.display_name}!")
                lmao = discord.Embed(
                    title=f"Banned {o.display_name}",
                    description=f"""
Banned {o.mention} for:
```
{reason}
```
                    """
                )
                await msg.edit(embed=oop)
                await o.ban(reason=reason)
                await o.send(embed=rip)
                await msg.edit(embed=lmao)


    @commands.command()
    @commands.cooldown(1, 1, type=BucketType.user)
    async def help(self, ctx):

        embed = discord.Embed(
            title="YesBot help",
            description=f"""
Below is a list of currently available YesBot commands!

            """,
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(
            name="Ban (@user) [reason]",
            value="""
Requires: ``ban_members``
> Ban a user from your guild
            """
        )
        embed.add_field(
            name="Echo [What to echo]",
            value="""
Requires: ``send_messages``
> Echo something as the bot
            """
        )
        embed.set_footer(
            icon_url=self.bot.user.avatar_url,
            text="YesBot Utilities"
        )
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 2, type=BucketType.user)
    async def echo(self, ctx, *, echo = None):

        mentions = discord.AllowedMentions(everyone=False, users=False, roles=False)

        if echo == None:

            await ctx.send('Please specify something to echo!')

        else:

            await ctx.message.delete()
            await ctx.send(f"""
{echo}
_ _
> {ctx.author.mention}
        """, allowed_mentions=mentions)




    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        embed = discord.Embed(
            title="Uh oh!",
            description=f"""
Uh oh! We ran into a problem.
```css
{error}
```
            """,
            colour=discord.Colour.red(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(
            icon_url=self.bot.user.avatar_url,
            text="Oh no, we ran into a problem!"
        )
        await ctx.send(embed=embed)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
def setup(bot):
    bot.add_cog(utils(bot))