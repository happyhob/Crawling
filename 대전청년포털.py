# import requests
# from bs4 import BeautifulSoup

# # Function to fetch HTML content and parse links
# def fetch_and_parse_links(url):
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         links = soup.find_all('a', href=True)
#         link_urls = [link['href'] for link in links]
#         return link_urls
#     else:
#         return []

# # Example usage
# url = 'https://www.daejeonyouthportal.kr/'  # Replace with the actual URL
# links = fetch_and_parse_links(url)
# for link in links:
#     print(link)



#https://www.daejeonyouthportal.kr/
#대전 청년 포털의 청년정책 url 가져오기

import requests
from bs4 import BeautifulSoup

# 크롤링할 웹 페이지의 URL
url = 'https://www.daejeonyouthportal.kr/'  # 실제 웹 페이지 URL로 변경

# 웹 페이지의 HTML을 가져옵니다.
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(html, 'html.parser')

# "청년지원" 메뉴를 찾아서 그 아래의 모든 링크를 추출합니다.
youth_support_section = soup.find('a', href='#gnb_m002')
if youth_support_section:
    youth_support_links = youth_support_section.find_next('ul', class_='depth2').find_all('a')
    for link in youth_support_links:
        print(link['href'])
else:
    print("청년지원 메뉴를 찾을 수 없습니다.")

