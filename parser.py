import os
import time
import shutil
import cv2
import requests
from bs4 import BeautifulSoup

def parser(typename):
    if not os.path.exists("D:/dataset/"):
        os.mkdir("D:/dataset/")
    if not os.path.exists("D:/dataset/" + typename):
        os.mkdir("D:/dataset/" + typename)

    if not os.path.exists("D:/test/"):
        os.mkdir("D:/test/")
    if not os.path.exists("D:/test/" + typename):
        os.mkdir("D:/test/" + typename)

    count = 0

    for page in range(0, 99):
        url = f"https://yandex.ru/images/search?text=" + typename + f"&p={page}"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        src_list = []
        for link in soup.find_all("img", class_="justifier__thumb"):
            src_list.append(link.get("src"))

if __name__ == "__main__":
    parser("tiger")
    parser("leopard")