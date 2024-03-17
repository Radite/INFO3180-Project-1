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
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # get the directory of the project root
    UPLOAD_FOLDER = os.path.normpath(os.path.join(BASE_DIR, os.environ.get('UPLOAD_FOLDER')))
    # Print the base directory and upload folder path
    print("Base Directory:", BASE_DIR)
    print("Upload Folder Path:", UPLOAD_FOLDER)