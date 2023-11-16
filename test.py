import requests 
from PIL import Image
from io import BytesIO
#i want to display the image
img =requests.get("http://127.0.0.1:5500/a8554548-83f7-4e0e-9beb-226c453e6f98")
print(img.content)

