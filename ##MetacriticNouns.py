import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
import re
from pprint import pprint

# Data processing
f = open('MetacriticReviews.txt', 'r', encoding='utf-8')
text = f.read()
f.close()
text.lower()
text = re.sub("\\.+","",text) ### preprocessing: remove a dot
text = re.sub("\\?+","",text) ### remove a ?
text = re.sub("\\!+","",text) ### remove a !
text = re.sub("\\,+","",text) ### remove a ?


tokens = [word for sent in nltk.sent_tokenize(text)
          for word in nltk.word_tokenize(sent)]
# remove stopwords
stop = stopwords.words('english')
tokens = [token for token in tokens if token not in stop]
stop1 = ('3D', '12/19/09', '110', '10sound', '10:00','10', '10+' ,'[0-1]', '/', 'sooo', '97', '90', '…','…','.', 'hurr')
tokens = [token for token in tokens if token not in stop1]
tokens = [word for word in tokens if len(word) >= 3] #remove word less than three letters
# lower capitalization
tokens = [word.lower() for word in tokens]

# lemmatization
wn = WordNetLemmatizer()
tokens = [wn.lemmatize(word) for word in tokens]
tokens = [wn.lemmatize(word, 'v') for word in tokens]
# stemming
#stemmer =PorterStemmer()
#tokens = [stemmer.stem(word) for word in tokens]

## nouns
tagged=nltk.pos_tag(tokens)
print(tagged)
tokens_noun = [word for word, pos in tagged if pos in ['NN', 'NNP']]
## transcribing

fw = open('MetacriticNouns.txt', 'w', encoding='utf-8')
tokens_noun = [word for word in tokens_noun if len(word) >= 3]
tokens_noun = [word for word in tokens_noun if len(word) <= 15]
tokens_noun_stop = [word for word in tokens_noun if word not in stop1]
fw.write('\t'.join(tokens_noun_stop))
fw.close()












