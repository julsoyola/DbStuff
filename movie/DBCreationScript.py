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
    },
{
        "Id": 3, "Name": "Tron", "Summary": "Future Cars.",
        "Duration": 90,
        "Avg Rating": 6.5,
        "Reviews": []
    },
{
        "Id": 4, "Name": "Little Women", "Summary": "",
        "Duration": 90,
        "Avg Rating": 6.5,
        "Reviews": []
    },
{
        "Id": 5, "Name": "Decsion To leave", "Summary": "Murder and love",
        "Duration": 90,
        "Avg Rating": 6.5,
        "Reviews": [{"Id": 1, "Name": "Sarah", "Rating": 7.0, "Review": "Greate Movie"},
                    {"Id": 2, "Name": "Este", "Rating": 5.5, "Review": "Cool Film, but def not part of my top 3"}]
    },
{
        "Id": 6, "Name": "Our Time", "Summary": "love",
        "Duration": 190,
        "Avg Rating": 3.5,
        "Reviews": [{"Id": 1, "Name": "Mandy", "Rating": 2.0, "Review": "Nah did not like"},
                    {"Id": 2, "Name": "Este", "Rating": 5.5, "Review": "Cool Film"}]
    },
{
        "Id": 7, "Name": "Fish Tales", "Summary": "Silly Fish",
        "Duration": 120,
        "Avg Rating": 4.5,
        "Reviews": [{"Id": 1, "Name": "Sarah", "Rating": 4.0, "Review": "Kinda dumb"},
                    {"Id": 2, "Name": "Este", "Rating": 6.0, "Review": "Funny, but not a fav"}]
    },
{
        "Id": 8, "Name": "The Whale", "Summary": "",
        "Duration": 95,
        "Avg Rating": 0,
        "Reviews": []
    },
{
        "Id": 9, "Name": "Mulan", "Summary": "Disney Film",
        "Duration": 90,
        "Avg Rating": 8.0,
        "Reviews": [{"Id": 1, "Name": "Sarah", "Rating": 7.0, "Review": "Greate Movie"},
                    {"Id": 2, "Name": "Este", "Rating": 9.5, "Review": "Loved"}]
    },
{
        "Id": 10, "Name": "Moonlight", "Summary": "",
        "Duration": 90,
        "Avg Rating": 8.5,
        "Reviews": [{"Id": 1, "Name": "Ron", "Rating": 8.0, "Review": "Greate Movie"},
                    {"Id": 2, "Name": "Laura", "Rating": 9.5, "Review": "Cool Film, but def not part of my top 3"},
                    {"Id": 3, "Name": "Michael", "Rating": 9.0, "Review": "Fun watch!!"}]
    },

]

x = colReviews.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

records = colReviews.find()
for r in records:
    print(r)

#close connection
client.close()
