from __future__ import division, print_function
from gensim import corpora, models, similarities, matutils
import re
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO  # ipython sometimes messes up the logging setup; restore

from gensim import corpora
from gensim import models

f1 = open('C:\Users\risha\Desktop\project 1\Topic Modelling\Hillary_text.txt','r')
f2 = open('C:\Users\risha\Desktop\project 1\Topic Modelling\Obama_text.txt','r')
f3 = open('C:\Users\risha\Desktop\project 1\Topic Modelling\Trump_text.txt','r')

content= f1.readlines()
content1= f2.readlines()
content2= f3.readlines()

corpus = content + content1 + content2
docs = []

for i in corpus:
    docs.append(i.strip().split())
dic = corpora.Dictionary(docs)
print (dic)

corpus = [dic.doc2bow(text) for text in docs]
print(type(corpus), len(corpus))

# term-document matrix
# for each document, word and count
#for corp in corpus:
#    print(len(corp), corp[:10])

tfidf = models.TfidfModel(corpus)
print(type(tfidf))

corpus_tfidf = tfidf[corpus]
print(type(corpus_tfidf))

NUM_TOPICS = count_topic
model = models.ldamodel.LdaModel(corpus_tfidf, 
                                 num_topics=NUM_TOPICS, 
                                 id2word=dic, 
                                 update_every=30, 
                                 passes=10)

print("LDA model")
topics_found = model.print_topics(count_topic)
counter = 1
for t in topics_found:
    print("Topic #{} {}".format(counter, t))
    counter += 1

model.print_topics()

