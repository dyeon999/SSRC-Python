from flask import Flask, render_template, request, send_file
import feedparser
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import datetime as dt

app = Flask(__name__)

def clean_html(html):
    return BeautifulSoup(html or "", "html.parser").get_text("", strip = True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rss", methods=['GET', 'POST'])
def rss():
    rss_url = request.form['rss_url']
    feed = feedparser.parse(rss_url)

    summaries = []
    for i,entry in enumerate(feed.entries[:5],1):
        title = entry.get("title")
        desc = entry.get("description","")
        summaries.append(f"[{i}] {title}.{desc}")
    
    news_text = "오늘의 뉴스 요약입니다. " + " ".join(summaries)

    today = dt.datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"news_{today}.mp3"
    tts = gTTS(text=news_text, lang="ko")
    tts.save(filename)

    return render_template('rss.html', feed=feed)

@app.route("/download/<path:filename>")
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)