# All database operation are perform here

import sqlite3

def checklogin(username, password):
    try:
        connection = sqlite3.connect("./bookstore.db")
        cur = connection.cursor()
        cur.execute("select count(*) from users where username=(?) and password=(?);",(username, password))
        count = cur.fetchone()
        if(count[0]==1):
            return True
        else:
            return False
    except:
        return False
    finally:
        connection.close()

def adduser(username, password, phone, address):
    try:
        connection = sqlite3.connect("./bookstore.db")
        cur = connection.cursor()
        count = cur.execute("insert into users (username, password, phone, address) values (?,?,?,?)",(username, password, int(phone), address))

        if(count.rowcount == 1):
            connection.commit()
            return True
        else:
            connection.rollback()
            return False
    except:
        connection.rollback()
        return False
    finally:
        connection.close()

def fetchbooks():
    try:
        connection = sqlite3.connect("./bookstore.db")
        cur = connection.cursor()
        cur.execute("select * from books;")
        data = cur.fetchall()
        return data
    except:
        return None
    finally:
        connection.close()

def fetchorderhistory(username):
    try:
        connection = sqlite3.connect("./bookstore.db")
        cur = connection.cursor()
        cur.execute("select o.username, o.bookname, o.quantity, o.amount, o.date, o.status, i.url from orders o left join books i on o.bookname = i.bookname where o.username=(?)",(username,))
        data = cur.fetchall()
        data = data[::-1]
        return data
    except:
        return None
    finally:
        connection.close()

def addorder(orderid, username, bookname, quantity, amount, date, status):
    try:
        connection = sqlite3.connect("./bookstore.db")
        cur = connection.cursor()
        count = cur.execute("insert into orders (orderid, username, bookname, quantity, amount, date, status) values (?,?,?,?,?,?,?)",(orderid, username, bookname, int(quantity),int(amount),date,status))
       
        if(count.rowcount==1):
          connection.commit()
          return True
        else:
            connection.rollback()
            return False
    except:
        connection.rollback()
        return False
    finally:
        connection.close()


def getcategory():
    try:
        connection = sqlite3.connect("./bookstore.db")
        cur = connection.cursor()
        cur.execute("select distinct category from books;")
        data = cur.fetchall()
        return data
    except:
        return None
    finally:
        connection.close()
        
