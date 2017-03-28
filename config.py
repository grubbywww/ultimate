import os
CSRF_ENABLED = True
SECRET_KEY = 'you-never-success'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'repo')
