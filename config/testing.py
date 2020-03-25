import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, '../data-test.sqlite')

DEBUG = False
TESTING = True
SECRET_KEY = 'you should change this!'
SERVER_NAME = 'example.com'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
