# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 10:27:59 2015

@author: Yuhlin
"""
import nltk
# step-1 download nltk data
# nltk.download()

from nltk import pos_tag, word_tokenize, ne_chunk

sentence1 = 'this demostration will show how to detect parts of speech with little effort using NLTK!'
words1 = word_tokenize(sentence1)
print pos_tag(words1)

sentence2 = "My cat likes eating bananas"
words2 = word_tokenize(sentence2)
print pos_tag(words2)

sentence3 = "My uncle Fred's cat likes eating bananas"
words3 = word_tokenize(sentence3)
tags = pos_tag(words3)
print ne_chunk(tags)

# stopword removal
words = words1 + words2
from nltk.corpus import stopwords
stop = stopwords.words('english')
words_nonstop = [word for word in words if word not in stop]
print words
print words_nonstop

# stemming
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
words_stemmed = [stemmer.stem(word) for word in words_nonstop]
print words_stemmed

from nltk.corpus import wordnet

print wordnet.synsets('dog') # works even if you use ‘dogs’ instead

from nltk.corpus import wordnet as wn

dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')

similarity_score = dog.path_similarity(cat)
print similarity_score
similarity_score = dog.wup_similarity(cat)
print similarity_score

'''
POS_tag from www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
#   Tag     Description
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
'''