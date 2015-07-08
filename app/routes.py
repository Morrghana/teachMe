from flask import Flask, render_template, json, request, redirect, url_for
from __main__ import teachMeApp
import pymysql
from pprint import pprint
from app.DB_connect import DB_connect

@teachMeApp.route("/")
def main():
    return render_template("home.html")

  
@teachMeApp.route("/showSignUp")
def showSignUp():
    return render_template("signup.html")

    
@teachMeApp.route("/signUp", methods=['POST'])
def signUp():
    _name = request.form['name']
    _email = request.form['email']
    _password = request.form['password']
    
    if _name and _email and _password:
        db = DB_connect()

        selectQuery = "SELECT username, email FROM users WHERE username='{0}' OR email='{1}'".format(_name, _email)
        result = dict(db.resultTuple(selectQuery))
        usersCount = len(result)

        if usersCount == 0:
            query = "INSERT INTO users (username, email, password) VALUES('{0}', '{1}', '{2}')".format(_name, _email, _password)
            db.execute(query)

        return render_template("signup.html")
        # return json.dumps({'html':pprint(result)})  
    # return json.dumps({'html':resLen})


@teachMeApp.route("/showLogin")
def showLogin():
    return render_template("login.html")


@teachMeApp.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email and password:
        db = DB_connect()
        query = "SELECT count(*) FROM users WHERE email = '{0}' AND password = '{1}'".format(email, password)
        result = db.resultSingle(query)

        if result[0] == 1:
            # return redirect(request.args.get("courses"))
            return redirect(url_for("courses"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")    
    # return json.dumps({'html':pprint(result[0])})


@teachMeApp.route("/courses")
def courses():
    return render_template("courses.html")