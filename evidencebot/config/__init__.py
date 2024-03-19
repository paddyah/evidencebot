import argparse
import logging
import os
import urllib.parse

from evidencebot.config import validators

# Discord API token
discord_api_token: str

# The logging level for EvidenceBot
log_level: str
# The location for EvidenceBot's log
log_location: logging.Handler


def populate_config_from_command_line() -> None:
    parser = argparse.ArgumentParser()

    # API Tokens
    parser.add_argument(
        "--discord-api-token",
        help="The Discord API client token",
        default=os.getenv("EVIDENCEBOT_DISCORD_CLIENT_TOKEN"),
        type=str,
    )

    # Logging Configuration
    logging_verbosity_group = parser.add_mutually_exclusive_group()
    # Accept all log levels recognized by the logging library except NOTSET
    logging_verbosity_group.add_argument(
        "--log-level",
        help="Set logging level",
        choices=[
            logging.getLevelName(level)
            for level in (
                logging.DEBUG,
                logging.INFO,
                logging.WARN,
                logging.ERROR,
                logging.CRITICAL,
            )
        ],
        default=os.getenv("EVIDENCEBOT_LOG_LEVEL", logging.getLevelName(logging.INFO)),
        type=str,
    )
    logging_verbosity_group.add_argument(
        "-v",
        "--verbose",
        help="Use verbose logging. Equivalent to --log-level DEBUG",
        dest="log_level",
        action="store_const",
        const=logging.getLevelName(logging.DEBUG),
    )
    parser.add_argument(
        "--log-location",
        help="Set the location for EvidenceBot's log",
        default=os.getenv("EVIDENCEBOT_LOG_LOCATION", "stdout"),
        metavar="{stdout,stderr,syslog,/path/to/file}",
        type=validators.validate_log_location,
    )

    args = parser.parse_args()

    global discord_api_token
    discord_api_token = args.discord_api_token

    global log_level
    global log_location
    log_level = args.log_level
    log_location = args.log_location


populate_config_from_command_line()