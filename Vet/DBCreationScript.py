import sqlite3
conn = sqlite3.connect('VetData.db')
cur = conn.cursor()

conn.execute('''Drop table if exists Vet''')

# commit and save changes to database
conn.commit()

# create table in database
cur.execute('''CREATE TABLE Vet(
Animal_ID INTEGER PRIMARY KEY NOT NULL,
Animal TEXT ,
AnimalName TEXT ,
Gender TEXT ,
Weight REAL ,
CellPh TEXT ,
Date TEXT);
''')

# commit and save changes to database
conn.commit()

# insert
cur.execute('''Insert Into Vet ('Animal_ID', 'Animal',
'AnimalName', 'Gender', 'Weight', 'CellPh', 'Date')
Values (1006, 'CAT', 'Charlie', 'Male', 10.0, '352-789-1600', '01/10/2023');''')


# commit and save changes to database
conn.commit()

cur.execute('''Select * from Vet;''')
print(cur.fetchall())


# close database connection
conn.close()
print('Connection closed.')

