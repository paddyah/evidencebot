FROM python:3.9.6-slim as build
WORKDIR /opt/evidencebot/

# Install requirements.
COPY requirements.txt requirements.txt
RUN \
    apt-get update -y && \
    # gcc is required to build package aiohttp (https://docs.aiohttp.org/en/stable/) required by discord.py
    apt-get install --no-install-recommends -y gcc=4:10.2.1-1

# Set up venv.
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Prepare run image.
FROM python:3.9.6-slim as run-base
WORKDIR /opt/evidencebot/
ENV PATH="/opt/venv/bin:$PATH"
COPY . .
ENTRYPOINT ["python3", "main.py"]

# Run release build.
FROM run-base as release
COPY --from=build /opt/venv /opt/venv
