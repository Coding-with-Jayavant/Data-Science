# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:23:34 2023

@author: Lenovo
"""
#the snetence tokeniztion , seperating sentences from 
import nltk
nltk.download('punkt')
data='my name is jay ? . !im so cleaver'
nltk_tokens=nltk.sent_tokenize(data)
print(nltk_tokens)

######################################################3333

#non english tokenization

german_tokenizer= nltk.load('tokenizers/punkt/german.pickle')
german_tokens= german_tokenizer.tokenize('wie geht es Ihnen? Gut, danke.')
print(german_tokens)
######################################333

#word tokenization
import nltk
word_data='it orgnised from the idea that there are readers who prefer'
nltk_token=nltk.word_tokenize(word_data)
print(nltk_token)

#########################################
import nltk
nltk.download('stopwords')
#it will download a file with english stopword,
#verifying the stopword

#doc. called corpus
from nltk.corpus import stopwords
stopwords.words('english')
""" stopwords
#'i',
 'me',
 'my',
 'myself',
 'we',
 'our',
 'ours',
 'ourselves',
 'you',
 "you're",
 "you'v
 """
########################################

#remove stop words from sentence
#1)tokenize
#2)remove stop word
from nltk.corpus import stopwords
en_stops=set(stopwords.words('english'))
all_words=['There','is','a','tree','near','river','the']
for word in all_words:
    if word not in en_stops:
        print(word)
#from avove all_words ther is remove stop words using nltk
"""
output-
There
tree
near
river
"""
#############################################33

#find synonyms word
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
#wordnet has all synonyms name
#doc. called corpus
from nltk.corpus import wordnet

synonyms=[]
for syn in wordnet.synsets("soil"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
""" output-
{'soil', 'filth', 'begrime', 'land', 'dirty', 'bemire', 'grunge', 
 'stain', 'ground', 'grease', 'dirt', 'grime', 'colly', 'territory'}
"""
################################################


#find antonyms word
import nltk
#wordnet has all synonyms and antonyms name
#doc. called corpus
from nltk.corpus import wordnet

antonyms=[]
for syn in wordnet.synsets("day"):
    for lm in syn.lemmas():
        antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))
""" output-

"""