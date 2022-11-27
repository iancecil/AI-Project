#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Iancecil waweru Njoroge 134669
"""

import numpy as np
import pandas as pd
import re
import unicodedata
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer



# Removing end-of-line, tabulation and carriage return. Turning into lower case:
def clean_and_lowercase(text):
    """ text lowercase
        removes \n
        removes \t
        removes \r """
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")

    return text


# Remove Hyperlinks
def remove_hyperlinks(text):
    """ This function removes hyperlinks from texts
        inputs:
         - text """
    return re.sub(r"http\S+", " ", text) 


#Remove emails
def remove_emails(text):
    """ This function removes numbers from a text
        inputs:
         - text """
    return re.sub(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""", " ", text)

#Remove numbers
def remove_numbers(text):
    """ This function removes numbers from a text
        inputs:
         - text """
    return re.sub(r"\d+", " ", text) 


# Remove unknown characters
def encode_unknown(text):
    """ This function encodes special caracters """
    return unicodedata.normalize("NFD", text).encode('ascii', 'ignore').decode("utf-8") 
    
         
# Remove punctuations and special characters
def clean_punctuation_no_accent(text):
    """ This function removes punctuation and accented characters from texts in a dataframe 
        To be appplied to languages that have no accents, ex: english 
    """
    return re.sub(r'[^\w\s]', ' ',text) 


#Remove stop words
def remove_stop_words(text, stopwords=set(stopwords.words('english'))):
    """ This function removes stop words from a text
        inputs:
         - stopword list
         - text """
    
    # prepare new text
    text_splitted = text.split(" ")
    text_new = list()
    for word in text_splitted:
      if word not in stopwords:
          text_new.append(word)

    return " ".join(text_new)


# Removing one and two letters words, removing unnecessary spaces, droping empty lines:
def remove_spaces(text):
    """ This function
     1) removes remaining one-letter words and two letters words
     2) replaces multiple spaces by one single space
     3) drop empty lines """
    text = re.sub(r'\b\w{1,2}\b', " ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = text if len(text) != 1 else ''
    text = np.nan if text == '' else text
    return text

def lemmatize_one_text(text):
    """ This function lemmatizes words in text (it changes word to most close root word)
        inputs:
         - lemmatizer
         - text """

    # initialize lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # prepare new text
    text_splitted = text.split(" ")
    text_new = list()
    
    for word in text_splitted:
        text_new.append(lemmatizer.lemmatize(word))
  
    return " ".join(text_new)


def main(corpus):
    corpus = clean_and_lowercase(corpus)                             
    corpus = remove_hyperlinks(corpus)
    corpus = remove_emails(corpus)
    corpus = remove_numbers(corpus)
    corpus = encode_unknown(corpus)
    corpus = clean_punctuation_no_accent(corpus)
    corpus = remove_stop_words(corpus)
    corpus = remove_spaces(corpus)
    corpus = lemmatize_one_text(corpus)
    
    return corpus


def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)