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

