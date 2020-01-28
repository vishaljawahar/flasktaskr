import os

# get the folder where this script is placed
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktasr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'b\xec\xc09\x8b\xaaI\xf7\xa7\x1b\xaf\xa7\xf6\xd9"\xf8\xa0\xa9o^\xb2\xbb\x08}\xea\xe6"?*\x16\x92'

# define full path to the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
