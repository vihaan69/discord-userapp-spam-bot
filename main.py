import discord
from discord.ext import commands
import ok
import say
import rickroll
import aiohttp

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

WHITELIST = ["1086525614829355018"]

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.interaction_check
async def global_check(interaction: discord.Interaction):
    if str(interaction.user.id) not in WHITELIST:
        await interaction.response.send_message("Get out sigma", ephemeral=True)
        return False
    return True

async def log_to_webhook(interaction: discord.Interaction, command_name: str, message: str = "", count: int = 1):
    embed = discord.Embed(title="Some sigma used command:", color=discord.Color.red())
    embed.add_field(name="Username", value=interaction.user.name, inline=False)
    embed.add_field(name="User ID", value=str(interaction.user.id), inline=False)
    embed.add_field(name="Command Used", value=command_name, inline=False)
    embed.add_field(name="Amount of Times", value=str(count), inline=False)
    embed.add_field(name="What they said", value=message, inline=False)
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(embed=embed, username="Logger")

bot.log_to_webhook = log_to_webhook

ok.setup(bot)
say.setup(bot)
rickroll.setup(bot)

bot.run("YOUR BOT TOKEN")
