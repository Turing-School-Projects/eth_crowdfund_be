from flask import Flask
from dotenv import load_dotenv # importing dotenv
load_dotenv(override=True) # loading the environment variables at app startup and overriding any existing system variables

from .config import app_config
from .models import db

from .views.CampaignView import campaign_api as campaign_blueprint
from .views.RequestView import request_api as request_blueprint
from flask_cors import CORS, cross_origin


def create_app(env_name):
  # app initiliazation
  app = Flask(__name__)

  cors = CORS(app)
  app.config['CORS_HEADERS'] = 'Content-Type'

  app.config.from_object(app_config[env_name])

  db.init_app(app)
  # db.create_tables()

  app.register_blueprint(campaign_blueprint, url_prefix='/api/v1/campaigns')
  app.register_blueprint(request_blueprint, url_prefix='/api/v1/requests')


  @app.route('/', methods=['GET'])
  def index():
    return 'Etherium for life'

  return app
  @app.route('/travis', methods=['GET'])
  def index():
    return 'travis deployed? YES'

  return app

