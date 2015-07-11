from flask import Flask
from config import config

teachMeApp = Flask(__name__)
import app.routes

teachMeApp.secret_key = config['appSecret']

if __name__ == "__main__":
    teachMeApp.run(debug=True)
