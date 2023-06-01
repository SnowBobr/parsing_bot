import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")  #  lxml, html.parser - парсеры страниц, для удобного представления данных

data = soup.find("div", class_="col-lg-4 col-md-6 mb-4") 
# для одного элемента
data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4") 
# для всех элементов
# див - теги(обьекты) внутри которых будет поиск
# через запятую параметры искомых обьектов
# так выводиться только первый обьект
for i in data:
    name = i.find("h4", class_="card-title").text.replace("\n", "")
    # когда добрались до самого содержимого  в виде текста, применяем атрибут текст и если необходимо
    # убираем лишнее - в данном случае переносы строки
    price = i.find("h5").text
    # по аналогии достали цену
    product_url = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
    # вытягиваем ссылку, тег имг, класс, а дальше ссылка не строка, по этому методом гет, по атрибуту срц ну и приклеиваем корневой адрес

    print(name, price, product_url, sep="\n", end="\n\n")