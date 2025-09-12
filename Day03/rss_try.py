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

data = {"제목": titles, "링크": links, "요약": descriptions, "작성자": authors, "날짜": publishes}

df = pd.DataFrame(data)

df.to_excel('Day03/DailySecu.xlsx', index=False)
print("COMPLETELY CREATED THE FILE")