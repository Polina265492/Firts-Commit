#1) Записати до файлу:
#- Назву товару
#- Кількість відгуків
#- Ціну

import requests
from bs4 import BeautifulSoup
import lxml

url = "https://allo.ua/ua/products/mobile/poco-x5-pro-5g-8-256-black.html"
user = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
headers = {"User-agent": user}


if responce_code == 200:
    soup = BeautifulSoup(responce.text, features:"lxml")
    elements =soup.find(name: "div", class_="snap-slider with-pagination")
    for i in all_products:
        try:
            if i.find('div', class = '<span class="sum">13&nbsp;499<span class="currency"> ₴ </span></span>')
            print(price.text)
        expect Exception:

          print('Нету скидки')

name:"POCO X5 Pro 5G 8/256 Black"
#Не знаю как написать про скидку



#=#2) Спарсити тільки ті товари, які мають знижку
# Записати до файлу:
#- Назву товару
#- Кількість відгуків
#- Ціну

import requests
from bs4 import BeautifulSoup
import lxml


url = "https://allo.ua/ua/televizory/"
user = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
headers = {"User-agent": user}


#дальше не знаю что писать что бы код нашел товары со скидками
