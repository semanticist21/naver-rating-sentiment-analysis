from konlpy.tag import Okt
from pprint import pprint

fr = open('NaverReviews.txt', 'rt', encoding='utf-8')
##lines = fr.readlines()
text = fr.read()
text = text.replace("관람객","")
lines = text.split('\n')

twitter = Okt()
fw = open('NaverReviewsNouns.txt', 'w', encoding = 'utf-8')



for line in lines:
    sentences_tag = [word for word in twitter.pos(line)]
    noun_adject_verb = [word for word, pos in sentences_tag if pos in ['Noun', 'Adjective','Verb']]
    #noun = twitter.nouns(line) #구형

    #text_processed = [word for word in noun_adject_verb if len(word) >= 2] ##2개 단어 이하 삭제
    fw.write('\t'.join(noun_adject_verb) + '\n')
fw.close()



