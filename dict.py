import requests
import json
# result = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")

# obj =  json.loads(result.content)
# for i in obj:
#     for key,value in i.items():
#         print(f'{key} : {value}')

# url = "https://image.shutterstock.com/image-vector/dotted-spiral-vortex-royaltyfree-images-600w-2227567913.jpg"
# img = requests.get(url)
# with open("image.jpg", "wb") as image:
#     image.write(img.content) 

# https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a
url = "https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a"

images = requests.get(url).json()
images = images['hits']
counter = 1
for img in images:
    pict = requests.get(img["webformatURL"])
    with open(f'img/{counter}.jpg','wb') as file:
        file.write(pict.content)
    counter += 1


