# RSS 서비스 사용해서 엑셀 저장하기 (RSS맛보기)
import feedparser
import pandas as pd

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)
# print(feed) #페이지 긁어오기

titles = []
links = []
descriptions = []
authors = []
publishes = []

# for entry in feed.entries:
#     print(entry)
#     print() 

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    publishes.append(entry.published)

print(titles)