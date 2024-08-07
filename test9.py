'''
단어 의미 찾기 함수
'''

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

WEB_URL = "https://en.dict.naver.com/"

def findWordMean(word):
    # ChromeDriver 설정
    service = ChromeService(executable_path=ChromeDriverManager().install())
    # WebDriver 초기화
    driver = webdriver.Chrome(service=service)
    try:
        # 웹 페이지 열기
        driver.get(WEB_URL)
        # input 요소 찾기
        search_box = driver.find_element(By.ID, 'ac_input')
        # 검색어 입력
        search_box.send_keys(word)
        # 검색 실행 (Enter 키 누르기)
        search_box.send_keys(Keys.RETURN)
        
        # 페이지가 로드될 때까지 기다림 (충분한 시간을 주세요)
        time.sleep(3)
        
        # BeautifulSoup을 사용하여 페이지 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the <a> tag for the first search result link
        a_tag = soup.find('a', class_='link')

        if a_tag:
            # Extract the href attribute
            href_value = a_tag.get('href')

            # Construct the new URL
            new_url = WEB_URL + href_value

            # Navigate to the new URL
            driver.get(new_url)

            # 페이지가 로드될 때까지 기다림 (충분한 시간을 주세요)
            time.sleep(3)

            # 다시 BeautifulSoup을 사용하여 새 페이지 파싱
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # 관련 단어 목록 가져오기
            entries = soup.find_all('div', class_='entry_mean_item', lang='ko')

            # 각 요소에서 meaning 클래스 안의 내용 추출하여 출력
            for entry in entries:
                meaning = entry.find('p', class_='meaning').text.strip()
                print(meaning)
        else:
            print("No search results found.")

    finally:
        # 브라우저 닫기
        driver.quit()

# 함수 호출하여 실행
findWordMean('relation')
