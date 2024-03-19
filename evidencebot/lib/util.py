from typing import Optional, cast, TYPE_CHECKING

import discord
import discord.ext.commands

if TYPE_CHECKING:
    pass

def parse_invocation(interaction: discord.Interaction) -> str:
    """Returns the command involacion parsed from the raw interaction data"""

    def impl(data: dict) -> str:
        out = []
        name: Optional[str] = data.get("name")
        options: list[dict] = data.get("options", [])
        value: Optional[str] = data.get("value")
        if value:
            out.append(value)
        elif name:
            out.append(name)
        for option in options:
            out.append(impl(option))

        return " ".join(out)

    if not interaction:
        return ""

    if interaction.command:
        prefix = cast(discord.ext.commands.Bot, interaction.client).command_prefix
    else:
        prefix = ""
    return f"{prefix}{impl(cast(dict, interaction.data))}"