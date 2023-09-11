# Prometheus Discord Bot

Prometheus is a simple Discord bot written in Python that offers basic commands: `!leave`, `!help`, `!join`, `!ticket` and `!ping` (ping pong). It has also a `ticket system` and `role-assign system` which can be really helpful for administrators.

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Prometheus is a bot designed to enhance your Discord server with minimalistic but essential functionality. Whether you need assistance, want to interact with other users, or just want to play a quick ping pong game, Prometheus has got you covered.

## Setup

To run Prometheus on your Discord server, you'll need to follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies (if any) for the Python bot.
3. Set up a new Discord application and obtain a bot token from the Discord Developer Portal.
4. Configure config.json File:
- Create a config.json file in the root directory of the cloned repository.
- Inside the config.json file, add your bot token like this:  `BOT_TOKEN = your_bot_token`
5. Start the Python bot using the appropriate command for your bot script.
6. Invite the Bot to Your Server:

## Usage

Once Prometheus is up and running on your server, you can start using its commands by typing them in any text channel. For example, to summon Prometheus to a voice channel, use `!join`. To see all available commands, type `!help`.

## Commands

- **!leave**
  - Description: Instruct the bot to leave the voice channel.
  - Usage: `!leave`

- **!help**
  - Description: Get a list of available commands and usage instructions.
  - Usage: `!help`

- **!join**
  - Description: Summon the bot to join your voice channel.
  - Usage: `!join`

- **!ping**
  - Description: Play a quick game of ping pong with the bot.
  - Usage: `!ping`

- **!ticket**
  - Description: Ticket system, after typing the command it creates a channel where administration can help you.
  - Usage: `!ticket`

## Contributing

Contributions to Prometheus are welcome! If you have any improvements, bug fixes, or new features to propose, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
