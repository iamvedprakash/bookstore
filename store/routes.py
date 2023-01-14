from flask import Flask, json, session, redirect, url_for, request, render_template
from store import app
from datetime import date
import random
from store import dboperations


items = dboperations.fetchbooks()
items = json.dumps(items)
categories = dboperations.getcategory()
categories = json.dumps(categories)


@app.route("/", methods=['POST','GET'])
@app.route("/login", methods=['POST','GET'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            status = dboperations.checklogin(username, password)
            if status:
                session['username']=username
                return redirect(url_for('home'))
            else:
                return render_template('login.html', items=items, categories=categories, logginerror=1)
        else:
            return render_template('login.html', items=items, categories=categories, logginerror=0)


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        if request.method=='POST':
            username   = request.form['username']
            phone      = request.form['phone']
            address    = request.form['address']
            password   = request.form['password']
            confirm_password = request.form['confirm_password']
            if not phone.isnumeric() or (password != confirm_password):   
                return render_template('signup.html', items=items, categories=categories, signuperror=1)
            else:
                status = dboperations.adduser(username, password, phone, address)
                if status:
                    session['username'] = username
                    return redirect(url_for('home'))
                else:  
                    return render_template('signup.html', items=items, categories=categories, signuperror=2)
        else:
            return render_template('signup.html', items=items, categories=categories, signuperror=0)


@app.route("/home", methods=['POST', 'GET'])
def home():
    if 'username' in session:
        if request.method=='POST':
            orderlist = request.get_json()
            today_date = str(date.today())
            orderid = str(random.randint(1000,9999))

            for data in orderlist.values():
                dboperations.addorder(orderid, session['username'], data['bookname'], data['quantity'], data['amount'], today_date, 'Placed')
            
            return redirect(url_for('home'))
        else:
            return render_template('home.html', items=items, categories=categories)
    else:
        return redirect(url_for('login'))


@app.route("/orders")
def orders():
    if 'username' in session:
        orders = dboperations.fetchorderhistory(session['username'])
        orders = json.dumps(orders)
        return render_template('order.html', orders=orders)
    else:
        return redirect(url_for('login'))
