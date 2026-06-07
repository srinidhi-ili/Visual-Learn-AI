from video_generator import create_video, merge_videos

import requests
from urllib.parse import quote
from text_to_speech import text_to_speech

from video_generator import create_video
print("SCENE_GENERATOR LOADED")

PEXELS_API_KEY = "your_actual_key"


def get_image(keyword):

    url = f"https://api.pexels.com/v1/search?query={quote(keyword)}&per_page=1"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    print("KEYWORD:", keyword)
    print("RESULT:", data)

    if data.get("photos"):
        return data["photos"][0]["src"]["medium"]

    return "https://picsum.photos/600/400"


def generate_scenes(text):
    import glob
    import os

    for file in glob.glob("scene_*.jpg"):
        os.remove(file)

    for file in glob.glob("scene_*.mp4"):

        os.remove(file)

    for file in glob.glob("audio/scene_*.mp3"):

        os.remove(file)

    slides = [
        slide.strip()
        for slide in text.split("===SLIDE===")
        if slide.strip()
    ]
    print("TOTAL SLIDES FOUND:", len(slides))

    scenes = []
    video_files = []

    for i, slide in enumerate(slides):
        

        lines = [
            line.strip()
            for line in slide.split("\n")
            if line.strip()
        ]

        if not lines:
            continue

        title = lines[0]

        subtitle = " ".join(lines[1:])

        print("SCENE:", i + 1)
        print("TITLE:", title)
        print("SUBTITLE:", subtitle)
        print("----------------")

        keyword = (title + " " + subtitle)[:100]
        print("SEARCH KEYWORD:", keyword)

        voice_text = subtitle if subtitle.strip() else title

        audio_file = text_to_speech(
            voice_text,
            f"scene_{i+1}.mp3"
            
        )
        video_file = f"scene_{i+1}.mp4"
        print("Video File:", video_file)
        image_url = get_image(keyword)

        print("IMAGE URL:", image_url)
        print("Audio File:", audio_file)
        print("CREATING VIDEO...")
        
        print("Current Image URL:", image_url)
        image_file = f"scene_{i+1}.jpg"

        response = requests.get(image_url)

        with open(image_file, "wb") as f:
            f.write(response.content)

            create_video(
    image_file,
    audio_file,
    video_file,
    voice_text
)



        scene = {
            "scene": i + 1,
            "title": title,
            "subtitle": subtitle,
            "voice_text": voice_text,
            "audio_file": audio_file,
            "image_prompt": f"Educational illustration of {title}",
            "keyword": keyword,
            "image_url": image_url
           
            
        }

        scenes.append(scene)
        video_files.append(video_file)

    if len(video_files) > 0:


        merge_videos(
        video_files,
        "final_video.mp4"
    )

    return scenes