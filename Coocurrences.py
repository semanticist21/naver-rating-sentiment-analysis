import sys
f= open('coocurrences.txt','w', encoding='utf-8')
stdout=sys.stdout # 저장
sys.stdout=f

from pprint import pprint

count = {}
for line in open('MetacriticNouns.txt', 'r', encoding='utf-8'):
    words = list(set(line.split())) #한줄씩 읽은뒤 단어별로 분리 #set 넣어중복제거후 list로
    for i, a in enumerate(words):
        for b in words[i+1:]:
            if a == b: continue #같은단어제외시키기
            if a > b: a, b = b, a #A, B B,A가 다르게 세어지는 것 맞음
            count[a, b] = count.get((a, b), 0) +1 #세는 작업
import operator
sdict = sorted(count.items(), key=lambda t : t[1]) ##정렬하기
pprint(sdict)

count1 = {}
for line in open('NaverReviewsNouns.txt', 'r', encoding='utf-8'):
    words = list(set(line.split())) #한줄씩 읽은뒤 단어별로 분리 #set 넣어중복제거후 list로
    for i, a in enumerate(words):
        for b in words[i+1:]:
            if a == b: continue #같은단어제외시키기
            if a > b: a, b = b, a #A, B B,A가 다르게 세어지는 것 맞음
            count1[a, b] = count1.get((a, b), 0) +1 #세는 작업
sdict1 = sorted(count1.items(), key=lambda t : t[1])
pprint(sdict1)


f.close()
sys.stdout = stdout
