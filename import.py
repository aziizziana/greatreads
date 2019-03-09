"""Program to import the books.csv into your postgres database"""

import os, csv, psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(host="localhost",database="bookreview", user="postgres", password="ziana")

csvfile = open("books.csv") 
reader = csv.reader(csvfile,delimiter=',')
print("Creating books table!")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS books ( id SERIAL PRIMARY KEY, \
								   isbn VARCHAR NOT NULL, \
								   title VARCHAR NOT NULL, \
								   author VARCHAR NOT NULL, \
								   year VARCHAR NOT NULL );")

print("Created!")
2
print("Adding books to table.")

for isbn, title, author, year in reader:
	cur.execute("INSERT INTO books (isbn, title, author, year) VALUES (%s, %s, %s, %s)",(isbn,title,author,year))

conn.commit()
print("Insert Completed!")