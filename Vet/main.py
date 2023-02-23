"""
Name: Juliana Oyola-Pabon
Date:02/06/2023
Assignment:Module5:Basic Key Value Store App
# Due Date:02/19/2023
# About this project: Implement an application with a key value database.
# Assumptions:
# All work below was performed by Juliana Oyola """

import pickledb
from datetime import date
import sqlite3

# load the DB for the Animals
db = pickledb.load('Vet.db', False)


def DictName(Part1):
    # get current date
    today = date.today()
    # mm/dd/YY
    d1 = today.strftime("%mm%dd%Y")
    return str(Part1 + '%%' + d1)


def getMaxId():
    animalNum = 1
    while db.exists(genKey(str(animalNum))):
        animalNum += 1

    # print(stdNum)
    return str(animalNum)


def genKey(animalNum):
    # get current date
    today = date.today()
    # mm/dd/YY
    d1 = today.strftime("%mm%dd%Y")

    return str('Animal' + ':' + d1 + ':' + animalNum)


def RemoveAll():
    # remove all data from key value store db
    db.deldb();


def print_Menu(hasAnimalInfo, Registered):
    # Add/Edit
    if Registered:
        print("A) Add Animal Info")
        # Delete by date lookup
        print("C) Delete Past Animal")

    elif hasAnimalInfo:
        print("A) Edit Animal Info")
        # Display Animal Info
        print("B) Display Animal Info")
        # Delete
        print("D) Delete Current Animal Info")
        # Add to your relational like Registering
        print("G) Add/Register Animal Info")


    else:
        print("A) Add Animal Info")
        print("C) Delete Past Animal")

    print("H) Display All Animal Info")
    print("Q) Quit")


def get_MenuOption():
    # Get the menu Option
    option = str(input("Please Enter an Option..."))

    # Convert to upper case
    option = option.upper()

    # Check for valid choices
    while (option < "A") and (option > "B") and (option > "H") and (option != "Q"):
        # display menu options
        print_Menu()

        # get menu option
        option = str(input("Please Enter an Option..."))

        # convert to upper case
        option = option.upper()

    return option


def addAnimal(hasAnimalInfo, Animal, Name, Gender, Weight, CellPh, Type, Date):
    if hasAnimalInfo:
        # Display the current Animal type
        print("Current Animal: ", Animal)

    # If nothing exists then add it
    print("Animal: ")
    Animal = getValidString()
    if not hasAnimalInfo:
        db.dcreate(DictName('Animal'))
        db.set(DictName('AnimalExists'), 1)
    db.dadd(DictName('Animal'), ('Animal', Animal))

    if hasAnimalInfo:
        # print the animals name
        print("Current Name: ", Name)

    # If not grab the name
    print("Name: ")
    Name = getValidString()
    db.dadd(DictName('Animal'), ('Name', Name))

    # Get Gender
    if hasAnimalInfo:
        # print Gender
        print("Gender: ", Gender)

    # Grab Gender
    print("Gender: ")
    Gender = getValidGender()
    db.dadd(DictName('Animal'), ('Gender', Gender))

    # grab weight
    if hasAnimalInfo:
        print("Weight: ", Weight)

    # grab weight
    print("Weight: ")
    Weight = getValidWeight()
    db.dadd(DictName('Animal'), ('Weight', Weight))

    # grab Cell Phone
    if hasAnimalInfo:
        print("CellPhone: ", CellPh)

    # grab cell phone number if not
    print("CellPhone: ")
    CellPh = validCellPhone()
    db.dadd(DictName('Animal'), ('CellPh', CellPh))

    # set as true since now we have our info
    hasAnimalInfo = True

    if Weight < 10.0:
        Type = "Small"
    else:
        Type = "Large"

    if hasAnimalInfo:
        print("Date: " + Date)
    db.dadd(DictName('Animal'), ('Date', Date))

    return hasAnimalInfo, Animal, Name, Gender, Weight, CellPh, Type, Date


def getValidString():
    # prompt and read string
    val = input("Enter Your Response ")

    # strip string of spaces
    val = val.strip()

    # while there is nothing in string
    while len(val) <= 0:
        # prompt and read in string
        val = input("Please write again: Can not be empty ")
        # strip string of spaces

    val = val.strip()
    val = val.upper()
    # return valid string
    return val


def getValidWeight():
    # prompt and read in weight

    val = float(input("Enter Animals Weight "))

    # if it is invalid get a correct weight
    while val <= 0:
        val = float(input("Enter a Weight Greater than 0 "))

    # return valid Weight
    return val


def getValidGender():
    # prompt and read in response
    print("Write Your Animals Sex: ")
    val = input("Gender: Write 'M' or 'F' ")

    # strip string of spaces
    val = val.strip()

    while len(val) <= 0 or val < "A":
        # can not be empty, prompt to write again
        val = input("Can not be Empty, Type a Response: M or F ")
        # strip string of spaces
        val = val.strip()

    # Convert to Upper
    val = val.upper()
    if val == "M":
        val = "Male"
    else:
        val = "Female"

    return val


