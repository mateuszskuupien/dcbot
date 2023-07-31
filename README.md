# Prometheus Discord Bot

Prometheus is a simple Discord bot written in Python that offers four basic commands: `!leave`, `!help`, `!join`, and `!ping` (ping pong).

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
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
4. Create a `.env` file in the root directory and add your bot token as follows: 
    DISCORD_TOKEN=your_discord_bot_token_here
5. Start the Python bot using the appropriate command for your bot script.

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

## Contributing

Contributions to Prometheus are welcome! If you have any improvements, bug fixes, or new features to propose, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
