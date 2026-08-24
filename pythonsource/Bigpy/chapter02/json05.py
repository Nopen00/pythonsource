import urllib.request as req
import os.path,random
import simplejson as json 

#URL 요청
url="https://api.github.com/repositories"

#경로와 파일면
savename = 'repo.json'

# 예외 처리
if not os.path.exists(url):
    req.urlretrieve(url, savename)


# 객체를 역직렬화(load)
item = json.load(open(savename,'r',encoding='utf-8'))
print('type : ',type(item))

for i in item:
    print(i['full_name']+' - '+ i['owner']['url'])

print('-'*20)
items = json.load(open(savename,'r',encoding='utf-8'))
print('type : ',type(items))

for it in items:
    print(i['full_name']+' - '+ it['owner']['url'])


    