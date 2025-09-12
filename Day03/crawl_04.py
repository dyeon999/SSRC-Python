import requests
from bs4 import BeautifulSoup

url = 'https://www.malware-traffic-analysis.net/2023/index.html'
header_info = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

r = requests.get(url, headers=header_info) # What is verify=true/false ?
soup = BeautifulSoup(r.text, 'html.parser')

tags = soup.select('#main_content > div.content > ul > li > a.main_menu')

results = []
for tag in tags:
    link_txt = tag.text
    link_href = f"https://www.malware-traffic-analysis.net/2023/{tag.get('href')}"
    results.append(f"{link_txt} \n{link_href} \n")

with open('Day03/malwares.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result)
