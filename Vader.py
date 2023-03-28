from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(text):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(text)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("text was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("text was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("text was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Text Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")

f= open('MetacriticNouns.txt','r',encoding='utf-8')
text = f.read()
lines = text.split('\n')
f.close()
import sys
fw= open('vader.txt','w', encoding='utf-8')
stdout=sys.stdout # 저장
sys.stdout=fw

sentiment_scores(text)
print('=======================')
for line in lines[0:30]:
    sentiment_scores(line)

fw.close()
sys.stdout = stdout
