# averio discord

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


Python application for product notifications via discord webhooks.

The scripts depends on [DiscordHooks](https://github.com/MeitarR/DiscordHooks), a python module for easily execute discord webhooks with embeds and more.


The script will request the new items from [averio](https://elk.averio.de/) website every 30 seconds,
 and post them on Discord channel using Webhook URL.

![Notification sample](https://i.imgur.com/hIBbS6U.png)

The notifications has simple and clean style, but can be edited quickly using DiscordHooks features.

## Installation and Usage

1. Install all the requirements, you may prefer to do it inside of a virtualenv.
    ```bash
    pip install -r requirements.txt
    ```

2. Run the main script
    ```bash
    python main.py <webhook_URL> [--username username] [--icon icon_url]
    ```

    Or use help in order to read the manual.
    ```bash
    python main.py --help
    ```

## Product object

Represent one product from [averio](https://elk.averio.de/).

The fields of the objects serialized into a discord embedded message.

-------
Made with 💗 for samolani by Aluma Gelbard. March 2020
