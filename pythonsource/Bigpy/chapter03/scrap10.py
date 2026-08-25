import urllib.request
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
}

# 1. Request 객체 생성 및 웹 페이지 요청
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html_doc = response.read().decode("utf-8")

# 2. BeautifulSoup 객체 파싱
soup = BeautifulSoup(html_doc, "html.parser")

# 3. id="tb_list" 테이블 안의 곡 목록 전체 가져오기
songs = soup.select("#tb_list tr")

count = 0
for song in songs:
    rank = song.select_one(".rank")
    title = song.select_one(".ellipsis.rank01 a")   # 곡 제목
    artist = song.select_one(".ellipsis.rank02 a")  # 가수

    if rank and title and artist:
        print(f"{rank.text.strip()}위 | {title.text.strip()} - {artist.text.strip()}")
        count += 1

    if count >= 10:
        break