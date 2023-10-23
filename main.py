from webserver import keep_alive
import requests

channelID = 1153308369671696434
headers = {
    "authorization":
    "Nzg1OTA0NzIyNDM5MDQ1MTUw.GiRQ9d.D3l2aL9KWnvYlFZZ4FoHtvsFG_fwJ4X9Fsbsrk"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
