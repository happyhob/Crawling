from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EA%B5%AD+%EA%B7%BC%EC%9B%90+%EC%86%8C%EB%B9%84%EC%9E%90%EB%AC%BC%EA%B0%80%EC%A7%80%EC%88%98%28CPI%29+%EC%A0%84%EB%85%84%EB%8C%80%EB%B9%84&oquery=%EB%AF%B8%EA%B5%AD+%EA%B7%BC%EC%9B%90+%EC%86%8C%EB%B9%84%EC%9E%90%EB%AC%BC%EA%B0%80%EC%A7%80%EC%88%98%28CPI%29+%EC%A0%84%EB%85%84%EB%8C%80%EB%B9%84&tqi=hrmwcdprvTossRxmw8CssssstlN-392985/")  # 크롤링하고자하는 사이트
soup = BeautifulSoup(response, "html.parser")  # html에 대하여 접근할 수 있도록

value = soup.find("strong", {"class": "num"})
print(value)

value2 = value.text.strip()
print(value2[0:4])