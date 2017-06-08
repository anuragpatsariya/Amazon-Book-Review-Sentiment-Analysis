import json, re, ast
import operator
import pprint as pp
import sqlite3 as lite
import sys
from pymongo import MongoClient

client = MongoClient()
db_name = 'book-reviews'
db = client[db_name]

f1 = open('movie_list.txt','r')
f2 = f1.read()
f1.close()
file_names = f2.strip('\n').split('\n')
for name in file_names:
    temp = name.replace("F:/amazon_book_reviews/","")
    print temp
    file_content = open(temp,'r')
    print temp+" file opened"
    #coll_name = temp.strip(".csv")
    temp = temp.strip(".csv")
    coll_name  = temp
    coll = db[coll_name]
    for record in file_content:
        r = re.split('	\/gp\/customer-reviews\/|\?ASIN=	|	\"<span class=\"\"a-size-base review-text\"\">',record)
        rating = r[0]
        #print rating
        review_id = r[1][:13]
        #print review_id
        review_title = r[1][30:].lstrip("\t").strip(" ")
        #print review_title
        text = r[2]
        review_text = text.replace('</span>\"','').strip("\n")
        #print review_text

        #code to put data into database
        doc = {}
        doc['rating'] = rating
        doc['review_id'] = review_id
        doc['review_title'] = review_title
        doc['review_text'] = review_text
        coll.insert_one(doc)
    
    file_content.close()
