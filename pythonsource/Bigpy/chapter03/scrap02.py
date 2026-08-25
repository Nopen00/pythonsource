import sys
import os
from bs4 import BeautifulSoup

'''
<html>
<body>
<ul id="cars">
  <li id="ge">Genesis</li>
  <li id="av">Avante</li>
  <li id="so">Sonata</li>
  <li id="gr">Grandeur</li>
  <li id="tu">Tucson</li>
</ul>
</body>
</html>
'''

fp = open('C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/cars.html', encoding='utf-8')

soup = BeautifulSoup(fp,'html.parser')
# print(soup)

# 함수
def car_func(select):
    print('car_func : ', soup.select_one(select).string)

# 메인
car_func('#gr') # 가장 단순
car_func('li#gr') # li이면서 아이디가 gr
car_func('ul>#gr') # ul의 직계 자식중 id가 gr
car_func('#cars #gr') # 아이디가 #car이면서 그 아래 어딘가에 있는 아이디가 gr
car_func('#cars>#gr') # 아이디가 #car의 직계자식중 id가 gr
# car_func("li*[id='gr']") 뭔가 안되는중

# 람다식(매개변수:q)
car_lambda = lambda q: print('car_func: ', soup.select_one(q).string)

# 메인
car_lambda('#gr') 
car_lambda('li#gr')
car_lambda('ul>#gr')    #아래 구문과 같으쓰면 좋음
car_lambda('#cars #gr') #단 좀 과감한 방식이라 오류 생각해야함
car_lambda('#cars>#gr') 
# car_lambda("li*[id='gr']") 뭔가 안되는중

print("--------------------------------------------------")
print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)