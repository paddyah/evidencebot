import discord
import re

from evidencebot.lib import exception

# TODO: write comment to describe this command group
evidence = discord.app_commands.Group(
    name="evidence",
    description="Controls acquisition and random redistribution of critical evidence.",
    guild_only=True,
)

@evidence.command()
async def store(interaction: discord.Interaction) -> None:
    """
    Sets channel for downloading evidence
    """
    channel = interaction.channel
    messages = []
    async for message in channel.history():
        match = re.search(r"^\"(.*)\"[^A-z]+([A-z]+)", message.content)
        if match is not None:
            messages.append({"content": message.content, "author": match.group(2).lower()})
    await interaction.response.send_message(f"{messages}")


@evidence.command()
async def retrieve(interaction: discord.Interaction) -> None:
    """
    Returns random evidence from set channel
    """
    await interaction.response.send_message(f"Returning random evidence")