import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, '../data-dev.sqlite')

DEBUG = True
SECRET_KEY = 'you should change this!'
JSONIFY_PRETTYPRINT_REGULAR = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + db_path
