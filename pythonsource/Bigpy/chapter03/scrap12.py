import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

books = soup.select('article.product_pod')

for book in books:
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    rating = book.select_one("p.star-rating")["class"][1]  # 두번째 class가 별점(One, Two, Three...)

    print(f"{title} | {price} | 별점: {rating}")