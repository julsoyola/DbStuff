from pymongo import MongoClient

# Provide the mongodb atlas url to connect python to mongodb using pymongo
#CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase
client = MongoClient("mongodb://localhost:27017/")

# create Movie database
MovieDb = client["Movies"]

# create Posts collection
colReviews = MovieDb["Reviews"]

one_item = colReviews.find_one({"Id": 1}, {"Reviews": True})
print(one_item)

Comments = one_item["Reviews"]
print(Comments)

print(len(Comments))

#close connection
client.close()