"""
Name:JULIANA OYOLA-PABON
Date:02/22/23
Assignment:#7
Due Date:02/26/23
About this project:Implement and use a Document Database.
All work below was performed by Juliana Oyola Pabon
"""
from pymongo import MongoClient

def print_Menu():
    #print menu
    print("A) Add New Movie or Review ")
    print("B) Update ")
    print("C) Display All Movies and Reviews")
    print("D) Display a specific Movie Reviews")

    # Quit
    print("Q) Quit")

def getMenuOption():
    # get menu option
    option = str(input("Please enter in your option..."))
    # convert to upper case
    option = option.upper()
    # while menu option not valid choice
    while ((option < "A") and (option > "D") and (option != "Q") ):
        #display menu
        print_Menu()
        # get menu option
        option = str(input("Please enter in your option..."))
        # convert to upper case
        option = option.upper()
    return option

def Update():
    # Ask what to Update
    print("A) Update Movie Name")
    print("B) Update Review/Rating")

    option = str(input("Enter Value: "))
    option = option.upper()

    if(option == "A"): UpdateMovieName()
    else: UpdateReview()

def UpdateMovieName():
    print("What Movie Do you want to change?")
    name = GetValidString(1)
    print("What do you want to change " + name + " to?")
    newName = GetValidString(1)

    print("Do you want to change the Summary? y/n")
    option = str(input("Enter Value: "))
    option = option.upper()

    # when user changes the movie they can pick whether they want to update the summary
    if (option == "Y"): summary = GetValidString(1)
    # else new summary is empty
    else: summary = ""

    if (client.list_database_names().index("Movies") != -1):
        MovieDb = client["Movies"]
        # Does Reviews collection exist
        if (MovieDb.list_collection_names().index("Reviews") != -1):
            colReviews = MovieDb["Reviews"]

            # check to see if a post exists for that id
            if (colReviews.count_documents({"Name": name}) == 0):
                print("There is no movie listed.")
            else:
                # check to see if a Review exists for that movie
                one_item = colReviews.find_one({"Name": name}, {"Reviews": True})
                print(one_item)

                # insert new name
                myquery = {"Name": name}
                newvalues = {"$set": {"Name": newName, "Summary": summary}}

                colReviews.update_one(myquery, newvalues)

        else:
            # No posts
            print("Movies doesn't exist")
    else:
        # No posts
        print("Movie Doesn't Exist")


def UpdateReview():
    print("What Movie Rating Do You Want to Change?")
    name = GetValidString(1)

    print("What is your username?")
    username = GetValidString(2)

    print("What Rating do you want to change " + name + " to?")
    rating = GetRating()

    if (client.list_database_names().index("Movies") != -1):
        MovieDb = client["Movies"]
        # Does Reviews collection exist
        if (MovieDb.list_collection_names().index("Reviews") != -1):
            colReviews = MovieDb["Reviews"]

            # check to see if a post exists for that id
            if (colReviews.count_documents({"Name": name}) == 0):
                print("There is no movie listed.")
            else:
                # check to see if a Review exists for that movie
                one_item = colReviews.find_one({"Name": name}, {"Reviews": True})
                print(one_item)

                Reviews = one_item["Reviews"]
                print(Reviews)

                myquery = {"Name": username}
                newvalues = {"$set": {"Name": username, "Rating": rating}}

                colReviews.update_one(myquery, newvalues)
        else:
            # No posts
            print("Movies doesn't exist")
    else:
        # No posts
        print("Movie Doesn't Exist")

def AddReview(client):
    # get user
    print("**** Enter User ****")
    user = GetValidString(2)

    # get review
    print("**** Leave a Review ****")
    review = GetValidString(1)

    # get rating
    print("**** Rating out of 10 ***")
    rating = GetRating()

    # Does Movie database exist
    if (client.list_database_names().index("Movies") != -1):
        MovieDb = client["Movies"]
        # Does Movie collection exist
        if (MovieDb.list_collection_names().index("Reviews") != -1):
            colReviews = MovieDb["Reviews"]
            # user select the id
            name = str(input("Enter Name of Movie: "))

            # check to see if a post exists for that id
            if (colReviews.count_documents({"Name": name}) == 0):
                print("There is no Movie.")
            else:
                # check to see if a Review exists for that id
                one_item = colReviews.find_one({"Name": name}, {"Reviews": True})
                print(one_item)

                Reviews = one_item["Reviews"]
                print(Reviews)
                reviewId = 1 + len(Reviews)
                # create new Review
                newReview = {"Id": reviewId, "Name": user, "Rating": rating, "Review": review}
                Reviews.append(newReview)
                print(Reviews)

                # insert new post comment
                myquery = {"Name": name}
                newvalues = {"$set": {"Reviews": Reviews}}

                colReviews.update_one(myquery, newvalues)

        else:
            # No posts
            print("There are no reviews.")
    else:
        # No posts
        print("There are no reviews.")

