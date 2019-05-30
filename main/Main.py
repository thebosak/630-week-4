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
    ResearcherID integer,
    Experiment text)''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('0','EPV Vaccine trial')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('1','Zombie Outbreak')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('2','XYZ thing')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('3','Andromeda Strain')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('4','Basement disease')''')
connection.execute('''INSERT INTO Experiment (ResearcherID, Experiment) VALUES ('5','None')''')
crsr = connection.cursor()
#crsr.execute('select * from Experiment')
crsr.execute('select p.Name, e.Experiment from People as p join Experiment as e where e.ResearcherID == p.PersonID')
rows = crsr.fetchall()
#for row in rows:
#    print (row)
for i in rows:
    print ('Name: %s\n\tExperiment: %s' % (i[0],i[1]))

connection.execute("delete from People where PersonID == '0'")
crsr.execute('select * from People')
rows=crsr.fetchall()
for row in rows:
    print(row)
connection.close()