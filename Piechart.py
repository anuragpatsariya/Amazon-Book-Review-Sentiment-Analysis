import json, re, ast
import operator
import pprint as pp
import sqlite3 as lite
import sys
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

client = MongoClient()
db_name = 'book-reviews'
db = client[db_name]
coll = db['rating_sentiment']
cursor = coll.find({})
print type(cursor)
#figure(1, figsize=(8,4))
plt.figure(1)
ax = axes([0.1, 0.1, 0.8, 0.8])
#graph_counts = 0
#plt.figure(
for i, doc in enumerate(cursor):
    movie_name = doc['movie_name']
    ratings = []
    ratings.append(doc['rating1'])
    ratings.append(doc['rating2'])
    ratings.append(doc['rating3'])
    ratings.append(doc['rating4'])
    ratings.append(doc['rating5'])
    #graph_counts = graph_counts+1
    #plt.figure(graph_counts)
    plt.subplot(math.ceil(cursor.count()/2),2,i+1)
    labels = '1.0', '2.0', '3.0', '4.0','5.0'
    #sizes = [15,30,45, 10,5]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue','red']
    #figure(graph_counts)
    #figure(movie_name)
    #subplot(2,2,graph_counts)
    patches, texts = plt.pie(ratings, colors=colors[:labels.__len__()], shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title(movie_name)
'''
# make a square figure and axes
figure(1, figsize=(8,4))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = '1.0', '2.0', '3.0', '4.0','5.0'
sizes = [15,30,45, 10,5]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue','red']

figure(1)
subplot(2,2,1)
patches, texts = pie(sizes, colors=colors[:labels.__len__()], shadow=True, startangle=90)
legend(patches, labels, loc="best")


figure(1)
subplot(2,2,2)
patches, texts = pie(sizes, colors=colors[:labels.__len__()], shadow=True, startangle=90)
legend(patches, labels, loc="best")

figure(1)
subplot(2,2,3)
patches, texts = pie(sizes, colors=colors[:labels.__len__()], shadow=True, startangle=90)
legend(patches, labels, loc="best")

figure(1)
subplot(2,2,4)
patches, texts = pie(sizes, colors=colors[:labels.__len__()], shadow=True, startangle=90)
legend(patches, labels, loc="best")

'''
show()
plt.plot()




