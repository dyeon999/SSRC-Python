import requests
from bs4 import BeautifulSoup

url = "https://zdnet.co.kr"

header_info = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

r = requests.get(url, headers=header_info)

soup = BeautifulSoup(r.text, 'html.parser')
links = soup.select('body > div.contentWrapper > div > div.left_cont > div.news1_box > div.news_list > div > div.assetText > a > h4')

# print(soup)
for link in links:
    print(link.string)