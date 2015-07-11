from app.lib.dbc import dbc

class CourseRepository():

    def __init__(self):
        pass


    def getNewestCourse(self):
        db = dbc()
        newestCourseQuery = "SELECT * FROM courses ORDER BY date DESC LIMIT 1"
        result = db.resultDict(newestCourseQuery)
        if result:
            return result[0]
        return False


    def insertCourse(self, userId, title, type):
        db = dbc()
        query = "INSERT INTO courses (author_id, title, type, date) VALUES ({0}, '{1}', '{2}', NOW())".format(userId, title, type)
        db.execute(query)
        id = db.getLastId()
        return id


    def insertDescription(self, courseId, description):
        db=dbc()
        query="UPDATE courses SET description='{0}' WHERE course_id='{1}'".format(description, courseId)
        db.execute(query)


    def insertQuestion(self, courseId, question):
        db=dbc()
        query = "INSERT INTO questions (course_id, question) VALUES ({0}, '{1}')"
        query = query.format(courseId, question)
        db.execute(query)
        questionId=db.getLastId()
        return questionId


    def insertAnswer(self, questionId, answer, correct):
        db=dbc()
        answQuery = "INSERT INTO answers (question_id, answer, correct) VALUES({0}, '{1}', {2})"
        answQuery = answQuery.format(questionId, answer, correct)
        db.execute(answQuery)


    def getQuestions(self, courseId):
        db=dbc()
        questionsQuery = "SELECT question_id, question FROM questions WHERE course_id={0}".format(courseId)
        questions = db.resultDict(questionsQuery)
        return questions


    def getAnswers(self, questionId):
        db=dbc()
        answersQuery = "SELECT answer_id, answer, correct FROM answers WHERE question_id={0}".format(questionId)
        answers = db.resultDict(answersQuery)
        return answers


    def courseTaken(self, userId, courseId):
        db = dbc()
        query="INSERT INTO courses_taken (user_id, course_id, date_log) VALUES({0}, {1}, NOW()) ".format(userId, courseId)
        db.execute(query)

    def getUserData(self, userId):
        db=dbc()        
        query = "SELECT email, username FROM users WHERE user_id={0}".format(userId)
        userData = db.resultDict(query)

        return userData


    def getUserCourses(self, userId):
        db=dbc()
        query = "SELECT title, type, date_log FROM courses_taken as A JOIN courses as B ON A.course_id = B.course_id WHERE user_id={0}".format(userId)
        courses = db.resultDict(query)

        return courses


    def getCourseTypes(self):
        db=dbc()
        query="SELECT type FROM course_types"
        types=db.resultDict(query)
        return types


    def searchCourses(self, courseType):
        db=dbc()
        query="SELECT course_id, title FROM courses WHERE type='{0}'".format(courseType)
        courses=db.resultDict(query)
        return courses


