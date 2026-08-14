Discord Role Manager

A simple command-line tool for adding or removing a Discord role from users who reacted to a specific Discord message.

What It Does
The script checks the reactions on a selected Discord message, identifies the users who reacted, and then either adds or removes a specified role from those users.
It runs locally, performs the requested action, and exits when the task is complete.

Features
Runs locally from the command line
Finds users who reacted to a specific Discord message
Supports ADD and REMOVE actions
Skips users who already have the role during ADD
Skips users who do not have the role during REMOVE
Logs successful role changes and skipped users
Loads the Discord bot token from an environment variable
Does not run as a continuously running bot

Requirements
Python 3.13
A Discord bot
The bot must be added to the target Discord server
The bot must have permission to manage the target role
The bot's highest role must be above the role being managed
Server Members Intent must be enabled

Discord Configuration
Before running the script, configure your Discord bot in the Discord Developer Portal.
Enable:
Server Members Intent
Make sure the bot has permission to manage the target role and that its highest role is positioned above the role it needs to add or remove.

Installation
Clone the repository and enter the project directory:
git clone https://github.com/blessingsofficial/discord-role-manager.git
cd discord-role-manager
Install the required packages:
py -3.13 -m pip install -r requirements.txt

Environment Variable
Create a .env file in the project directory:
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
Replace YOUR_DISCORD_BOT_TOKEN with your Discord bot token.
Never commit or share the .env file.

Usage
The script requires four arguments:
--server-id — Discord server ID
--message-id — ID of the message containing the reaction
--role-id — ID of the role to add or remove
--action — ADD or REMOVE

Test Configuration
Server ID: 1536802345491497053
Message ID: 1536808716433883228
Role ID: 1536901621940879443

Add a Role
py -3.13 bot.py --server-id 1536802345491497053 --message-id 1536808716433883228 --role-id 1536901621940879443 --action ADD

Remove a Role
py -3.13 bot.py --server-id 1536802345491497053 --message-id 1536808716433883228 --role-id 1536901621940879443 --action REMOVE
The script checks the selected message, finds users who reacted, and performs the requested role action.
Users who already have the role are skipped during ADD, while users who do not have the role are skipped during REMOVE.

Logging
The script logs role changes and skipped users, for example:
ADDED: username -> role
REMOVED: username -> role
SKIPPED: username already has role
SKIPPED: username does not have role
This makes it easy to see which users were successfully updated and which users were skipped.

Security
The Discord bot token is loaded from the DISCORD_TOKEN environment variable.
Do not:
Upload .env to GitHub
Share your bot token publicly
Include your bot token directly in the source code

License
This project is provided for demonstration and bounty submission purposes.
