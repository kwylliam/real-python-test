#Cars database

#import sqlite3
import sqlite3

#create the database
conn=sqlite3.connect("cars")

#cursor object
c=conn.cursor()

#create a table
c.execute("""CREATE TABLE inventory
	(make TEXT, model TEXT, quantity INT)""")

#close the database connection
conn.close()
