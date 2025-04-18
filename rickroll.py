import discord
from discord import app_commands
from logger import log_to_webhook, check_whitelist

def setup(bot):
    @bot.tree.command(name="rickroll", description="rick")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.describe(count="number of times")
    async def rickroll_command(interaction: discord.Interaction, count: int = 1):
        if count > 5:
            count = 5

        if not await check_whitelist(interaction):
            return

        await interaction.response.send_message("sigma", ephemeral=True)
        await interaction.followup.send("Never gonna give you up... https://www.youtube.com/watch?v=xvFZjo5PgG0")
        for _ in range(count - 1):
            await interaction.followup.send("Never gonna give you up... https://www.youtube.com/watch?v=xvFZjo5PgG0")
        
        await log_to_webhook(interaction, "rickroll", "", count)
