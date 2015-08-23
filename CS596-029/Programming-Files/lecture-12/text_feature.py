# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:59:35 2015

@author: Yuhlin
"""

corpus = ['This is the first document.',
         'This is the second second document.',
         'And the third one.',
         'Is this the first document?',]
         
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
analyze = vectorizer.build_analyzer()
analyze("This is a text document to analyze.")
print vectorizer.get_feature_names()
print X.toarray()
print vectorizer.transform(['Something completely new.']).toarray()

# to preserve order
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)
print bigram_vectorizer.fit_transform(corpus).toarray()

# tf-idf
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
counts = [[3, 0, 1],
          [2, 0, 0],
          [3, 0, 0],
          [4, 0, 0],
          [3, 2, 0],
          [3, 0, 2]]
tfidf = transformer.fit_transform(counts)
print tfidf.toarray()

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
print X.toarray()

# cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial
counts= [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1],
         [1, 1, 0],
         [1, 0, 1],
         [0, 1, 1],
         [1, 1, 1],
         [1, 0, 1],
         [0, 1, 1]]
tfidf = transformer.fit_transform(counts)
print tfidf.toarray()
for vector in counts:
    #print spatial.distance.cosine(q, vector)
    print cosine_similarity(q, vector)
q = [1, 1, 0]
qt = transformer.transform(q)
for vector in tfidf.toarray():
    #print spatial.distance.cosine(q, vector)
    print cosine_similarity(qt, vector)
    