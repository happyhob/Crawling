from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://news.naver.com/section/101')
bs =BeautifulSoup(html.read(),'html.parser')

div =bs.find_all('strong')
# div =bs.find_all('meta', class_='sh_text_headline')

for d in div:
    print(d.get_text()+"\n")
