from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
s = Service('C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/chromedriver/chromedriver.exe')

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.set_window_size(1920,1080) # 화면크기
driver.get('https://google.com')
time.sleep(3)
driver.save_screenshot('C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/img/Website1.png')

driver.set_window_size(1920,1080) # 화면크기
driver.get('https://daum.net')
time.sleep(3)
driver.save_screenshot('C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/img/Website2.png')


driver.quit()
print('스샷 성공~')