# Evidencebot 

This is Evidencebot, a discord bot.

If you are hosting yourself, you will need to pass a Discord API client token to the bot
as a string, either via a command-line parameter or an environment variable. 
See [Configuration](#configuration) for more context.

## Configuration

### Command-line parameters

```
usage: main.py [-h] [--discord-api-token DISCORD_API_TOKEN]
               [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL} | -v]
               [--log-location {stdout,stderr,syslog,/path/to/file}]
               [--nodb] [--database-uri DATABASE_URI]

optional arguments:
  -h, --help            show this help message and exit
  --discord-api-token DISCORD_API_TOKEN
                        The Discord API client token
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set logging level
  -v, --verbose         Use verbose logging. Equivalent to --log-level DEBUG
  --log-location {stdout,stderr,syslog,/path/to/file}
                        Set the location for EvidenceBot's log
  --nodb                Disable the database connection, and all features
                        which require it.
  --database-uri DATABASE_URI
                        URI of the MongoDB database server
```

### Environment Variables
Evidencebot can also be configured with environment variables, although command-line arguments
will take precedence.

To see which environment variables can be used to configure Evidencebot, see [template.env](./docker/template.env).

## Commands

Current commands that can be used in Discord:

    !hello - Say "hello" to Evidencebot!

## Docker
Evidencebot has a straightforward Docker image that can be build based on the [Dockerfile](./docker/Dockerfile) in this 
repository. This image can be used for both deployment and testing purposes.

The Evidencebot image is designed to be used as an "executable," since it is only designed to
run Evidencebot and nothing else. 

For example:
```shell
$ docker run --env-file docker/.env --rm -it evidencebot --discord-api-token ...
```

The Evidencebot image has one build targets: `release`.

`release` contains only the dependencies to run Evidencebot, and only copies the source
directory.

The easiest way to create your `.env` is by copying [template.env](./docker/template.env), 
and then filling out whichever environment variables are desired. 
Leaving variables empty just means that default values will be used.