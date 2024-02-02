import discord
from discord import app_commands
from discord.ext import tasks
import os
from dotenv import load_dotenv
import dotenv

from yanyan_AddPlayer import add_player
from yanyan_CheckStatus import check_status
from yanyan_ResetSession import reset_session
from yanyan_All_ResetSession import allreset_session
from yanyan_DeletePlayer import delete_player
from yanyan_PlayerList import player_list
from yanyan_Online import get_online_list

dotenv_file = dotenv.find_dotenv()
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Logged in as hypixel status")
    await tree.sync() #  コマンドを同期
    print("command sync") #  コマンドを同期した事の確認
    check_status()
    # my_background_task.start()


@tree.command(name="command",description="Show command list")
async def command_command(interaction: discord.Interaction):
    embed = discord.Embed(title="/command　Show this command list\n/start　Start tracking\n/stop　Stop tracking\n/add [name]　Add player\n/delete [name]　Delete player\n/reset [name]　Reset player session\n/allreset　Reset sessions for all players\n/token [token]　Enter Hypixel token",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="add",description="Add player")
async def add_command(interaction: discord.Interaction,name:str):
    add_return = add_player(name)
    embed = discord.Embed(title=f"{add_return}",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="delete",description="Delete player")
async def delete_command(interaction: discord.Interaction,name:str):
    delete_player(name)
    embed = discord.Embed(title="Success",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="list",description="Player list")
async def list_command(interaction: discord.Interaction):
    players = player_list()
    players_text = ""
    for item in players:
        players_text = f"{players_text}{item}\n"
    embed = discord.Embed(title=players_text,color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="output",description="Output player list")
async def list_command(interaction: discord.Interaction):
    players = player_list()
    embed = discord.Embed(description=players,color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="input",description="Input player list")
async def list_command(interaction: discord.Interaction,players:str):
    players = players[1:len(players)-1].replace("'","").replace(" ","").split(",")
    print(players)
    text = ""
    await interaction.response.defer()
    for item in players:
        return_text = add_player(item)
        text = f"{text}\n{return_text}"
    embed = discord.Embed(description=text,color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="reset",description="Reset player session")
async def reset_command(interaction: discord.Interaction,name:str):
    return_text = reset_session(name)
    embed = discord.Embed(title=f"{return_text}",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="allreset",description="Reset sessions for all players")
async def allreset_command(interaction: discord.Interaction):
    return_text = allreset_session()
    embed = discord.Embed(title=f"{return_text}",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="start",description="Tracker Start")
async def start_command(interaction: discord.Interaction):
    my_background_task.start()
    embed = discord.Embed(title="✅ Start tracker!",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="stop",description="Tracker Stop")
async def stop_command(interaction: discord.Interaction):
    my_background_task.stop()
    embed = discord.Embed(title="🛑 Stop tracker!",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="token",description="Enter Hypixel token")
async def token_command(interaction: discord.Interaction,token:str):
    dotenv.set_key(dotenv_file, "HYPIXEL_TOKEN", token)
    embed = discord.Embed(title=f"Success!",color=0x0000ff)
    await interaction.response.send_message(embed=embed)


@tree.command(name="status",description="Player list")
async def status_command(interaction: discord.Interaction):
    players_text = ""
    await interaction.response.defer()
    player_status = get_online_list()
    for item in player_status[0]:
        players_text = f"{players_text}🟢  {item}\n"
    for item in player_status[1]:
        players_text = f"{players_text}🔴  {item}\n"
    embed = discord.Embed(title=players_text,color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tasks.loop(seconds=30)  # 何秒おきにステータスをチェックするか指定(今は60秒)
async def my_background_task():
    return_list = check_status()
    if return_list != ["API Key Error\nhttps://developer.hypixel.net/dashboard/"]:
        # channel_id = 1200281946643759145
        print(return_list)
        for item in return_list:
            if item[0] in [5,6]:
                channel_id = 1200281905174675577
            elif item[0] in [17,18]:
                channel_id = 1200281873973264435
            elif item[0] in [23,24]:
                channel_id = 1200947061038776443
            elif item[0] in [37,38]:
                channel_id = 1200281758084628520
            elif item[0] in [43,44]:
                channel_id = 1201526061570207795
            else:
                break
            
            channel = client.get_channel(channel_id)

            if item[0] % 2 == 1:
                embed = discord.Embed(title=f"🔷 [{item[6]}☆] {item[5]}{item[1]}",description=f"     Won with **{item[2]}**\n     Ws {item[3]}→ **{item[4]}**\n     Session FKDR : **{item[7]}**",color=0x00ff00)
                await channel.send(embed=embed)
            else:
                embed = discord.Embed(title=f"🔻 [{item[6]}☆] {item[5]}{item[1]}",description=f"     Lost with **{item[2]}**\n     Ws {item[3]}→ **{item[4]}**\n     Session FKDR : **{item[7]}**",color=0xff0000)
                await channel.send(embed=embed)
    else:
        embed = discord.Embed(title=f"{return_list[0]}",color=0x0000ff)
        await channel.send(embed=embed)
        my_background_task.stop()


client.run(TOKEN)  # \(0 w 0)/ ﾜｰｲ