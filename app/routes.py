from flask import Flask, render_template, json, request, redirect, url_for, session
from __main__ import teachMeApp

import pymysql
from pprint import pprint
from app.lib.dbc import dbc

@teachMeApp.route("/")
def main():
    return render_template("home.html")


@teachMeApp.route("/signUp")
def showSignUp():
    return render_template("signup.html")


@teachMeApp.route("/signUp", methods=['POST'])
def signUp():
    _name = request.form['name']
    _email = request.form['email']
    _password = request.form['password']

    if _name and _email and _password:
        db = dbc()

        selectQuery = "SELECT username, email FROM users WHERE username='{0}' OR email='{1}'".format(_name, _email)
        result = dict(db.resultTuple(selectQuery))
        usersCount = len(result)

        if usersCount == 0:
            query = "INSERT INTO users (username, email, password) VALUES('{0}', '{1}', '{2}')".format(_name, _email, _password)
            db.execute(query)
            session['email'] = _email
            return redirect(url_for("courses"))

    return render_template("signup.html")
        # return json.dumps({'html':pprint(result)})
    # return json.dumps({'html':resLen})


@teachMeApp.route("/login")
def showLogin():
    return render_template("login.html")


@teachMeApp.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email and password:
        db = dbc()
        query = "SELECT user_id, role FROM users WHERE email = '{0}' AND password = '{1}'".format(email, password)
        result = db.resultDict(query)

        if result:
            # return redirect(request.args.get("courses"))
            session['userId'] = result[0]['user_id']
            session['email'] = email
            session['role'] = result[0]['role']

            return redirect(url_for("courses"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    # return json.dumps({'html':pprint(result[0])})


@teachMeApp.route("/courses")
def courses():
    if "email" in session:
        return render_template("courses.html")

    return redirect(url_for('login'))


@teachMeApp.route("/courses", methods=['POST'])
def startCreateCourses():
    name = request.form['name']
    count = request.form['questions']
    courseType = request.form['type']

    db = dbc()
    query = "INSERT INTO courses (author_id, title, type) VALUES ({0}, '{1}', '{2}')".format(session['userId'], name, courseType)
    db.execute(query)
    id = db.getLastId()

    if name and count and courseType:
        return redirect(url_for("openCreateCourseForm", name=name, count=count, id=id))
        # return redirect(url_for('/createCourse?name=' + name + '&count=' + count + '&type=' + courseType))

    return render_template("courses.html")
        

@teachMeApp.route("/createCourse", methods=['GET'])
def openCreateCourseForm():
    count = int(request.args.get('count'))
    name = request.args.get('name')
    id = request.args.get('id')

    return render_template("createCourse.html", name=name,count=count, id=id)


@teachMeApp.route("/createCourse", methods=['POST'])
def createCourse():
    data = dict(request.form)


    return json.dumps({'html':print(data)})
    # return json.dumps({'html':print(request.values)})
    return render_template("courses.html")


@teachMeApp.route("/addQuestion", methods=["POST"])
def addQuestion():
    data = dict(request.form)
    # return json.dumps({'html':print(data)})
    # id = request.args.get(id)
    # return json.dumps({'html':id})

    return render_template("createCouse.html")