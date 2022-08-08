import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.environ["APP_NAME"]

FLASK_ENV = os.environ["FLASK_ENV"] 
FLASK_RUN_PORT =  os.environ["FLASK_RUN_PORT"]
FLASK_DEBUG =  os.environ["FLASK_DEBUG"]
APP_SECRET_KEY =  os.environ["APP_SECRET_KEY"]

PATH_LOGIN_API = 'login/'

PATH_API_BACKEND = 'http://127.0.0.1:5000/'

