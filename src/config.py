import os

class Development(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  MAIL_SERVER = 'smtp.sendgrid.net'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'apikey'
  MAIL_PASSWORD = os.getenv('SENDGRID_API_KEY')
  MAIL_DEFAULT_SENDER = "etho@ethoboost.com"

class Production(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  MAIL_SERVER = 'smtp.sendgrid.net'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'apikey'
  MAIL_PASSWORD = os.getenv('SENDGRID_API_KEY')
  MAIL_DEFAULT_SENDER = "etho@ethoboost.com"

class Testing(object):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_TEST_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS=False


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
