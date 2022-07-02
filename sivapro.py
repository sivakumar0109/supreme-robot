import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

alex = connection.cursor()
alex.execute("CREATE TABLE IF NOT EXISTS Movies( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
alex.execute("INSERT INTO Movies VALUES('Beast','Vijay','Pooja Hegde','Nelson Dilipkumar',2022)")
alex.execute("INSERT INTO Movies VALUES('Mersal','Vijay','Samantha','Atlee',2017)")
alex.execute("INSERT INTO Movies VALUES('Bigil','Vijay','Nayanthara','Atlee',2019)")
alex.execute("INSERT INTO Movies VALUES('Theri','vijay','Samantha','Atlee',2016)")
alex.execute("INSERT INTO Movies VALUES('Sarkar','vijay','Keerthy Suresh','A R Murugadoss',2018)")

# Printing all the elements of the database
print("ALL RECORDS IN THE DATABASE TABLE")
allMovies = alex.execute("SELECT * FROM Movies").fetchall()
for m in allMovies:
  title,actor,actress,director,releasedYear = m
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))


# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("\n\n\nSELECTED VIJAY ACTING MOVIES")
actorQuery = alex.execute("SELECT * FROM Movies WHERE ACTOR = 'vijay'").fetchall()
for m in actorQuery:
  title,actor,actress,director,releasedYear = m
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
