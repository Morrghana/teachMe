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
    else:
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
        db = dbc()
        newestCourseQuery = "SELECT * FROM courses ORDER BY date DESC LIMIT 1"
        result = db.resultDict(newestCourseQuery)
        result = result[0]
        # pprint(result)
        newest = ''
        if result:
            newest = "/takeCourse?id={0}&title={1}".format(result['course_id'], result['title'])
        
        return render_template("courses.html", newUrl=newest, newTitle=result['title'])

    return redirect(url_for('login'))


@teachMeApp.route("/courses", methods=['POST'])
def startCreateCourses():
    name = request.form['name']
    count = request.form['questions']
    courseType = request.form['type']

    db = dbc()
    query = "INSERT INTO courses (author_id, title, type, date) VALUES ({0}, '{1}', '{2}', NOW())".format(session['userId'], name, courseType)
    db.execute(query)
    id = db.getLastId()

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
    data = dict(request.form)
    db = dbc()
    course_id = int(request.args.get('courseId'))
    count = int(request.args.get('count'))

    for i in range(1, count + 1):
        key = 'questions[{0}]'.format(i)
        question_data = request.form.getlist(key)
        query = "INSERT INTO questions (course_id, question) VALUES ({0}, '{1}')"
        query = query.format(course_id, question_data[0])
        db.execute(query)
        question_id = db.getLastId()

        answer = request.form.getlist('answers[{0}]'.format(i))
        for j in range(1, len(question_data)):
            isCorrect = 0
            if int(answer[0]) == j:
                isCorrect = 1
            answQuery = "INSERT INTO answers (question_id, answer, correct) VALUES({0}, '{1}', {2})"
            answQuery = answQuery.format(question_id, question_data[j], isCorrect)
            db.execute(answQuery)

    return redirect(url_for("courses"))


@teachMeApp.route("/takeCourse", methods=['GET'])
def openCourse():
    db = dbc()
    id = request.args.get("id")
    title = request.args.get("title")
    questionsQuery = "SELECT question_id, question FROM questions WHERE course_id={0}".format(id)
    questions = db.resultDict(questionsQuery)

    result = {}
    for arr in questions:
        result[arr['question_id']] = {}
        result[arr['question_id']]['question'] = arr['question']

        answersQuery = "SELECT answer_id, answer, correct FROM answers WHERE question_id={0}".format(arr['question_id'])
        answers = db.resultDict(answersQuery)

        i = 1;    
        for answer in answers:
            result[arr['question_id']]["answer{0}".format(i)] = answer['answer']
            result[arr['question_id']]["correct{0}".format(i)] = answer['correct']
            i = i+1

    return render_template('/loadCourse.html', courseData=result, id=id, title=title)


@teachMeApp.route("/takeCourse", methods=['POST'])
def finishCourse():
    db = dbc()
    courseId = request.args.get('id')
    query="INSERT INTO courses_taken (user_id, course_id, date_log) VALUES({0}, {1}, NOW()) ".format(session['userId'], courseId)
    db.execute(query)
    # return json.dumps({'html':request.form})
    return redirect(url_for('courses'))


@teachMeApp.route("/profile")
def viewProfile():
    id=session['userId']
    db = dbc()
    query = "SELECT email, username FROM users WHERE user_id={0}".format(id)
    userData = db.resultDict(query)

    query = "SELECT title, type, date_log FROM courses_taken as A JOIN courses as B ON A.course_id = B.course_id WHERE user_id={0}".format(id)
    courses = db.resultDict(query)
    # return json.dumps({'html':courses})
    return render_template("profile.html", userData=userData, courses=courses)