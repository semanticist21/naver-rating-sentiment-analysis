import requests
import urllib.request as rq
import urllib
import ssl
from bs4 import BeautifulSoup

page = 0
flag = True
fw = open('MetacriticReviews.txt', 'w', encoding='utf-8')
flag = True
while flag:
    url = 'https://www.metacritic.com/movie/avengers-infinity-war/user-reviews?page=' + str(page)
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    comments = soup.select("body > div > div > div div.summary")

    for comment in comments:
        reply = comment.select_one("div.review_body > span").text.strip()
        fw.write(reply + '\n')

    page = page + 1
    if page == 7:
        flag = False
    else: continue

fw.close()
