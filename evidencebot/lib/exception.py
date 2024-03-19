import discord


class EvidencebotUserError(discord.app_commands.AppCommandError):
    """
    Exception which carries a message to be displayed to the user
    """


class EvidencebotInternalError(discord.app_commands.AppCommandError):
    """
    Exception which is thrown on purpose, but whose content would likely confuse a user.
    """