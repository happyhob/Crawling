from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

import pandas as pd


EXEL_FILE = './test.xlsx'
WEB_URL = "https://en.dict.naver.com/"

#유의어 & 반의어
'''
input 영단어 , output {title:영단어, '유의어' : [word1, word2..], '반의어' : [word1, word1...]}
'''
def findWoedRelationship(word):
    synonyms_1=[]
    synonyms_2=[]
    dicts={}
    dicts['title'] = word
    # ChromeDriver 설정
    service = ChromeService(executable_path=ChromeDriverManager().install())

    # WebDriver 초기화
    driver = webdriver.Chrome(service=service)

    try:
        # 웹 페이지 열기
        driver.get(WEB_URL)  # 여기에 실제 검색 페이지의 URL을 입력하세요.

        # input 요소 찾기
        search_box = driver.find_element(By.ID, 'ac_input')

        # 검색어 입력
        search_query = word  # 검색어를 여기에 입력하세요.
        search_box.send_keys(search_query)

        # 검색 실행 (Enter 키 누르기)
        search_box.send_keys(Keys.RETURN)

        # 검색 결과가 로드될 때까지 대기 (필요에 따라 시간 조정)
        # time.sleep(3)

        # 유의어사전 버튼 클릭
        thesaurus_button = driver.find_element(By.ID, 'redirectThesaurusdict')
        thesaurus_button.click()

        # 새로 열린 페이지로 전환 (예시)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])  # 마지막으로 열린 탭으로 전환

        time.sleep(1)


        # BeautifulSoup을 사용하여 페이지 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # "유의어" 섹션 전체 선택
        synonym_section = soup.find('div', class_='relation_word_group synonym multi')
        
        # 유의어 목록 가져오기
        synonyms = []
        word_areas = synonym_section.find_all('div', class_='word_area')
        for word_area in word_areas:
            word_list = word_area.find_all('li', class_='relation_word_item')
            for item in word_list:
                word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'})
                if word:
                    synonyms.append(word.text.strip())
        

        # print("유의어:")
        for synonym in synonyms:
            synonyms_1.append(synonym)
            # print(synonym)
            

        dicts['유의어'] = synonyms_1

        # "반의어" 섹션 전체 선택
        synonym_section2 = soup.find('div', class_='relation_word_group antonym')


        # 반의어 목록 가져오기
        synonyms2 = []
        word_areas2 = synonym_section2.find_all('div', class_='word_area')
        for word_area in word_areas2:
            word_list = word_area.find_all('li', class_='relation_word_item')
            for item in word_list:
                word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'})
                if word:
                    synonyms2.append(word.text.strip())

        # print("반의어:")
        for synonym in synonyms2:
            synonyms_2.append(synonym)
            # print(synonym)
        dicts['반의어'] = synonyms_2

        
    finally:
        # 브라우저 닫기
        driver.quit()
        #만약 유의어를 못찾았을 경우를 위한 조건문
        if '유의어' in dicts:
            return dicts
        else:
            wordList = test(dicts)
            dicts['유의어'] = wordList
            return dicts

#유의어만 있는 경우 가져오는 함수
'''
input dict , output [word1, word2 ....]
'''
def test(dict):
    wordList = []
    if '유의어' in dict:
        print()
        print(dict['유의어'])
    else:
        # ChromeDriver 설정
        service = ChromeService(executable_path=ChromeDriverManager().install())
        # WebDriver 초기화
        driver = webdriver.Chrome(service=service)
        try:
            # 웹 페이지 열기
            driver.get(WEB_URL)  # 여기에 실제 검색 페이지의 URL을 입력하세요.
            # input 요소 찾기
            search_box = driver.find_element(By.ID, 'ac_input')
            # 검색어 입력
            search_query = dict['title']  # 검색어를 여기에 입력하세요.
            search_box.send_keys(search_query)
            # 검색 실행 (Enter 키 누르기)
            search_box.send_keys(Keys.RETURN)


            # 유의어사전 버튼 클릭
            thesaurus_button = driver.find_element(By.ID, 'redirectThesaurusdict')
            thesaurus_button.click()
            # 새로 열린 페이지로 전환 (예시)
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])  # 마지막으로 열린 탭으로 전환
            time.sleep(1)
            # BeautifulSoup을 사용하여 페이지 파싱
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # 관련 단어 목록 가져오기
            word_items = soup.find_all('li', class_='relation_word_item')
            # 데이터 출력
            for item in word_items:
                word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'}).text
                wordList.append(word)
                print(word)
        finally:
            # 브라우저 닫기
            driver.quit()
            return wordList

#단어의 의미를 가져오기
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


#엑셀에서 단어 불러오기
'''
input 파일 경로 , output 파일에 적힌 단어 리스트
'''
def fileReadData(filePath):
    # 엑셀 파일 불러오기
    df = pd.read_excel(filePath, sheet_name='Sheet1')  # 시트명에 맞게 변경

    # 0열 데이터를 리스트로 저장
    wordList = df.iloc[:,0].tolist()

    # 결과 출력
    print("0열의 데이터 리스트:", wordList)
    return wordList

# findWordMean('rude')

# wordList = fileReadData(EXEL_FILE)
# print(wordList)

dict = findWoedRelationship('insignificant')
print(dict)