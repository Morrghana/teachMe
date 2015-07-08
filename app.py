from flask import Flask
from config import config

teachMeApp = Flask(__name__)
teachMeApp.secret_key = config['appSecret']
import app.routes

if __name__=="__main__":
    teachMeApp.run(debug=True)