import requests

url = "https://images.pexels.com/photos/22763683/pexels-photo-22763683.jpeg?auto=compress&cs=tinysrgb&h=350"

response = requests.get(url)

with open("scene_1.jpg", "wb") as file:
    file.write(response.content)

print("Image downloaded!")