def validCellPhone():
    # prompt and read in response
    print("Write Your Phone Number: ")
    val = input("CellPhone: ")

    # strip string of spaces
    val = val.strip()

    while len(val) <= 0 or val > "A":
        # can not be empty, prompt to write again
        val = input("Must have Valid Integers, Type a Response:")
        # strip string of spaces
        val = val.strip()

    return val


def deleteAnimal(Animal, Name, Gender, Weight, CellPh):
    print("***********************************")
    print("Deleting " + Name + " now...")
    print("***********************************")
    # displayAnimal(Animal, Name, Gender, Weight, CellPh)
    # delete each key (info from animal)
    db.dpop(DictName('Animal'), 'Animal')
    db.dpop(DictName('Animal'), 'Name')
    db.dpop(DictName('Animal'), 'Gender')
    db.dpop(DictName('Animal'), 'Weight')
    db.dpop(DictName('Animal'), 'CellPh')
    db.dpop(DictName('Animal'), 'Date')


def displayAnimal(Animal, Name, Gender, Weight, CellPh):
    print("******* : ANIMAL INFO : ***********")
    print("Animal: ", Animal)
    print("Name: ", Name)
    print("Gender: ", Gender)
    print("Weight: ", Weight)
    print("Cell Phone Num: ", CellPh)
    print("***********************************")


# load and return the Animals Info this will save it
def loadAnimals():
    # load animals from key value store
    Animal = db.dget(DictName('Animals'), 'Animal')
    Name = db.dget(DictName('Animals'), 'Name')
    Gender = db.dget(DictName('Animals'), 'Gender')
    Weight = db.dget(DictName('Animals'), 'Weight')
    CellPh = db.dget(DictName('Animals'), 'CellPh')
    Type = db.dget(DictName('Animals'), 'Type')
    d1 = db.dget(DictName('Animals'), 'Date')

    # return Animal info
    return Animal, Name, Gender, Weight, CellPh, Type, d1


# Register an Animal
def RegAnimal(Animal, Name, Gender, Weight, CellPh, Date):
    # connect to sqlite db
    conn = sqlite3.connect('VetData.db')
    # get cursor
    cur = conn.cursor()

    # create a key for the date
    # insert new record
    sql_insert_query = """Insert Into Vet (
       'Animal','AnimalName','Gender','Weight', 'CellPh', 'Date') 
       Values (?, ?, ?, ?, ?, ?);"""
    cur.execute(sql_insert_query, (Animal, Name, Gender, Weight, CellPh, Date))

    # commit and save changes to database
    conn.commit()
    print("***********************************")
    print(Name + " has been registered...")
    print("***********************************")


    # close database connection
    conn.close()

    # delete key store db
    RemoveAll()


def DisplayAllRegAnimals():
    # connect to sqlite db
    conn = sqlite3.connect('VetData.db')
    # get cursor
    cur = conn.cursor()
    # get all record from Animal table
    cur.execute('''Select * from Vet;''')
    print(f"{'ID':8s}", f"{'Animal':10s}", f"{'Name':12s}", f"{'Gender':10s}", f"{'Weight':7s}", f"{'Cell Phone':15s}",
          f"{'Joining Date':10s}")

    for r in cur.fetchall():
        print(f"{str(r[0]):8s}", f"{str(r[1]):10s}", f"{str(r[2]):12s}", f"{str(r[3]):10s}", f"{str(r[4]):7s}",
              f"{str(r[5]):15s}", f"{str(r[6]):10s}")

    # close database connection
    conn.close()

def DisplayDates():
    # connect to sqlite db
    conn = sqlite3.connect('VetData.db')
    # get cursor
    cur = conn.cursor()
    for row in conn.execute('''select Date from Vet'''):
        print(row)

    # close database connection
    conn.close()

# delete animals from a certain date
def DeleteDay(deleteDay):
    # connect to sqlite db
    conn = sqlite3.connect('VetData.db')
    # get cursor
    cur = conn.cursor()
    # query to display all data in the table
    cursor = conn.execute("SELECT * from Vet")
    # display row by row
    for row in cursor:
        print(row)

    conn.execute("DELETE from Vet where Date= (?)", [deleteDay])

    print("After  deleting Date")

    # display row by row
    cursor = conn.execute("SELECT * from Vet")
    for row in cursor:
        print(row)

    # save changes
    conn.commit()

    # close database connection
    conn.close()


# aggregates
def SetSmallAniaml(Animal, Name, Gender, Weight, CellPh, Type):
    SetAnimal(Animal, Name, Gender, Weight, CellPh, None)


def SetAnimal(Animal, Name, Gender, Weight, CellPh, Type, Size):
    Size = Type
    if (Type == 'Small'):
        Record = {
            'stu-Type': Type,
            'stu-Animal': Animal,
            'stu-Name': Name,
            'stu-Gender': Gender,
            'stu-Weight': Weight,
            'stu-CellPh': CellPh,
            'stu-Size': Size
        }
    else:
        Record = {
            'stu-Type': Type,
            'stu-Animal': Animal,
            'stu-Name': Name,
            'stu-Gender': Gender,
            'stu-Weight': Weight,
            'stu-CellPh': CellPh,
        }

    animalNum = getMaxId()
    db.set(genKey(animalNum), Record)


