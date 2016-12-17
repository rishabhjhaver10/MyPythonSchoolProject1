import numpy as np  # a conventional alias
import glob
import os
import string
import nltk
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import decomposition

f1 = open('\Users\risha\Desktop\project 1\Topic Modelling\Hillary_text.txt','r')
f2 = open('\Users\risha\Desktop\project 1\Topic Modelling\Obama_text.txt','r')
f3 = open('\Users\risha\Desktop\project 1\Topic Modelling\Trump_text.txt','r')

content= f1.readlines()
content1= f2.readlines()
content2= f3.readlines()

corpus = content + content1 + content2

vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
dtm = vectorizer.fit_transform(corpus)
vocab = vectorizer.get_feature_names() # list of unique vocab, we will use this later
print('(# of Docs, # of Unique Words)') 
print(dtm.shape) 

num_topics = count_topic

clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)
print('# of topics, CLF Reconstruction Error')
print (num_topics, clf.reconstruction_err_)

topic_words = []
num_top_words = 7
for topic in clf.components_:
    #print topic.shape, topic[:5]
    word_idx = np.argsort(topic)[::-1][0:num_top_words] # get indexes with highest weights
    #print 'top indexes', word_idx
    topic_words.append([vocab[i] for i in word_idx])
    #print topic_words[-1]
    #print

print ('*'* 90)   
for t in range(len(topic_words)):
    print ("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))
    

    
