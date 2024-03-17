import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    FLASK_APP = '__init__.py'
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '2bfb59bfcad871d1e4a67b5a8aa26b3e')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
