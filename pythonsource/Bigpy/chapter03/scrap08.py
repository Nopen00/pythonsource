import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse


url = "http://www.encar.com/"

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    }
)

mem = urllib.request.urlopen(req)
print(type(mem))
print('geturl : ',mem.geturl())
print('status : ', mem.status)

# 서버가 사용하는 문자 인코딩, 없으면 utf-8
encoding = mem.info().get_content_charset() or 'utf-8'

print('header : ', mem.header())
print('info : ', mem.info())
print('getcode : ', mem.getcode())



# 바이트를 500개만 자르면 멀티바이트(한글, 한자, 특문등) 중간에 끊김
# unicodeDecodeError가 날수 있으므로 errors = 'ignore'처리
raw = mem.read(500)
print('read: ', raw.decode(encoding, errors = 'ignore'))

print(urlparse('http://www.encar.co.kr?test=test').query)
