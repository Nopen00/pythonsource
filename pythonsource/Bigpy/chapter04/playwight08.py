from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 기본값이 headless=True이므로 창이 보이게 하려면 headless=False로 설정
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page(viewport={"width": 1920, "height": 1080})  # 화면크기

    page.goto('https://google.com')
    page.wait_for_timeout(3000)  # 대기 (밀리초 단위, 3초)
    page.screenshot(path="C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/img/Web3.png")

    page.goto('https://daum.net')
    page.wait_for_timeout(3000)
    page.screenshot(path="C:/Users/Nopen/Desktop/LLTTYY/soldesk/source/pythonsource/Bigpy/Py_Scrap/img/Web4.png")

    browser.close()

print('스크린샷 성공')