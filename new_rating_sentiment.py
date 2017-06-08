import json, re, ast
import operator
import pprint as pp
import sqlite3 as lite
import sys
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt



client = MongoClient()
db_name = 'book-reviews'
db = client[db_name]
coll = db['rating_sentiment']

#print coll
cursor = coll.find({})
#print cursor
n_groups = 0
rating = []
sentiment = []
movies = []
for doc in cursor:
    movies.append(doc['movie_name'])
    rating.append(doc['avg_rating'])
    sentiment.append(doc['avg_sentiment'])
    n_groups = n_groups+1
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, tuple(rating), bar_width,
                 alpha=opacity,
                 color='b',
                 label='Rating')
 
rects2 = plt.bar(index + bar_width, tuple(sentiment), bar_width,
                 alpha=opacity,
                 color='g',
                 label='Sentiment')
 
plt.xlabel('Books')
plt.ylabel('Results')
plt.title('Results by Books')
plt.xticks(index + bar_width, tuple(movies))
plt.legend()
 
plt.tight_layout()
plt.show()  


