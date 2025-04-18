import discord
from discord import app_commands
from logger import log_to_webhook, check_whitelist

def setup(bot):
    @bot.tree.command(name="say", description="say one msg")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.describe(message="msg")
    async def say_command(interaction: discord.Interaction, message: str):
        if not await check_whitelist(interaction):
            return

        await interaction.response.send_message("sigma", ephemeral=True)
        await interaction.followup.send(f"{message}")
        
        await log_to_webhook(interaction, "say", message)
