import urllib.request as rq
import ssl
from bs4 import BeautifulSoup
import pprint

page = 1
flag = True
fw = open('NaverEscape.txt', 'w', encoding='utf-8')

while flag:
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=48246&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=' + str(page)
    res = rq.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    comments = soup.select( "body div div.score_result > ul > li")

    for comment in comments:
        reply = comment.select_one("div.score_reple > p").text.strip()
        fw.write(reply + "\n")

    page = page + 1
    next = soup.find('a', { 'class' : "pg_next"})
    if next:
        continue
    else:
        flag = False

fw.close()