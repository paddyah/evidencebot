import discord
import re
import random

from evidencebot.lib import exception

# TODO: write comment to describe this command group
evidence = discord.app_commands.Group(
    name="evidence",
    description="Controls acquisition and random redistribution of critical evidence.",
    guild_only=True,
)

messages = []

@evidence.command()
async def store(interaction: discord.Interaction) -> None:
    """
    Sets channel for downloading evidence
    """
    channel = interaction.channel
    async for message in channel.history():
        match = re.search(r"^\"(.*)\"[^A-z]+([A-z]+)", message.content)
        if match is not None:
            messages.append({"content": message.content, "author": match.group(2).lower()})
    await interaction.response.send_message(f"Stored evidence in #{channel.name}")


@evidence.command()
async def retrieve(interaction: discord.Interaction, author_name: str =None) -> None:
    """
    Returns random evidence from set channel
    """
    if not messages:
        await interaction.response.send_message(f"No messages stored")
    if author_name is None:
        await interaction.response.send_message(f"{random.choice(messages)['content']}")
    else:
        author_messages = list(filter(lambda message: message['author'] == author_name.lower(), messages))
        if not author_messages:
            await interaction.response.send_message(f"No messages stored by {author_name}")
        await interaction.response.send_message(f"{random.choice(author_messages)['content']}")
