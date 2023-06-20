from requests import Session
import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/detail_ajax/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
"""заменяем реальный заголовок GET запроса на заголовок Хрома, что бы сайт не распознавал бота"""

work = Session()
work.get(url, headers=headers)
resp = work.get(url, headers=headers)

#  Заходим в сеть, переходим на закладку Fetch/XHR и смотри есть ли перенаправление на другую страницу
work_url = "https://scrapingclub.com/exercise/ajaxdetail/"
response = requests.get(work_url).json()
#   если в ответе идет json с обычным словарем, таким образом можно его забрать и использовать
#   есл содержит булевые значения - нужно импортировать библиотеку json и коныертировать

     

print(response)