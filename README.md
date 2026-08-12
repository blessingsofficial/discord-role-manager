Discord Role Manager
A simple command-line tool that adds or removes a Discord role from users who reacted to a specific Discord message.
Features
Runs locally from the command line
Finds users who reacted to a specified message
Adds a role to those users with ADD
Removes a role from those users with REMOVE
Skips users who already have the role when using ADD
Skips users who do not have the role when using REMOVE
Logs role changes and skipped users
Uses an environment variable for the Discord bot token
Does not run as a continuously running bot
Requirements
Python 3.13
A Discord bot
The bot must be added to your Discord server
The bot needs permission to manage the target role
The bot's role must be higher than the role it is managing
Server Members Intent must be enabled
Installation
Clone the repository and enter the project directory:
git clone YOUR_REPOSITORY_URL
cd discord-role-manager
Install the required packages:
py -3.13 -m pip install -r requirements.txt
Environment Variable
Create a file named .env in the project directory:
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
Replace YOUR_DISCORD_BOT_TOKEN with your Discord bot token.
Never commit or share the .env file.
Usage
The script requires four arguments:
--server-id
--message-id
--role-id
--action
Add the role
py -3.13 bot.py --server-id SERVER_ID --message-id MESSAGE_ID --role-id ROLE_ID --action ADD
Remove the role
py -3.13 bot.py --server-id SERVER_ID --message-id MESSAGE_ID --role-id ROLE_ID --action REMOVE
Example
py -3.13 bot.py --server-id 1536802345491497053 --message-id 1536808716433883228 --role-id 1536901621940879443 --action ADD
The script finds users who reacted to the specified message and adds the selected role to users who do not already have it.
For removal:
py -3.13 bot.py --server-id 1536802345491497053 --message-id 1536808716433883228 --role-id 1536901621940879443 --action REMOVE
Logging
The script logs actions such as:
ADDED: username -> role
REMOVED: username -> role
SKIPPED: username already has role
SKIPPED: username does not have role
This makes it clear which users were changed and which users were skipped.
Discord Configuration
In the Discord Developer Portal, enable:
Server Members Intent
The bot also needs permission to manage the target role.
Make sure the bot's highest role is above the role that the script needs to add or remove.
Security
The Discord bot token is loaded from the DISCORD_TOKEN environment variable.
Do not upload .env to GitHub or share your bot token publicly.
License
This project is provided for demonstration and bounty submission purposes.
