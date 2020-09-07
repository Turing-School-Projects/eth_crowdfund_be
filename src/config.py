import os
import psycopg2


class Development(object):
  DEBUG = True
  TESTING = False
  # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class Production(object):
  DEBUG = True
  TESTING = False
  # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
  # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class Testing(object):
  TESTING = True
  # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_TEST_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=False


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
