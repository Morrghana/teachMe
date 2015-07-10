from flask import Flask, render_template, json, request, redirect, url_for, session
from __main__ import teachMeApp

import pymysql
from pprint import pprint
from app.lib.dbc import dbc
from app.models.UserModel import UserModel
from app.models.CourseModel import CourseModel

@teachMeApp.route("/")
def main():
    return render_template("home.html")


@teachMeApp.route("/signUp")
def showSignUp():
    return render_template("signup.html")


@teachMeApp.route("/signUp", methods=['POST'])
def signUp():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if name and email and password:
        model=UserModel()
        hasUser = model.checkUser(name=name, email=email)
        
        if hasUser:
            model.createUser(name=name, email=email, password=password)
            session['email'] = email
            return redirect(url_for("courses"))
    else:
        return render_template("signup.html")

@teachMeApp.route("/login")
def showLogin():
    return render_template("login.html")


@teachMeApp.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    model=UserModel()

    if email and password:
        result=model.checkAndGetUserInfo(email=email, password=password)

        if result:
            session['userId'] = result['user_id']
            session['email'] = email
            session['role'] = result['role']

            return redirect(url_for("courses"))

    return render_template("login.html")


@teachMeApp.route("/courses")
def courses():
    if "email" in session:
        model=CourseModel()
        result=model.getNewestCourse()
        
        return render_template("courses.html", newUrl=result["url"], newTitle=result['title'])

    return redirect(url_for('login'))


@teachMeApp.route("/courses", methods=['POST'])
def startCreateCourses():
    name = request.form['name']
    count = request.form['questions']
    courseType = request.form['type']

    model=CourseModel()
    id=model.addCourse(userId=session['userId'], title=name, type=courseType)

    if name and count and courseType:
        return redirect(url_for("openCreateCourseForm", name=name, count=count, id=id))

    return render_template("courses.html")


@teachMeApp.route("/createCourse", methods=['GET'])
def openCreateCourseForm():
    count = int(request.args.get('count'))
    name = request.args.get('name')
    id = request.args.get('id')

    return render_template("createCourse.html", name=name, count=count, id=id)


@teachMeApp.route("/createCourse", methods=['POST'])
def createCourse():
    course_id = int(request.args.get('courseId'))
    count = int(request.args.get('count'))

    model=CourseModel()
    model.createCourse(courseId=course_id, count=count)

    return redirect(url_for("courses"))


@teachMeApp.route("/takeCourse", methods=['GET'])
def openCourse():
    id = request.args.get("id")
    title = request.args.get("title")
    model=CourseModel()
    result=model.getCourse(courseId=id)

    return render_template('/loadCourse.html', courseData=result, id=id, title=title)


@teachMeApp.route("/takeCourse", methods=['POST'])
def finishCourse():
    model=CourseModel()
    courseId = request.args.get('id')
    model.finishCourse(session['userId'], courseId)

    return redirect(url_for('courses'))


@teachMeApp.route("/profile")
def viewProfile():
    id=session['userId']
    model=CourseModel()

    userData=model.getUserData(userId=id)
    courses=model.getUserCourses(userId=id)

    return render_template("profile.html", userData=userData, courses=courses)

