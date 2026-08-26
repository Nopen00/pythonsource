from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
s = Service('C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.set_window_size(1920,1080) # 화면크기
driver.get('https://auth.wishket.com/login')
time.sleep(3)

driver.find_element(By.NAME, 'emailOrId').send_keys('tkwk651@naver.com')
driver.find_element(By.NAME, 'password').send_keys('Nopen4532@')

# 로그인 버튼
login_button_xpath = '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/form/div[3]/button'
driver.find_element(By.XPATH,login_button_xpath).click()
driver.save_screenshot('C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/img/Website.png')
time.sleep(3)
print('로그인 성공')

# 포트폴리오 페이지로 이동
driver.get('https://www.wishket.com/mywishket/partners/')
time.sleep(3)

registered_projects=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[6]/div[1]/p').text
contracted_projects = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[6]/div[2]/p').text
completed_amount = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[6]/div[3]/p').text

print(f'등록된 프로젝트: {registered_projects}')
print(f'계약된 프로젝트: {contracted_projects}')
print(f'누적 완료 금액: {completed_amount}')