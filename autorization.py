from requests import Session  #  для сохранения кукки в сайтах где нужно логинится
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
page_url = "https://quotes.toscrape.com"

work = Session()
work.get(page_url, headers=headers)
#  имитация входа на сайт
work.get(page_url + "/login", headers=headers)
#  переходим на страницу логирования


print()