import json

import requests
from bs4 import BeautifulSoup


# URL = "https://upl.uz/"
# page = 'policy'
# HEADERS = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/100.0.4896.127 Safari/537.36",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
# }
#
# response = requests.get(URL + page, headers=HEADERS)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# container = soup.find("div", id='dle-content')
# articles = container.find_all('div', class_='short-story')
#
# print(articles)
# data = []
# i = 1
# for item in articles:
#     title = item.find('h2', class_='sh-tit').get_text(strip=True)
#     description = item.find('div', class_='sh-pan').get_text(strip=True).split('...')[0] + "..."
#     link = item.find('a')['href']
#     photo = 'https://upl.uz' + item.find('img', class_='lazy-loaded')['data-src']
#     data.append({
#         "news": f"News {i}",
#         "title": title,
#         "link": link,
#         "image": photo,
#         "description": description
#     })


class UplParser:
    def __init__(self, page, format_file='json'):
        self.URL = "https://upl.uz/"
        self.HEADERS = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/100.0.4896.127 Safari/537.36",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        self.page = page
        self.format = format_file

    def get_soup(self):
        response = requests.get(self.URL + self.page, headers=self.HEADERS)

        try:
            response.raise_for_status()
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except requests.HTTPError:
            print("Sahifa mavjud emas!!!")

    def get_info(self):
        soup = self.get_soup()
        container = soup.find("div", id='dle-content')
        articles = container.find_all('div', class_='short-story')

        data = []
        for item in articles:
            title = item.find('h2', class_='sh-tit').get_text(strip=True)
            description = item.find('div', class_='sh-pan').get_text(strip=True).split('...')[0] + "..."
            link = item.find('a')['href']
            photo = 'https://upl.uz' + item.find('img', class_='lazy-loaded')['data-src']
            data.append({
                "title": title,
                "link": link,
                "image": photo,
                "description": description
            })
        return data

    def write_document(self):
        info = self.get_info()
        text = ''
        if self.format.lower() == "json":
            with open(f'{self.page}.json', mode='w', encoding='utf-8') as json_file:
                json.dump(info, json_file, indent=4, ensure_ascii=False)
        elif self.format.lower() == "txt":
            for item in info:
                for key, value in item.items():
                    text += f"{key}: {value}\n"
                text += '\n'
            with open(f'{self.page}.txt', mode='w', encoding='utf-8') as txt:
                txt.write(text)

        else:
            print("Siz kiritgan format text uchun emas !!!")


UplParser('president', 'txt').write_document()
UplParser('economy').write_document()
UplParser('economy', 'txt').write_document()
