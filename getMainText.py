#해당 뉴스 본문 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen('https://news.naver.com/newspaper/home')
html = urlopen('https://n.news.naver.com/mnews/article/008/0005047197')
bs =BeautifulSoup(html.read(),'html.parser')

# divs =bs.find_all('div', {"class":"offc_content_txt"})
divs =bs.find_all('div', {"class":"newsct_article _article_body"})





for div in divs:
    title = div.get_text()
    # link = div.parent['href']  # 부모 요소의 href 속성을 가져옵니다.
    # url = div['href']               #해당 부분의 URL 가져오기

    print(f"Title: {title}")   
    # print(f"Url:{url}")         
    # print(f"Link: {link}\n")
