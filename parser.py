import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com"

def get_quotes_from_web():
    print(f"Парсим сайт {URL}...")
    response = requests.get(URL)

# def get_books_from_web():
#     """
#     Функция должна вернуть список книг.
#     Пример: [{'title': 'A Light in the Attic', 'price': '£51.77'}, ...]
#     """
#     print(f"Парсим сайт {URL}...")
#     response = requests.get(URL)


    if response.status_code !=200:
        print("Ошибка подключения")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")

    quote_cards = soup.find_all("div", class_="quote")

    quotes = []

    for quote in quote_cards:
        text = quote.find("span", class_= "text")
        author = quote.find("small", class_= "author")

        if text and author:
            quotes.append({
                "text": text.text,
                "author": author.text})

    #     price = card.find("p", class_="price_color").text[1:]
    #     books.append({"title": title, "price": price})
    # return books







    # ==========================================
    # ПРАКТИКА №2: Логика парсинга
    # Мы напишем requests.get и soup.find_all
    # ==========================================

    # 1. Получить страницу
    # 2. Создать суп
    # 3. Найти книги (тег article, класс product_pod)

    return []  # Пока возвращаем пустой список
