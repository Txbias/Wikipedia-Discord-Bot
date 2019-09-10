import discord
import re
import requests
import json

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!") != -1:
        content = message.content
        content = content.replace("!", "", 1)
        awnser = handle(content)
        await message.channel.send(awnser)
    

def handle(text):
    awnser = ""

    replacement1 = re.compile(re.escape("who is"), re.IGNORECASE)
    replacement2 = re.compile(re.escape("informationen about"), re.IGNORECASE)
    replacement3 = re.compile(re.escape("?"), re.IGNORECASE)
    replacement4 = re.compile(re.escape("please"), re.IGNORECASE)
    replacement5 = re.compile(re.escape("search"), re.IGNORECASE)
    replacement6 = re.compile(re.escape("for"), re.IGNORECASE)

    text = replacement1.sub("", text)
    text = replacement2.sub("", text)
    text = replacement3.sub("", text)
    text = replacement4.sub("", text)
    text = replacement5.sub("", text)
    text = replacement6.sub("", text)

    link = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + text
    try:
        f = requests.get(link)
        response = f.text
        data = json.loads(f.text)
        output = data["query"]["pages"]
        final = output[list(output.keys())[0]]["extract"]
        awnser = final
    except KeyError:
        awnser = "I'm sorry I couldn't find anything about that."
    except Exception:
        awnser = "Wikipedia is currently not available."

    return awnser


client.run("YOUR_TOKEN_HERE") #Replace this