from requests import Session
from bs4 import BeautifulSoup
import time, random


started_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
"""заменяем реальный заголовок GET запроса на заголовок Хрома, что бы сайт не распознавал бота"""
"""аякс практически всегда проверят был ли вход на страницу и наличие куки"""


def main(started_url):
    work = Session()
    work.headers.update(headers)
    """второй вариант передавать заголовки обманки"""

    count = 1
    pagination = 1

    while count != pagination + 1:
        if count > 1:
            url = started_url + "?page=" + str(count)
        else:
            url = started_url

        response = work.get(url)
        # with open("data.html", "w", encoding="utf-8") as file:
        #     file.write(response.text)
        """тут была запись страницы на комп"""
        soup = BeautifulSoup(response.text, "lxml")

        if count == 1:
            pagination = int(soup.find("ul", class_="pagination invisible").find_all("li", class_="page-item")[-2].text)
            """если страница первая, ищем пагинацию, получиаем списком все элементы - количество страниц
            далее присваиваем предпоследний элемент, потому что последний - не номер страницы а переход дальше
            """



        cards = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

        for card in cards:
            name = card.find("h4", class_="card-title").text.replace("\n", "")
            print(name)
        
        print(count)
        time.sleep(random.randint(3, 7))
        count +=1


main(started_url)