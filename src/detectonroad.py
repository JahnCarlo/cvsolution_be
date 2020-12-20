import requests

image_data = open("./resources/images/road_1.png", "rb").read()

response = requests.post("http://localhost:80/v1/vision/scene",
files={"image":image_data}).json()
print(response)
