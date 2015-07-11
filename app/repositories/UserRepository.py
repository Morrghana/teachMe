from app.lib.dbc import dbc


class UserRepository():

    def __init__(self):
        pass

    def checkUser(self, name, email):
        db = dbc()

        selectQuery = "SELECT username, email FROM users WHERE username='{0}' OR email='{1}'".format(name, email)
        result = dict(db.resultTuple(selectQuery))
        usersCount = len(result)
        return usersCount

    def createUser(self, name, email, password):
        db = dbc()
        query = "INSERT INTO users (username, email, password) VALUES('{0}', '{1}', '{2}')".format(name, email, password)
        db.execute(query)

    def getUserInfo(self, email, password):
        db = dbc()
        query = "SELECT user_id, role FROM users WHERE email = '{0}' AND password = '{1}'".format(email, password)
        result = db.resultDict(query)
        return result
