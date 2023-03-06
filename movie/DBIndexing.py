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

#1) Create a find that does not use an index
results = colReviews.find()
print("******* ALL RESULTS IN MOVIE DB ********************************")
for result in results:
  print(result)
print()

#2) Use the Explain to show that no index is used when running the find from step 1
results = colReviews.find().explain()
print("******* Explain DB ********************************")
print(result)
print()

#3)Add an index that will be used when running the find from step 1
colReviews.create_index([("Avg Rating", 1)])

#4)Use the Explain to show that an index is now used when running the find from step 1
print("******* Explain DB ********************************")
result = colReviews.find().explain()
print(result)
print()

#5) Drop the index you created in step 3
colReviews.drop_index([("Avg Rating", 1)])
print("******* Explain DB ********************************")
result = colReviews.find().explain()
print(result)
print()

client.close()