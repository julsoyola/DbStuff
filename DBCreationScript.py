from pymongo import MongoClient

# Connect to your local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# drop database
client.drop_database("Movies")

# create Movie Database
MovieDb = client["Movies"]

# create Review Collection
colReviews = MovieDb["Reviews"]

mylist = [
    {
        "Id": 1, "Name": "Spirited Away", "Summary": "10-year-old Chihiro and her parents"
                                                     " stumble upon a seemingly abandoned "
                                                     "amusement park.",
        "Duration": 95,
        "Avg Rating": 8.5,
        "Reviews": []

    },
    {
        "Id": 2, "Name": "The Hurt Locker", "Summary": "The film follows an Iraq War Explosive "
                                                       "Ordnance Disposal team who are targeted by "
                                                       "insurgents and shows their psychological "
                                                       "reactions to the stress of combat.",
        "Duration": 90,
        "Avg Rating": 6.5,
        "Reviews": [{"Id": 1, "Name": "Sarah", "Rating": 8.0, "Review": "Greate Movie"},
                    {"Id": 2, "Name": "Este", "Rating": 5.5, "Review": "Cool Film, but def not part of my top 3"}]
    }
]

x = colReviews.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

records = colReviews.find()
for r in records:
    print(r)

#close connection
client.close()
