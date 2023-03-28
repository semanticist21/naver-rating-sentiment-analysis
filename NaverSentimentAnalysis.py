
def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # txt 파일의 헤더(id document label)는 제외하기
        data = data[1:]
    return data

train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')

from konlpy.tag import Okt

okt = Okt()

import json
import os
from pprint import pprint

def tokenize(doc):
    # norm 정규화  stem 근어표시
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
    with open('train_docs.json', encoding='utf-8') as f:
        train_docs = json.load(f)
    with open('test_docs.json', encoding='utf-8') as f:
        test_docs = json.load(f)
else:
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
    # JSON 파일 저장
    with open('train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

##pprint(train_docs[0])
tokens = [t for d in train_docs for t in d[0]]
#print(len(tokens)) #토큰개수 확인용

import nltk

text = nltk.Text(tokens, name='NMSC')

# 전체 토큰의 개수
#print(len(text.tokens))

# 중복을 제외한 토큰의 개수
#print(len(set(text.tokens)))

# 출현 빈도가 높은 상위 토큰 10개
#pprint(text.vocab().most_common(10))
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
#%matplotlib inline
import matplotlib


##font_fname = '/Library/Fonts/AppleGothic.ttf'
##font_name = font_manager.FontProperties(fname=font_fname).get_name()
##rc('font', family=font_name)



font_location = 'C:\\WINDOWS\\Fonts\\NGULIM.ttf'
                    # ex - 'C:/asiahead4.ttf'
font_name = font_manager.FontProperties(fname = font_location).get_name()
matplotlib.rc('font', family = font_name)

#plt.figure(figsize=(20,10))
#text.plot(50) ##데이터 시각화

selected_words = [f[0] for f in text.vocab().most_common(2000)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]

import numpy as np

x_train = np.asarray(train_x).astype('float32')
x_test = np.asarray(test_x).astype('float32')

y_train = np.asarray(train_y).astype('float32')
y_test = np.asarray(test_y).astype('float32')

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(2000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
             loss=losses.binary_crossentropy,
             metrics=[metrics.binary_accuracy])

model.fit(x_train, y_train, epochs=10, batch_size=512)
results = model.evaluate(x_test, y_test)

def predict_pos_neg(review):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    if(score > 0.5):
        print("{:.2f}% 확률로 호평영화임\n".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정영화임\n".format((1 - score) * 100))


## 단어들 입력해서 sys.out으로 결과물 출력
import sys
fw = open('NaverSentimental.txt','w',encoding='utf-8')
stdout=sys.stdout # 저장
sys.stdout=fw

print('========어벤져스========')
with open('NaverReviewsNouns.txt', mode='r', encoding='utf-8') as fp:
    text = fp.read().splitlines()
    for sentences in text[0:30]:
        predict_pos_neg(sentences)

##어벤져스
print('===========시그널=======')
with open('NaverSignalNouns.txt', mode='r', encoding='utf-8') as fp:
    text = fp.read().splitlines()
    for sentences in text[0:30]:
        predict_pos_neg(sentences)

##시그널

print('===========7광구===========')
with open('NaverEscapeNouns.txt', mode='r', encoding='utf-8') as fp:
    text = fp.read().splitlines()
    for sentences in text[0:30]:
        predict_pos_neg(sentences)

print('===========오블리비언===========')
with open('NaverOblivionNouns.txt', mode='r', encoding='utf-8') as fp:
    text = fp.read().splitlines()
    for sentences in text[0:30]:
        predict_pos_neg(sentences)

print('===========싸이보그지만 괜찮아===========')
with open('NaverCyborgNouns.txt', mode='r', encoding='utf-8') as fp:
    text = fp.read().splitlines()
    for sentences in text[0:30]:
        predict_pos_neg(sentences)


##7광구
fw.close()
sys.stdout = stdout