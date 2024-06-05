#해당 카테고리 주소로 들어가서 헤드라인 정보 및 url 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup

import webbrowser


html = urlopen('https://news.naver.com/section/10')
bs =BeautifulSoup(html.read(),'html.parser')


divs =bs.find_all('a', {"class":"sa_text_title"})

dict_URL = {}
dict_TITLE = {}

count = 1
for div in divs:

    title = div.get_text()
    # link = div.parent['href']  # 부모 요소의 href 속성을 가져옵니다.
    url = div['href']               #해당 부분의 URL 가져오기

    print(f"Title: {title}")   
    print(f"Url:{url}")         
    dict_URL[f"title{count}"] = url
    dict_TITLE[f"title{count}"] = title
    count = count+1
    # print(f"Link: {link}\n")



print(f"dict:{dict_URL}")



# 헤딩 url 주소 열기
webbrowser.open(dict_URL["title1"])