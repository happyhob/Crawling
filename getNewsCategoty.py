#뉴스 카테고리와 해당 카테고리에 관한 url 얻어오기

from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen('https://news.naver.com/newspaper/home')
html = urlopen('https://news.naver.com/')
bs =BeautifulSoup(html.read(),'html.parser')

# divs =bs.find_all('div', {"class":"offc_content_txt"})
divs =bs.find_all('span', {"class":"Nitem_link_menu"})
divs2 =bs.find_all('a', {"class":"Nitem_link"})




for div in divs2:
    title = div.get_text()
    # link = div.parent['href']  # 부모 요소의 href 속성을 가져옵니다.
    url = div['href']               #해당 부분의 URL 가져오기

    print(f"Title: {title}")   
    print(f"Url:{url}")         
    # print(f"Link: {link}\n")
