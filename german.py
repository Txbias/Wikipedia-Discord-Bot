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

    replacement1 = re.compile(re.escape("wer ist"), re.IGNORECASE)
    replacement2 = re.compile(re.escape("informationen über"), re.IGNORECASE)
    replacement3 = re.compile(re.escape("?"), re.IGNORECASE)
    replacement4 = re.compile(re.escape("bitte"), re.IGNORECASE)
    replacement5 = re.compile(re.escape("suche"), re.IGNORECASE)
    replacement6 = re.compile(re.escape("such"), re.IGNORECASE)

    text = replacement1.sub("", text)
    text = replacement2.sub("", text)
    text = replacement3.sub("", text)
    text = replacement4.sub("", text)
    text = replacement5.sub("", text)
    text = replacement6.sub("", text)

    link = "https://de.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + text
    try:
        f = requests.get(link)
        response = f.text
        data = json.loads(f.text)
        output = data["query"]["pages"]
        final = output[list(output.keys())[0]]["extract"]
        awnser = final
    except KeyError:
        awnser = "Ich konnte dazu leider nichts finden."
    except Exception:
        awnser = "Wikipedia ist momentan nicht ereichbar."

    return awnser

token = open("token.txt")
client.run(token.read()) 