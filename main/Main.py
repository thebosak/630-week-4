'''
Created on May 28, 2019

@author: Brad Bosak
'''

import sqlite3

connection = sqlite3.connect("C:\\Users\\Brad Bosak\\git\\630-week-4\\database.db")

#Drop tables if they exists to start over
connection.execute('DROP TABLE IF EXISTS People')
connection.execute('DROP TABLE IF EXISTS Experiment')

#Create People table
connection.execute('''CREATE TABLE People(
    PersonID integer,
    Name text,
    Position text,
    Phone text,
    Location text)''')
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('0','Alice','Research Director','555-123-0001','4b')''')
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('1','Bob','Research Assistant','555-123-0002','17')''')
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('2','Charles','Research Assistant','555-123-0003','24')''')
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('3','David','Research Assistant','555-123-0004','8')''')
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('4','Edward','Toadie','None','Basement')''')
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('5','Brad','Captain','555-123-0005','Captains Quarters')''')

#Create Experiment table
connection.execute('''CREATE TABLE Experiment(
    ResearcherID integer,
    Experiment text)''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('0','EPV Vaccine trial')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('1','Zombie Outbreak')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('2','XYZ thing')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('3','Andromeda Strain')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('4','Basement disease')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('5','Strange thing')''')
crsr = connection.cursor()
crsr.execute('SELECT P.Name, E.Experiment FROM People AS P JOIN Experiment AS E WHERE E.ResearcherID == P.PersonID')
rows = crsr.fetchall()
print('Initial researchers and experiments:')
print()
for i in rows:
    print ('Name: %s\n\tExperiment: %s' % (i[0],i[1]))
print()

#Add a new user and experiment to database
connection.execute('''INSERT INTO People (PersonID, Name, Position, Phone, Location) VALUES ('6','Fry','Delivery Boy','555-123-0005','Benders Closet')''')

#Delete Alice from the People table
connection.execute("DELETE FROM People WHERE PersonID == '0'")

#Reassign Alice's experiment to Fry's ID
connection.execute("UPDATE Experiment SET ResearcherID = '6' WHERE ResearcherID == '0'")

#Print experiments and researchers
crsr.execute('SELECT P.Name, E.Experiment FROM People AS P JOIN Experiment AS E where E.ResearcherID == P.PersonID')
rows = crsr.fetchall()
print("After reassigning Alice's experiment:")
print()
for i in rows:
    print ('Name: %s\n\tExperiment: %s' % (i[0],i[1]))
connection.close()