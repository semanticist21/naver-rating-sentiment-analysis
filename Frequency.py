import nltk
import urllib
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm
import matplotlib

#font_list = fm.findSystemFonts(fontpaths=None,fontext='ttf')
#print(font_list[:300])
#C:\\WINDOWS\\Fonts\\HANDotumExt.ttf


font_location = 'C:\\WINDOWS\\Fonts\\NGULIM.ttf'
                    # ex - 'C:/asiahead4.ttf'
font_name = fm.FontProperties(fname = font_location).get_name()
matplotlib.rc('font', family = font_name)

f1 = open('MetacriticNouns.txt' , 'rt',encoding='utf-8')
f2 = open('NaverReviewsNouns.txt', 'rt', encoding='utf-8')
text1 = f1.read()
text2 = f2.read()

## \n \t 없애주기
#text1_split = [word for word in text1.split('\t')]
#text2_split = [word for word in text1.split('\t')]
#print(text1_split)
f1.close()
f2.close()
f3 = open('MetacriticNouns.txt' , 'rt',encoding='utf-8')
f4 = open('NaverReviewsNouns.txt', 'rt', encoding='utf-8')
text1_lines = f3.readlines()
text2_lines = f4.readlines()
##for words in text1:
    ##words_splited1 = [words.split('\t')]
    ##metacritic = []
    ##metacritic.extend(words_splited1)

#for words in text2:
    ##words_splited2 =[words.split('\t')]
    ##naver = []
    ##naver.extend(words_splited2)


metacritic = [word for word in text1.split('\t')]
naver = [word for word in text2.split('\t')]

##Frequency
total_word_meta = len(metacritic)
ex_total_word_meta = len(list(set(metacritic)))

import sys
f= open('Frequency.txt','w', encoding='utf-8')
stdout=sys.stdout # 저장
sys.stdout=f

print('댓글 개수:' +'\t')
print(len(text1_lines))

print('단어(중복포함):' +'\t')
print(total_word_meta) # 전체 단어수(중복포함)

print('단어(중복제거):' + '\t')
print(ex_total_word_meta) # 전체 단어수(중복제거)

Freq_dist_nltk=nltk.FreqDist(metacritic)
Freq_dist_nltk.plot(30, cumulative=False)

print(len(naver)) # 전체 단어수(중복포함)
total_word_naver = len(naver)
ex_total_word_naver = len(list(set(naver)))

print('댓글 개수:' +'\t')
print(len(text2_lines))

print('단어(중복포함):' +'\t')
print(total_word_naver) # 전체 단어수(중복포함)

print('단어(중복제거):' + '\t')
print(ex_total_word_naver)# 전체 단어수(중복제거)

Freq_dist_nltk=nltk.FreqDist(naver)
Freq_dist_nltk.plot(30, cumulative=False)

f.close()