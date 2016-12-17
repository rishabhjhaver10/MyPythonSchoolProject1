import os
import json
from textblob import TextBlob
import nltk
import string
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt

path = '/Users/risha/Downloads/project 1/tweets/obama/'
lst = []
for fname in os.listdir(path):
    print fname
    with open(path + fname, 'r') as f:
        data = json.load(f)       
        lst.extend(data)
        print(len(data), len(lst))
print(len(lst))
x=[]
z=[] 
for twt in lst:
    #y = twt['text']
    tb = TextBlob(twt)
    x.append(tb.sentiment.polarity)
    x1 = sum(x)/len(x)
    z.append(tb.sentiment.subjectivity)
    z1 = sum(z)/len(z)
    #print y, tb.sentiment.polarity
print x1, z1

stopwords = nltk.corpus.stopwords.words('english')
stopwords.append('RT')
stopwords.append('https://t.co/')
stopwords.append('https')
stopwords.append('co')
stopwords.append('rt')
stopwords.append('amp')
stopwords.append('day')
stopwords.append('say')
#stopwords.append('\u2026')
#stopwords.append('\u2019')
#stopwords.append('\u2018')

p = string.punctuation
d = string.digits

table_p = string.maketrans(p, len(p) * " ")
table_d = string.maketrans(d, len(d) * " ")


text1 = ''
tweet = ''
tweet1 = ''
twt1 = ''
twt2 = ''

for item in lst:
    #tweet = item['text']
    #print tweet
    tweet1 = item.encode("utf-8")
    #tweet1 = tweet.decode('unicode_escape').encode('ascii','ignore')
    twt1 = tweet1.translate(table_p)
    #print twt1
    twt2 = twt1.translate(table_d)    
    #print twt2
    words = twt2.split()
    for word in words:
        try:
            if word not in stopwords:
                text1 += ' {}'.format(word)
        except:
            pass
        
wordcloud = WordCloud().generate(text1)
plt.imshow(wordcloud)
plt.axis("off")

wordcloud1 = WordCloud(max_font_size=40).generate(text1)
plt.figure()
plt.imshow(wordcloud1)
plt.axis('off')
plt.show() 

wordcloud2 = WordCloud(max_font_size=50).generate(text1)
plt.figure()
plt.imshow(wordcloud2)
plt.axis('off')
plt.show() 

wordcloud3 = WordCloud(max_font_size=60).generate(text1)
plt.figure()
plt.imshow(wordcloud3)
plt.axis('off')
plt.show() 

sys.exit(1)