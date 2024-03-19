from evidencebot import config

config.populate_config_from_command_line()

from evidencebot.client import evidencebot
from evidencebot import log



def main() -> None:
    """
    Main function, initializes EvidenceBot and then loops
    :return: Exit status of discord.Client.run()
    """
    log.set_third_party_logging()

    # !! DO NOT HARDCODE THE TOKEN !!
    evidencebot.run(config.discord_api_token)


if __name__ == "__main__":
    main()