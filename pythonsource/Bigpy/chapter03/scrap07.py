import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse

# 내 공인 IP주소를 알려주는 API
API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

# 딕셔너리
values={
    'ctxCd':'1012'
}

print('before',values)
params = urllib.parse.urlencode(values) # html -> text
print('after',params)

# 요청
url = API + '?' + params
print('요청 url=',url)

# 읽기
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)