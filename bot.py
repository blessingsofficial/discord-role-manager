import argparse
import asyncio
import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing from .env")


def get_args():
    parser = argparse.ArgumentParser(
        description="Add or remove a Discord role from users who reacted to a message."
    )

    parser.add_argument("--server-id", type=int, required=True)
    parser.add_argument("--message-id", type=int, required=True)
    parser.add_argument("--role-id", type=int, required=True)
    parser.add_argument(
        "--action",
        choices=["ADD", "REMOVE"],
        required=True
    )

    return parser.parse_args()


class RoleManager(discord.Client):

    def __init__(self, args):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.members = True

        super().__init__(intents=intents)
        self.args = args

    async def find_message(self, guild, message_id):
        channels = await guild.fetch_channels()

        for channel in channels:
            if not isinstance(channel, discord.TextChannel):
                continue

            try:
                return await channel.fetch_message(message_id)
            except discord.NotFound:
                continue
            except discord.Forbidden:
                continue
            except discord.HTTPException:
                continue

        return None

    async def on_ready(self):

        print(f"Logged in as {self.user}")

        guild = self.get_guild(self.args.server_id)

        if guild is None:
            print("ERROR: Server not found.")
            await self.close()
            return

        roles = await guild.fetch_roles()

        print("\nRoles visible to the bot:")

        for server_role in roles:
            print(f"{server_role.name} -> {server_role.id}")

        role = discord.utils.get(
            roles,
            id=self.args.role_id
        )

        if role is None:
            print("\nERROR: Requested role was not found.")
            await self.close()
            return

        print(f"\nUsing role: {role.name} ({role.id})")

        print("\nSearching for the message...")

        message = await self.find_message(
            guild,
            self.args.message_id
        )

        if message is None:
            print("ERROR: Message not found.")
            await self.close()
            return

        print(f"Message found in #{message.channel.name}")

        users = set()

        print("Checking reactions...")

        for reaction in message.reactions:

            async for user in reaction.users():

                if user.bot:
                    continue

                try:
                    member = guild.get_member(user.id)

                    if member is None:
                        member = await guild.fetch_member(user.id)

                    users.add(member)

                except (discord.NotFound, discord.Forbidden):
                    print(f"Could not find member: {user}")

        print(f"Found {len(users)} reacting user(s).")

        for member in users:

            try:

                if self.args.action == "ADD":

                    if role in member.roles:
                        print(
                            f"SKIPPED: {member} already has {role.name}"
                        )
                    else:
                        await member.add_roles(
                            role,
                            reason="Discord role manager bounty script"
                        )

                        print(
                            f"ADDED: {member} -> {role.name}"
                        )

                else:

                    if role not in member.roles:
                        print(
                            f"SKIPPED: {member} does not have {role.name}"
                        )
                    else:
                        await member.remove_roles(
                            role,
                            reason="Discord role manager bounty script"
                        )

                        print(
                            f"REMOVED: {member} -> {role.name}"
                        )

            except discord.Forbidden:
                print(
                    f"FAILED: No permission to manage {member}"
                )

            except discord.HTTPException as error:
                print(
                    f"FAILED: Discord API error for {member}: {error}"
                )

        print("\nFinished.")
        await self.close()


async def run():

    args = get_args()

    client = RoleManager(args)

    try:
        await client.start(TOKEN)

    except discord.LoginFailure:
        print("ERROR: Invalid Discord bot token.")

    except discord.PrivilegedIntentsRequired:
        print("ERROR: Enable Server Members Intent.")


if __name__ == "__main__":
    asyncio.run(run())
