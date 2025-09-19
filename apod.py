import requests
from PIL import Image 

API_URL = f'https://api.nasa.gov/planetary/apod?api_key=<YOUR API KEY>'

r = requests.get(API_URL)
data = r.json()

img_url = data["hdurl"]

print(data["title"])
print(data["date"])
print(img_url)
print(data["explanation"])

# fetch and show image
response = requests.get(img_url, stream=True)
img = Image.open(response.raw)
img.show()
