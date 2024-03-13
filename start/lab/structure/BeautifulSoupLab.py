import requests
from bs4 import BeautifulSoup

response = requests.get("https://aday7.tistory.com/entry/IntelliJ-IDEA%EC%97%90%EC%84%9C-Python-%EC%84%A4%EC%B9%98%EC%99%80-%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%B2%AB-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EA%B9%8C%EC%A7%80");

soup = BeautifulSoup(response.text, 'html.parser');

headlines = soup.select('.inner h1');

for headline in headlines:
    print(headline.text.strip());