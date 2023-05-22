import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# get the json
response = requests.get(api_url)
# print(response)
# content = response.content
# print(type(content))      # data-type: <class 'bytes'>
# print(content)

content = response.content.decode('UTF-8')
# print(type(content))      # data-type: <class 'str'>
# print(content)

# convert string to json
dict_content = json.loads(content)
# print(type(dict_content))   # data-type: <class 'dict'>
# print(dict_content)

# get the image url
image_url = dict_content['url']
# print(image_url)

# download the image
response = requests.get(image_url)
# print(response) 

# save the image
with open('apod.png', 'wb') as image:
    image.write(response.content)

# set as wallpaper
PyWallpaper.change_wallpaper('E:\Phitron\Python\apod.png')