def GetAnimalAttrib(animalNum):
    if (db.exists(genKey(animalNum))):
        record = db.get(genKey(animalNum))
        if (record['stu-Type'] == 'Small'):
            return (
                record['stu-Type'], record['stu-Animal'], record['stu-Name'], record['stu-Gender'],
                record['stu-Weight'],
                record['stu-CellPh'], record['stu-Size'])
        else:
            return (
                record['stu-Type'], record['stu-Animal'], record['stu-Name'], record['stu-Gender'],
                record['stu-Weight'],
                record['stu-CellPh'], None)
    else:
        return None


def GetAnimalDict(animalNum):
    if (db.exists(genKey(animalNum))):
        return (db.get(genKey(animalNum)))
    else:
        return None


def FindSmallAnimal():
    # show all
    AnimalTempNum = str(1)
    # show all
    print(db.getall())

    if (db.exists(genKey(AnimalTempNum))):
        print(GetAnimalDict(AnimalTempNum))
        Type, Animal, Name, Gender, Weight, CellPh, Size = GetAnimalAttrib(AnimalTempNum)
        if (Type == "Small"):
            print("****** ANIMALS *******")
            print(Animal + ": " + Name)
            print("**********************")


def FindLargeAnimal():
    # show all
    AnimalTempNum = str(1)
    # show all
    print(db.getall())

    if (db.exists(genKey(AnimalTempNum))):
        print(GetAnimalDict(AnimalTempNum))
        Type, Animal, Name, Gender, Weight, CellPh, Size = GetAnimalAttrib(AnimalTempNum)
        if (Type == "Large"):
            print("****** ANIMALS *******")
            print(Animal + ": " + Name)
            print("**********************")


def mainApp(hasAnimalInfo):
    # To store user Options
    option = ""

    # get current date
    today = date.today()
    # mm/dd/YY
    d1 = today.strftime("%mm%dd%Y")
    Date = str(d1)

    Registered = False

    # Pet Attributes
    if not hasAnimalInfo:
        # if not in db set to default values
        Animal = ""
        Name = ""
        Gender = ""
        Weight = 0.0
        CellPh = ""
        Type = ""
        Date = str(d1)
    else:
        # if an Animal exists in the DB set to saved values
        Animal, Name, Gender, Weight, CellPh, Type, Date = loadAnimals()

    # now the menu
    while option != "Q":
        # show menu
        print_Menu(hasAnimalInfo, Registered)
        # get option
        option = get_MenuOption()

        if option == "A":
            # edit/Add a Animal
            hasAnimalInfo, Animal, Name, Gender, Weight, CellPh, Type, Date = addAnimal(hasAnimalInfo, Animal,
                                                                                      Name, Gender, Weight,
                                                                                      CellPh, Type, Date)
            Registered = False
            hasAnimalInfo = True
        elif option == "B":
            # display but if there's nothing to display prompt to create
            if not hasAnimalInfo:
                print("You must add an Animal first.")
            else:
                # display animal info
                displayAnimal(Animal, Name, Gender, Weight, CellPh)
        elif option == "C":
            # get option
            print("**********************")
            print("Pick a Day To Delete")
            print("Format: 02m07d2023")
            DisplayDates()

            deleteDay = str(input("Enter Date Here: "))
            print()
            print("*************************************")
            print("Animals with Date: " + deleteDay)
            DeleteDay(deleteDay)

        elif option == "D":
            # delete animal
            if not hasAnimalInfo:
                print("You must add an Animal first.")
            else:
                # delete Animal
                deleteAnimal(Animal, Name, Gender, Weight, CellPh)
                hasAnimalInfo = False

        elif option == "G":
            # Register Animal
            RegAnimal(Animal, Name, Gender, Weight, CellPh, Date)
            SetAnimal(Animal, Name, Gender, Weight, CellPh, Type, Type)
            Registered = True
            hasAnimalInfo = False

        elif option == "H":
            print("Choose Option:")
            print("A) All Animals")
            print("B) Small Animals")
            print("C) Large Animals")
            # get option
            option = get_MenuOption()
            if (option == "A"):
                DisplayAllRegAnimals()
            elif (option == "C"):
                FindLargeAnimal()
            else:
                FindSmallAnimal()

    RemoveAll()

    return hasAnimalInfo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # check to see if there is Animal information
    # in the key value db
    hasAnimalInfo = False
    try:
        if db.get(DictName('AnimalExists')):
            if db.dget(DictName('Animal'), 'Animal'):
                hasAnimalInfo = True
    except:
        hasAnimalInfo = False

    hasAnimalInfo = mainApp(hasAnimalInfo)
    db.dump()
