import discord
from discord import app_commands
from logger import log_to_webhook, check_whitelist

def setup(bot):
    @bot.tree.command(name="ok", description="hi")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.describe(message="msg")
    @app_commands.describe(count="no. of times..")
    async def useable_only_users(interaction: discord.Interaction, message: str, count: int = 1):
        if not await check_whitelist(interaction):
            return

        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send("sigma")
        for i in range(count):
            await interaction.followup.send(f"{message}")
        
        await log_to_webhook(interaction, "ok", message, count)
