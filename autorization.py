from requests import Session  #  для сохранения кукки в сайтах где нужно логинится
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
page_url = "https://quotes.toscrape.com"
work = Session()
post_data = {}

def connect():
    global post_data
    work.get(page_url, headers=headers)
    #  имитация входа на сайт
    response = work.get(page_url + "/login", headers=headers)
    #  переходим на страницу логирования
    soup = BeautifulSoup(response.text, "lxml")
    token = soup.find("form").find("input").get("value")
    #  вытягиваем одноразовый токен авторищации
    post_data = {"csrf_token": token, "username": "noname", "password": "password"}
    #  создаем словарь для post запроса
    result = work.post(page_url + "/login", headers=headers, data=post_data, allow_redirects=True)
    #  передаем на страницу логирования словарь с данными: ключь, логин и пароль
    #  и добавляем параметр разрещающий автоматическое перенаправление, так как на сайте это есть (код 302 и переходы страниц)
    print(post_data["csrf_token"])
    return result

def scrap_quotes():
    for count in range(1, 10**10):
        sleep(3)
        page_number = str(count) + "/"
        url = f"https://quotes.toscrape.com/page/{page_number}"
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        quotes = soup.find_all("div", class_="quote")

        if len(quotes) <=1:
            print()
            print("That's all")
            break


        for quote in quotes:
            author = quote.find("small", class_="author").text
            text = quote.find("span", class_="text").text
            tags = quote.find("meta", class_="keywords").get("content").split(",")

            print(author, text, tags, sep="\n")
            print("*" * 40)

        print(count)

connect()
scrap_quotes()
