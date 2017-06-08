import json, re, ast
import operator
import pprint as pp
import sqlite3 as lite
import sys
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt

#creating connection to Database
client = MongoClient()
db_name = 'book-reviews'
db = client[db_name]
coll = db['rating_sentiment']
afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)

#getting the names of movies stored in DB
movie_names = db.collection_names()
movies = []
rating = []
sentiment = []

#calculate average rating and average sentiment for each movie
for mn in movie_names:
    collection = db[mn]
    cursor = collection.find({})
    count = 0
    avg_rating = 0.0
    avg_sentiment = 0.0
    total_rating = 0.0
    total_sentiment = 0.0
    temp = 0
    count_negative_sentiment = 0
    count_positive_sentiment = 0
    count_rating1 = 0
    count_rating2 = 0
    count_rating3 = 0
    count_rating4 = 0
    count_rating5 = 0
    for doc in cursor:
        temp = temp+1
        #if temp%500 == 0:
        #    print temp
        sentiment_score = 0.0
        count = count + 1
        temp_rating = float(doc['rating'])
        if temp_rating == 1.0 :
            count_rating1 = count_rating1 + 1
        if temp_rating == 2.0 :
            count_rating2 = count_rating2 + 1
        if temp_rating == 3.0 :
            count_rating3 = count_rating3 + 1
        if temp_rating == 4.0 :
            count_rating4 = count_rating4 + 1
        if temp_rating == 5.0 :
            count_rating5 = count_rating5 + 1
        total_rating = total_rating + float(doc['rating'])
        word_arr = doc['review_text'].strip().split(" ")
        sentiment_score = 0.0  
        
        for word in word_arr:
            
            if word.lower() in scores.keys():
                #print "in if loop"
                sentiment_score = sentiment_score + int(scores[word.encode('utf-8').lower()])
        if sentiment_score < 0 :
            count_negative_sentiment = count_negative_sentiment + 1
        else :
            count_positive_sentiment = count_positive_sentiment + 1
        total_sentiment = total_sentiment + sentiment_score
        if temp == 1000:
            break
    movie_name = mn
    avg_sentiment = total_sentiment/count
    avg_rating = total_rating/count
    print count_rating1, count_rating2,count_rating3,count_rating4,count_rating5,count_negative_sentiment,count_positive_sentiment

#storing rating and sentiment details to database
    doc = {}
    doc['movie_name'] = movie_name
    doc['rating1'] = count_rating1
    doc['rating2'] = count_rating2
    doc['rating3'] = count_rating3
    doc['rating4'] = count_rating4
    doc['rating5'] = count_rating5
    doc['count_negative_sentiment'] = count_negative_sentiment
    doc['count_positive_sentiment'] = count_positive_sentiment
    doc['avg_rating'] = avg_rating
    doc['avg_sentiment'] = avg_sentiment
    coll.insert_one(doc)
    
    #print "total sentiment score: "+str(total_sentiment)
    #print "count: "+str(count)
    print "avg rating: ", type(avg_rating), avg_rating
    print "avg sentiment: ", type(avg_sentiment), avg_sentiment
    #print movie_name
    movies.append(movie_name)
    rating.append(avg_rating)
    sentiment.append(avg_sentiment)

'''
########------ Graph plotting part ----######
#print tuple(movies)
#print tuple(rating)
#print tuple(sentiment)

# data to plot
n_groups = movies.__len__()
#avg_rating = (90, 55, 40, 65, 44, 67, 20, 36)

#print type(avg_rating)
#avg_sentiment = (85, 62, 54, 20, 45, 68, 90, 25)
 
# create plot
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
 
plt.xlabel('Movies')
plt.ylabel('Results')
plt.title('Results by Movies')
plt.xticks(index + bar_width, tuple(movies))
plt.legend()
 
plt.tight_layout()
plt.show()  
'''
