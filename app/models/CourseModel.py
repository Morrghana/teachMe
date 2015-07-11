from app.repositories.CourseRepository import CourseRepository
from flask import request

class CourseModel():

    def __init__(self):
        pass


    def getNewestCourse(self):
        courseRepo=CourseRepository()
        result=courseRepo.getNewestCourse()
        newest=''
        title=''
        if result:
            title=result['title']
            newest = "/takeCourse?id={0}&title={1}".format(result['course_id'], result['title'])
        data={'url':newest, 'title':title}
        return data


    def addCourse(self, userId, title, type):
        courseRepo=CourseRepository()
        id=courseRepo.insertCourse(userId=userId, title=title, type=type)
        return id


    def createCourse(self, courseId, count):
        courseRepo = CourseRepository()
        description = request.form['description']
        courseRepo.insertDescription(courseId=courseId, description=description)
        for i in range(1, count + 1):
            key = 'questions[{0}]'.format(i)
            question_data = request.form.getlist(key)
            questionId=courseRepo.insertQuestion(courseId=courseId, question=question_data[0])

            answer = request.form.getlist('answers[{0}]'.format(i))
            for j in range(1, len(question_data)):
                isCorrect = 0
                if int(answer[0]) == j:
                    isCorrect = 1
                    courseRepo.insertAnswer(questionId=questionId, answer=question_data[j], correct=isCorrect)


    def getCourse(self, courseId):
        courseRepo=CourseRepository()
        questions=courseRepo.getQuestions(courseId=courseId)

        result = {}
        for arr in questions:
            result[arr['question_id']] = {}
            result[arr['question_id']]['question'] = arr['question']

            answers=courseRepo.getAnswers(arr['question_id'])

            i = 1;
            for answer in answers:
                result[arr['question_id']]["answer{0}".format(i)] = answer['answer']
                result[arr['question_id']]["correct{0}".format(i)] = answer['correct']
                i = i+1

        return result 


    def finishCourse(self, userId, courseId):
        courseRepo=CourseRepository()
        courseRepo.courseTaken(userId, courseId)


    def getUserData(self, userId):
        courseRepo=CourseRepository()
        userData=courseRepo.getUserData(userId=userId)
        return userData        


    def getUserCourses(self, userId):
        courseRepo=CourseRepository()
        userCourses=courseRepo.getUserCourses(userId=userId)
        return userCourses


    def getCourseTypes(self):
        courseRepo=CourseRepository()
        types=courseRepo.getCourseTypes()
        return types


    def searchCourses(self, courseType):
        courseRepo=CourseRepository()
        courses=courseRepo.searchCourses(courseType=courseType)
        return courses