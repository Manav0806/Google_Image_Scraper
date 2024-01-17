import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os 

link = input("Enter the link:")
image_name = input("enter the name of image:")
path = input("enter the path to save images:")

save_dir = f"{path}"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

query = image_name
response = requests.get(f"{link}")


soup = BeautifulSoup(response.content,'html.parser')

images_tages = soup.find_all("img")

del images_tages[0]


for i in images_tages:
    images_url = i['src']
    image_data = requests.get(images_url).content
    with open(os.path.join(save_dir , f"{query}_{images_tages.index(i)}.jpg"), "wb") as f :
        f.write(image_data)
    