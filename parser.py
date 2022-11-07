from bs4 import BeautifulSoup
import requests

def parser():
    url = 'https://yandex.ru/images/search?text=tiger&from=tabbar'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    img = soup.find_all('img', class_ = 'serp-item__thumb justifier__thumb')

if __name__ == "__main__":
    parser()