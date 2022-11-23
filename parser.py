import os
import time
import shutil
import cv2
import requests
from bs4 import BeautifulSoup

def parser(count_img, typename, index=None):
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

        for img_url in src_list:
            if img_url.find("n=13") != -1:
                src = "https:" + img_url
                img = requests.get(src)

                if index is not None:
                    file_name = str(index[count])
                else:
                    file_name = str(count)

                out = open("D:/test/" + typename + "/" + file_name.zfill(4) + ".jpg", "wb")
                out.write(img.content)
                out.close()

                name_file = str("D:/test/" + typename + "/" + file_name.zfill(4) + ".jpg")
                image = cv2.imread(name_file)
                file_write = str("D:/dataset/" + typename + "/" + file_name.zfill(4) + ".jpg")
                cv2.imwrite(file_write, image)

                time.sleep(1)
                count += 1
                if count == count_img:
                    return page


if __name__ == "__main__":
    c = 1100
    print("Парсинг тигров")
    parser(c, "tiger")

    print("Пауза")
    time.sleep(60)

    print("Парсинг леопардов")
    parser(c, "leopard")

    shutil.rmtree("D:/test/")