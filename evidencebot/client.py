import logging

import discord
import discord.ext.commands

from evidencebot import commands
from evidencebot import config
from evidencebot import db
from evidencebot import log
from evidencebot.lib import exception, util


async def on_ready() -> None:
    """
    Determines what the bot does as soon as it is logged into discord
    """
    if not evidencebot.user:
        raise exception.EvidenceBotInternalError("Evidencebot is not logged in to Discord")
    log.info(f"Logged in as {evidencebot.user}")
    synced = await evidencebot.tree.sync()
    log.info(f"Synced {len(synced)} command(s)")


async def on_interaction(interaction: discord.Interaction) -> None:
    """
    Provides logging on interaction ingress
    """
    log.interaction(
        interaction,
        f"{util.parse_invocation(interaction.data)} from {interaction.user}",
    )


async def on_command_error(
    interaction: discord.Interaction, error: discord.app_commands.AppCommandError
) -> None:
    command = interaction.command
    if not isinstance(command, discord.app_commands.Command):
        log.exception(error)
        return

    invocation = util.parse_invocation(interaction.data)

    if isinstance(error, exception.EvidencebotInternalError):
        # For intentionally thrown internal errors
        log.interaction(
            interaction,
            f"Raised an internal exception: ",
            level=logging.WARNING,
            exc_info=error,
        )
        err_msg = f"Internal error occurred with `{invocation}`"
    elif isinstance(error, exception.EvidencebotUserError):
        # If the error is user-facing, we want to send it directly to the user
        err_msg = str(error)
        log.interaction(interaction, err_msg)
    else:
        # For uncaught exceptions
        # (discord.py wraps these in a CommandInvokeError and re-raises)
        if isinstance(error, discord.app_commands.CommandInvokeError):
            original = error.original
        else:
            original = error
        log.interaction(
            interaction,
            f"Raised an unhandled exception: ",
            exc_info=original,
            level=logging.ERROR,
        )
        err_msg = f"Unhandled error occurred with `{invocation}`"

    await interaction.response.send_message(
        err_msg,
        ephemeral=True,
    )


evidencebot = discord.ext.commands.Bot(
    command_prefix="/",
    intents=discord.Intents().all(),
    activity=discord.Game(name="• /hello"),
)

evidencebot.tree.add_command(commands.hello)

evidencebot.add_listener(on_ready)
evidencebot.add_listener(on_interaction)
evidencebot.tree.error(on_command_error)
