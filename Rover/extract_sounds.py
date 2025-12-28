import base64
import json


mp3s = json.load(open("sounds-mp3.json", encoding="utf-8"))
for i, mp3 in mp3s.items():
    mp3 = mp3.split(",")[-1]
    open(f"{i}.mp3", "wb").write(base64.b64decode(mp3))