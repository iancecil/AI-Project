#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Iancecil Waweru Njoroge
"""
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

def process_postings(results):
    
    # Subset only needed columns
    cols = list(['JobID']+ ['JobTitle'] + ['Company'] + ['Summary'])
    data = results[cols]
    
    data.columns = ['job_id', 'job_title', 'company', 'summary']
    
    # combining the columns of title, company and summary
    data['combined_info'] = data["job_title"].map(str) + " " + data["company"] +" "+data['summary']
    
    # remove unnecessary characters
    data['combined_info'] = data['combined_info'].str.replace('[^a-zA-Z \n\.]'," ")
    
    # convert to lower case
    data["combined_info"] = data["combined_info"].str.lower()
    
    data = data[['job_id', 'combined_info']]
    data = data.fillna(" ")
    
    # Remove stopwords
    stemmer =  PorterStemmer()
    stop = stopwords.words('english')
    combined_info = data['combined_info']
    only_text = combined_info.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    
    # Stemming
    only_text = only_text.apply(lambda x : filter(None,x.split(" ")))
    only_text = only_text.apply(lambda x : [stemmer.stem(y) for y in x])
    only_text = only_text.apply(lambda x : " ".join(x))
    
    data['text'] = only_text
    data = data.drop("combined_info", 1)
    
    return data
    # print(len(data))
    # print(data.head())