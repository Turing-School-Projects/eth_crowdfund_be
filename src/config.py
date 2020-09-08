import os

class Development(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class Production(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=False

class Testing(object):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_TEST_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=False


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
