# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 10:34:00 2015

@author: Yuhlin
based on code by
"""
from nltk import word_tokenize,WordNetLemmatizer,NaiveBayesClassifier,classify
# MaxentClassifier
from nltk.corpus import stopwords
import random
import os, glob, re
import codecs

# globals
wordlemmatizer = WordNetLemmatizer()
commonwords = stopwords.words('english')
    
# extract features from emails
def email_features(sent):
    features = {}
    words = word_tokenize(sent) # .decode("utf8")
    wordtokens = [wordlemmatizer.lemmatize(word.lower()) for word in words]
    for word in wordtokens:
        if word not in commonwords:
            features[word] =  True
    return features

# start main
if __name__ == '__main__':
    hamtexts  = []
    spamtexts  = []
    # The dataset we will use is located at the following url:
    # http://www.aueb.gr/users/ion/data/enron-spam/

    for infile in glob.glob( os.path.join('ham/', '*.txt')):
        #text_file = open(infile, "r")
        text_file = codecs.open(infile, "r", encoding="utf-8", errors='ignore')
        hamtexts.append(text_file.read())
        text_file.close()
    
    for infile in glob.glob( os.path.join('spam/', '*.txt') ):
        # text_file = open(infile, "r")
        text_file = codecs.open(infile, "r", encoding="utf-8", errors='ignore')
        spamtexts.append(text_file.read())
        text_file.close()
    
    mixedemails = ([(email,'spam') for email in spamtexts] + [(email,'ham') for email in hamtexts])
    
    random.shuffle(mixedemails)
    featuresets = [(email_features(n), g) for (n,g) in mixedemails]
    
    size = int(len(featuresets) * 0.35)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = NaiveBayesClassifier.train(train_set)
    #classifier = MaxentClassifier.train(train_set,'Powell',3)
    
    print 'accuracy: ', classify.accuracy(classifier,test_set)
    classifier.show_most_informative_features(30)
    print 'labels:',classifier.labels()
    for i in range(10):
        featset = email_features(raw_input("Enter text to classify: "))
        print classifier.classify(featset)
