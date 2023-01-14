import sqlite3
import pandas

#df = pandas.read_excel("./Books.xlsx")
#data = df.values.tolist()


connection = sqlite3.connect("./bookstore.db")
cur = connection.cursor()

#for d in data:
#cur.execute("DELETE FROM orders;")

#connection.commit()

print(cur.execute("select * from books;").fetchall())

connection.close()


#CREATE TABLE users (userid integer primary key autoincrement, username varchar unique, password varchar, phone integer unique, address varchar);

#CREATE TABLE books (bookid integer primary key autoincrement, bookname varchar unique, category varchar, price integer, description varchar, url varchar);

#CREATE TABLE orders (orderid varchar, username varchar, bookname varchar, quantity integer, amount integer, date varchar, status varchar);
