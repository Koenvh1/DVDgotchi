import json
import os

import PIL.Image
from PIL import ImageDraw, ImageFont

animations = json.load(open("agent.json", encoding="utf-8"))["animations"]


def create_bar(bg, food_level, happiness_level):
    draw = ImageDraw.Draw(bg)

    img_w, img_h = bg.size

    bar_width = 300
    bar_height = 20
    segment_count = 3
    segment_gap = 4

    total_gap = segment_gap * (segment_count - 1)
    segment_width = (bar_width - total_gap) // segment_count

    center_x = img_w // 2
    start_x = center_x - bar_width // 2

    happiness_y = img_h - 50
    food_y = happiness_y - 50

    outline_color = "white"
    fill_color = "green"
    text_color = "white"

    font = ImageFont.truetype("arial.ttf", 16)

    def draw_bar(y, label, fill_level):
        draw.text((start_x, y - 22), label, fill=text_color, font=font)

        x = start_x
        for i in range(segment_count):
            draw.rectangle(
                [x, y, x + segment_width, y + bar_height],
                outline=outline_color,
                fill=fill_color if fill_level > i else None
            )
            x += segment_width + segment_gap

    draw_bar(food_y, "Food", food_level)
    draw_bar(happiness_y, "Happiness", happiness_level)

pre_vids = [
    "Acknowledge",
    "Shopping",
    "Writing",
    "Searching",
    "Embarrassed",
    "GestureLeft",
    "Greet",
    "LookUp",
    "Show",
    "GetAttentionMinor",
    "Congratulate",
    "ClickedOn",
]

post_vids = [
    "Travel",
    "Hide",
    "ImageSearching",
    "HideQuick",
    "Pleased",
    "CharacterSucceeds",
    "Surprised",
    "Thinking",
    "LookUpLeft",
    "RestPose",
    "GetAttention",
    "Idle",
]

pre_vid_idx = 0
post_vid_idx = 0

for food_level in range(1, 4):
    for happiness_level in range(1, 4):
        for key in ["Books", "Celebrity", "Cooking", "Searching", "Sports"]:
            value = animations[key]
            print(food_level, happiness_level, key)
            base_folder = f"animations\\{food_level}\\{happiness_level}\\{key}"
            os.makedirs(f"{base_folder}", exist_ok=True)

            sounds = []
            print(pre_vids[pre_vid_idx])
            frames = []
            frames.extend(animations[pre_vids[pre_vid_idx]]["frames"])
            frames.extend(value["frames"])
            frames.extend(animations[post_vids[post_vid_idx]]["frames"])

            for i, frame in enumerate(frames):
                if "sound" in frame:
                    sounds.append((i * 100, frame["sound"]))

                img = PIL.Image.open("map.png").convert("RGBA")
                coords = frame["images"][0]
                img = img.crop((coords[0], coords[1], coords[0] + 80, coords[1] + 80))

                bg = PIL.Image.new("RGB", (720, 540), (0, 0, 0))
                bg.paste(img, (720 // 2 - 80 // 2, 540 // 2 - 80 // 2), mask=img)

                create_bar(bg, food_level, happiness_level)

                bg.save(f"{base_folder}/{i}.png")

            try:
                os.remove(f"{base_folder}\\out.mpg")
            except:
                pass
            os.system(f"ffmpeg -framerate 10 -i \"{base_folder}\\%d.png\" -target pal-dvd {base_folder}\\out.mpg")
            pre_vid_idx += 1
            pre_vid_idx %= len(pre_vids)
            post_vid_idx += 1
            post_vid_idx %= len(post_vids)
            for sound in sounds:
                continue
                cmd = (
                    f'ffmpeg -y '
                    f'-i {base_folder}\\out.mpg '
                    f'-i sounds\\{sound[1]}.mp3 '
                    f'-filter_complex '
                    f'"[1:a]adelay={sound[0]}|{sound[0]}[a]" '
                    f'-map 0:v '
                    f'-map "[a]" '
                    f'-c:v copy '
                    f'-shortest '
                    f'-c:v copy out2.mpg'
                )
                print(cmd)
                os.system(cmd)
                os.remove(f"{base_folder}\\out.mpg")
                os.rename("out2.mpg", f"{base_folder}\\out.mpg")
                print(sound)