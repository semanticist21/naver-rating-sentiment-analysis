import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
import re
from pprint import pprint

# Data processing
f = open('MetacriticReviews.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
fw = open('MetacriticNouns.txt', 'w', encoding='utf-8')
for line in lines:
    line.lower()
    line = re.sub("\\.+", "", line)  ### preprocessing: remove a dot
    line = re.sub("\\?+", "", line)  ### remove a ?
    #line = re.sub("\\!+", "", line)  ### remove a !
    #line = re.sub("\\,+", "", line)  ### remove a ,
    line = re.sub("\\*+", "", line)  ### remove a ,

    #tokenize
    tokens = [word for sent in nltk.sent_tokenize(line)
              for word in nltk.word_tokenize(sent)]
    stop = stopwords.words('english')

    tokens = [token for token in tokens if token not in stop]

    stop1 = ('hurr', 'um', 'umm')

    tokens = [token for token in tokens if token not in stop1]
    tokens = [word for word in tokens if len(word) >= 3]  # remove word less than three letters

    # lower capitalization
    tokens = [word.lower() for word in tokens]

    # lemmatization
    wn = WordNetLemmatizer()
    tokens = [wn.lemmatize(word) for word in tokens]
    tokens = [wn.lemmatize(word, 'v') for word in tokens]

    # stemming
    #stemmer = PorterStemmer()
    #tokens = [stemmer.stem(word) for word in tokens]

    ## nouns
    tagged = nltk.pos_tag(tokens)
    tokens_noun = [word for word, pos in tagged if pos in ['NN', 'NNP', 'JJ', 'VB']]

    ## transcribing


    tokens_noun2 = [word for word in tokens_noun if len(word) >= 3]
    tokens_noun3 = [word for word in tokens_noun2 if len(word) <= 15]
    tokens_noun_stop = [word for word in tokens_noun3 if word not in stop1]
    fw.write('\t'.join(tokens_noun_stop) + '\n')

fw.close()












