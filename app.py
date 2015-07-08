from flask import Flask

teachMeApp = Flask(__name__)
import app.routes

if __name__=="__main__":
    teachMeApp.run(debug=True)