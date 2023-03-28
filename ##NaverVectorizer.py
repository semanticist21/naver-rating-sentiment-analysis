from sklearn.feature_extraction.text import CountVectorizer
import nltk
from pprint import pprint

f = open('MetacriticNouns.txt', 'r', encoding= 'utf-8')
f1 = open('NaverReviewsNouns.txt', 'r', encoding='utf-8')


text = f.read()
f.close()
corpus = [text]
vect = CountVectorizer()
vect.fit(corpus)
print(vect.vocabulary_)

text1 = f1.read()
f1.close()
corpus1=[text1]
vect.fit(corpus1)
print(vect.vocabulary_)





