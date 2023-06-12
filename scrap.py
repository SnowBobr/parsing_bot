import random
import requests
from bs4 import BeautifulSoup
from time import sleep
"""импортируем модуль паузы из модуля работы со временем"""


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
"""заменяем реальный заголовок GET запроса на заголовок Хрома, что бы сайт не распознавал бота"""

page_url = "https://scrapingclub.com/exercise/list_basic/"

def find_max_number_of_page(url):
    res = requests.get(url, headers=headers)
    page_soup = BeautifulSoup(res.text, "lxml")
    page = 1
    page_data = page_soup.find_all("a", class_="page-link")
    for i in page_data:
        # sleep(random.randint(3, 7)) #  таким способом в начале каждого цикла ставим паузу на 3 - 7 секунды, что бы сайт не индетефицировал бота
        if i.text.isdigit():
            if int(i.text) > page:
                page = int(i.text)
    return page + 1


def get_urls():
    for count in range(1, find_max_number_of_page(page_url)):
        # так как на сайте 7 страниц делаем цикл по поиску на всех страницах
        # sleep(random.randint(3, 7))
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")  #  lxml, html.parser - парсеры страниц, для удобного представления данных

        # data = soup.find("div", class_="col-lg-4 col-md-6 mb-4") 
        # для одного элемента
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4") 
        # для всех элементов
        # див - теги(обьекты) внутри которых будет поиск
        # через запятую параметры искомых обьектов
        # так выводиться только первый обьект
        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url
            #  это вместо обычного возврата, превращаем в генератор
            #  он будет выдавать по 1 элементу в дальнейшем выполнении функции


def array():
    for card in get_urls():
        xls_list = []
        response = requests.get(card, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="card-body")

        name = data.find("h3", class_="card-title").text.replace("\n", "")
            # когда добрались до самого содержимого  в виде текста, применяем атрибут текст и если необходимо
            # убираем лишнее - в данном случае переносы строки
        description = data.find("p", class_="card-text").text
        price = data.find("h4").text
            # # по аналогии достали цену
        img_url = "https://scrapingclub.com" + soup.find("img", class_="card-img-top img-fluid").get("src")
            # # вытягиваем ссылку, тег имг, класс, а дальше ссылка не строка, по этому методом гет, по атрибуту срц ну и приклеиваем корневой адрес
        yield name, description, price, img_url
              



    