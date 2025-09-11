import requests
from bs4 import BeautifulSoup

keyword = input("Enter Keyword: ")
url = f"https://kin.naver.com/search/list.naver?query={keyword}"

header_info = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

r = requests.get(url, headers=header_info)

soup = BeautifulSoup(r.text, 'html.parser')


titles = soup.select("#s_content > div.section > ul > li > dl > dt > a")

for title in titles:
    print(f"Question: {title.text}")