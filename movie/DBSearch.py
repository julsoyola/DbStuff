"""
Name:JULIANA OYOLA-PABON
Date:02/27/23
Assignment:#8
Due Date:03/12/23
About this project:Implement and use a Document Database. DB Search Part 1
All work below was performed by Juliana Oyola Pabon
"""

from pymongo import MongoClient

# Connect to your local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# I will be using the same Database from previous assignment
MovieDb = client["Movies"]
colReviews = MovieDb["Reviews"]

#1)Using find you must display all items in your collection to the screen
results = colReviews.find()
print("******* ALL RESULTS IN MOVIE DB ********************************")
for result in results:
  print(result)
print()

#2) Create a find that using an  $lt
print("***** Movies with an AVG Rating Less Than 7 ****************************")
results = colReviews.find( { "Avg Rating": { "$lt": 7 } } )
for result in results:
  print(result)
print()

#3) Create a find that using an  $gte
print("****** Movies with an AVG Rating Greater or Equal to 6.5 **************")
results = colReviews.find( { "Avg Rating": { "$gte": 6.5 } } )
for result in results:
  print(result)
print()

#4) Create a find that using an  $eq
print("****** Movies with Duaration of 90 mins ********************")
results = colReviews.find( { "Duration": { "$eq": 90 } } )
for result in results:
  print(result)
print()

#5) Create a find that using an  $ne
print("****** Movies with Duaration that is not 90 mins ********************")
results = colReviews.find( { "Duration": { "$ne": 90 } } )
for result in results:
  print(result)
print()

# 6) Create a find that using an  $or
print("****** Movie Reviews by Sarah or a Rating of 8 or Higher ********************")
query = {"Reviews.Name": "Sarah",
           "$or": [
                { "Reviews.Rating": {"$gte": 8}}
                    ]}
results = colReviews.find(query)
for result in results:
  print(result)
print()

#7) Create a find that using an  $and
print("****** Movie Reviews by Este w a Rating of 5 or Higher ********************")
query = {"Reviews.Name": "Este",
           "$and": [
                { "Reviews.Rating": {"$gte": 5}}
                    ]}
results = colReviews.find(query)
for result in results:
  print(result)
print()

#8) Create a find that using an  $not
print("****** Movies w/ No Summaries ********************")
results = colReviews.find({"Summary": {"$not": {"$gt": ""}}})
for result in results:
  print(result)
print()

#9) Create a find that using an $exist
print("****** Movies w No Reviews ********************")
results = colReviews.find({"Reviews.Review": {"$exists": False}})
for result in results:
  print(result)
print()

#10) Create a find that using an $elemMatch
print("****** First Review in Every Movie  ********************")
results = colReviews.find({"Reviews": {"$elemMatch": {"Id": {"$eq": 1}}}})
for result in results:
  print(result)
print()

# 11) Create a statement that using an $inc
print("****** Decrement Dunes Duration ********************")
query = colReviews.update_many(
    {"Name": "Dune"},
    {"$inc": {"Duration": -10}})
results = colReviews.find( { "Name": { "$eq": "Dune" } } )
for result in results:
  print(result)
print()

#12) Create a find using {item: null } null search
print("****** Null Search  ********************")
results = colReviews.find({"Summary": None})
for result in results:
  print(result)
print()

#13) Create a find using {item: {$exists : false} } null search
print("****** Movies w No Reviews ********************")
results = colReviews.find({"Reviews.Review": {"$exists": False}})
for result in results:
  print(result)
print()

#14) Create a find using {item: {$type : 10} } null search
print("****** Movies w Type String For Name ********************")
results = colReviews.find({"Name": {"$type": "string"}})
for result in results:
  print(result)
print()

#15) Create a find that uses projection to limit the results to two fields per document
print("****** Projection ********************")
results = colReviews.find({"Name": "The Hurt Locker"}, {"Reviews.Review": 1,"Reviews.Rating": 1})
for result in results:
  print(result)
print()

client.close()