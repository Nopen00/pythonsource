from bs4 import BeautifulSoup
import urllib.request as req
import requests

# 주식 요청 url
url="http://finance.naver.com/sise/"

# 요청
print(requests.get(url).encoding) # euc-kr
res=req.urlopen(url).read().decode('euc-kr')
# print('res',res)

soup = BeautifulSoup(res, 'html.parser')

items = soup.select('#siselist_tab_0 a.tltle')

print("--- 네이버 증권 상한가 Top 리스트 ---")
for idx, item in enumerate(items, 1):
    title = item.text.strip()
    print(f"{idx}위 : {title}")