# add a new Movie
def AddMovie(client):
    # get new Movie
    print("***** Add Movie Title *****")
    movie = GetValidString(1)

    # get summary for movie
    print("****** Add Summary ******")
    summary = GetValidString(1)

    # get duration in minutes
    print("***** Add Duration (In Minutes) *****")
    minutes = GetValidTime()

    # avg rating
    avgRating = GetAvgRating()

    # compute next ID
    # check if DB Exists
    if (client.list_database_names().index("Movies")!=-1):
        MovieDb = client["Movies"]
        # Does Reviews collection exist
        if (MovieDb.list_collection_names().index("Reviews")!=-1):
            colReviews = MovieDb["Reviews"]
            # Get the max Id value for all posts
            result = colReviews.find({},{"Id":True}).sort("Id",-1).limit(1)
            for r in result:
                # the nextId will be 1 + max Id value for all posts
                nextId = int(r["Id"]) +1
        else:
            # No posts
            nextId =1
    else:
        nextId = 1

    # create new post
    newReview = {"Id": nextId, "Name": movie, "Summary": summary, "Duration": minutes,
                 "Avg Rating": avgRating,  "Reviews": []}

    # insert new post
    colReviews.insert_one(newReview)

def GetRating():
    # the avg of the ratings in the reviews
    val = int(input("Enter Rating 1-10: "))

    while (val < 1 or val > 10 ):
        val = int(input("Enter Rating 1-10: "))
    return val

def GetAvgRating():
    val = 1.0
    return val;

def GetValidTime():
    # prompt and read int
    val = float(input("Enter Value In Minutes: "))

    while val <= 0:
         val = float(input("Enter Value More than 0: "))

    return val

def GetValidString(num):
    #prompt and read in string
    val = input("Enter Value: ")

    match num:
        # movie titles
        case 1:
            # while string empty
            while (len(val) <= 0):
                val = input("Enter in a value")
        # users
        case 2:
            val = val.strip()
            while (len(val) <= 0):
                val = input("Enter in a value")

    #return valid string
    return val

def DisplayAReview(review):
    # display the comment
    print("\t\t\t", "*** Comment ***")
    print("\t\t\t", "Id:", review["Id"])
    print("\t\t\t", "Name:", review["Name"])
    print("\t\t\t", "Review:", review["Review"])

def DisplayReviews(Review):
    # display All the reviews for that movie
    print("Id:", Review["Id"])
    print("Name:", Review["Name"])
    print("Reviews:", Review["Reviews"])
    print("*** Reviews For Movie ***")

    # for each review in the movie
    for r in Review["Reviews"]:
        # display the comment
        DisplayAReview(r)

def DisplayAll(client):

    #Display all movies and there Reviews
    if (client.list_database_names().index("Movies")!=-1):
        MovieDb = client["Movies"]

        ## Does Posts collection exist
        if (MovieDb.list_collection_names().index("Reviews")!=-1):
            colReviews = MovieDb["Reviews"]

            # locate all posts
            records = colReviews.find()
            # for each post
            for r in records:
                print("************")
                print("*** Reviews ***")
                # display the post
                DisplayReviews(r)
                print("************")
                print()
        else:
            # there are no posts
            print("*** There are no Reviews ***")
    else:
        # there are no posts
        print("*** There are no Reviews ***")

def DisplayMovieAndReview(client):
    # Display A Specific Review
    if (client.list_database_names().index("Movies")!=-1):
        MovieDb = client["Movies"]

        # Does Reviews collection exist
        if (MovieDb.list_collection_names().index("Reviews")!=-1):
            colReviews= MovieDb["Reviews"]

            # user select the id
            name = str(input("Enter Movie Name: "))

            #check to see if a post exists for that id
            if (colReviews.count_documents({"Name": name})==0):
                print("Movie Doesn't Exist")
            else:
                # if the post exists for that id
                # locate the post
                records = colReviews.find({"Name": name})
                # for that post
                for r in records:
                    print("************")
                    print("*** Post ***")
                    # display the post
                    DisplayReviews(r)
                    print("************")
                    print()
        else:
            # post does not exist
            print("*** There are no Posts ***")
    else:
        # post does not exist
        print("*** There are no Posts ***")

def mainApp(client):
    option = ""

    # while user decides not to quit
    while (option != "Q"):
        # show menu
        print_Menu()
        # get option from user
        option = getMenuOption()

        if (option == "A"):
            # Add a New Movie
            print("A) Add New Movie")
            print("B) Leave Review")
            val = str(input("Enter Choice: "))
            # convert to upper case
            val = val.upper()
            if (val == "A"): AddMovie(client)
            else: AddReview(client)

        elif (option == "B"):
            # Update
            Update()

        elif (option == "C"):
            # Display All Reviews and Movies
            DisplayAll(client)

        elif (option == "D"):
            # Display A specific Movies Review
             DisplayMovieAndReview(client)


if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    mainApp(client)
    #close connection
    client.close()