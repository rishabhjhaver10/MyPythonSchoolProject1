import os
import json
from textblob import TextBlob
import nltk
import string
#import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt

path = '/Users/Rishabh/Desktop/project 1/Tweets_2/New York/'
lst = []
for fname in os.listdir(path):
    print fname
    with open(path + fname, 'r') as f:
        data = json.load(f)       
        lst.extend(data)
        print(len(data), len(lst))
print(len(lst))

w = '' #string to store text of tweet
t = [] #list to store Trump tweets
u = [] #list to store Hillary tweets
v = [] #list to store Obama tweets

x = 'Trump'
y = 'Hillary'
z = 'Obama'

for twt in lst:
    w = twt['text']
    if x in w:
        t.append(w)
    elif y in w:
        u.append(w)
    elif z in w:
        v.append(w)

pol = [] #stores polarity for trump tweets
sub = [] #stores subjectivity for trump tweets      
        
for tw in t:
    #y = twt['text']
    tb = TextBlob(tw)
    pol.append(tb.sentiment.polarity)
    pol1 = sum(pol)/len(pol)
    sub.append(tb.sentiment.subjectivity)
    sub1 = sum(sub)/len(sub)
    #print y, tb.sentiment.polarity
print 'Polarity and Subjectivity for Trump: ',pol1, sub1

pol_1 = [] #stores polarity for hillary tweets
sub_1 = [] #stores subjectivity for hillary tweets

for tw in u:
    #y = twt['text']
    tb = TextBlob(tw)
    pol_1.append(tb.sentiment.polarity)
    pol2 = sum(pol_1)/len(pol_1)
    sub_1.append(tb.sentiment.subjectivity)
    sub2 = sum(sub_1)/len(sub_1)
    #print y, tb.sentiment.polarity
print 'Polarity and Subjectivity for Hillary: ',pol2, sub2

pol_2 = [] #stores polarity for obama tweets
sub_2 = [] #stores subjectivity for obama tweets

for tw in v:
    #y = twt['text']
    tb = TextBlob(tw)
    pol_2.append(tb.sentiment.polarity)
    pol3 = sum(pol_2)/len(pol_2)
    sub_2.append(tb.sentiment.subjectivity)
    sub3 = sum(sub_2)/len(sub_2)
    #print y, tb.sentiment.polarity
print 'Polarity and Subjectivity for Obama: ',pol3, sub3

       
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
tweet1 = ''
twt1 = ''
twt2 = ''

for item in t:
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
        
wordcloud1 = WordCloud().generate(text1)
plt.imshow(wordcloud1)
plt.axis("off")

text2 = ''
tweet2 = ''
twt1_1 = ''
twt2_1 = ''
        
for item in u:
    #tweet = item['text']
    #print tweet
    tweet2 = item.encode("utf-8")
    #tweet1 = tweet.decode('unicode_escape').encode('ascii','ignore')
    twt1_1 = tweet1.translate(table_p)
    #print twt1
    twt2_1 = twt1.translate(table_d)    
    #print twt2
    words = twt2.split()
    for word in words:
        try:
            if word not in stopwords:
                text2 += ' {}'.format(word)
        except:
            pass
        
wordcloud2 = WordCloud().generate(text2)
plt.imshow(wordcloud2)
plt.axis("off")

text3 = ''
tweet3 = ''
twt1_2 = ''
twt2_2 = ''

for item in v:
    #tweet = item['text']
    #print tweet
    tweet3 = item.encode("utf-8")
    #tweet1 = tweet.decode('unicode_escape').encode('ascii','ignore')
    twt1_2 = tweet1.translate(table_p)
    #print twt1
    twt2_2 = twt1.translate(table_d)    
    #print twt2
    words = twt2.split()
    for word in words:
        try:
            if word not in stopwords:
                text3 += ' {}'.format(word)
        except:
            pass
        
wordcloud3 = WordCloud().generate(text3)
plt.imshow(wordcloud3)
plt.axis("off")