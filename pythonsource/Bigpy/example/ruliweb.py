import requests
from bs4 import BeautifulSoup

with requests.Session() as s:
    #게시글 가져오기
    post_one = s.get('https://bbs.ruliweb.com/market/board/1020/read/106677?')

    post_one.raise_for_status
    print(post_one)
    print('-'*30)
    print()

    soup = BeautifulSoup(post_one.text,'html.parser')
    # print(soup.prettify)
    print('-'*30)
    # 문서 출력
    article = soup.select_one('div.view_content article')
    if article:
        print(article.get_text(strip=True))

    print('-'*30)

    article = soup.select('div.view_content article p')
    print(article[4].text)
    if len(article) >= 5:
        target_text = article[4].text.strip()
        print("5번째 문장:", target_text)