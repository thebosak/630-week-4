'''
Created on May 28, 2019

@author: Brad Bosak
'''

import sqlite3

connection = sqlite3.connect("C:\\Users\\Brad Bosak\\git\\630-week-4\\database.db")
connection.execute('drop table if exists People')
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
connection.execute('''CREATE TABLE Experiment(
    Researcher text,
    Experiment text)''')
connection.execute('''INSERT INTO Experiment (Researcher, Experiment) VALUES ('Alice','EPV Vaccine trial')''')
connection.execute('''INSERT INTO Experiment (Researcher, Experiment) VALUES ('Bob','Zombie Outbreak')''')
connection.execute('''INSERT INTO Experiment (Researcher, Experiment) VALUES ('Charles','XYZ thing')''')
connection.execute('''INSERT INTO Experiment (Researcher, Experiment) VALUES ('Edward','Basement disease')''')
connection.execute('''INSERT INTO Experiment (Researcher, Experiment) VALUES ('Brad','None')''')
crsr = connection.cursor()
#crsr.execute('select * from Experiment')
crsr.execute('select p.Name, e.Experiment from People as p join Experiment as e where e.Researcher == p.Name')
rows = crsr.fetchall()
for row in rows:
    print (row)
connection.close()