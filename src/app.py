from flask import Flask
from dotenv import load_dotenv # importing dotenv
load_dotenv(override=True) # loading the environment variables at app startup and overriding any existing system variables

from .config import app_config
from .models import db

from .views.CampaignView import campaign_api as campaign_blueprint
from .views.RequestView import request_api as request_blueprint
from .views.PriceConverter import price_converter_api as price_converter_blueprint
from .views.ContributorView import contributor_api as contributor_blueprint
from .views.ApiKeyView import api_key_api as api_key_blueprint
from flask_cors import CORS, cross_origin


def create_app(env_name):
  # app initiliazation
  app = Flask(__name__)

  cors = CORS(app)
  app.config['_HEADERS'] = 'Content-Type'

  app.config.from_object(app_config[env_name])

  db.init_app(app)
  app.register_blueprint(campaign_blueprint, url_prefix='/api/v1/campaigns')
  app.register_blueprint(request_blueprint, url_prefix='/api/v1/requests')
  app.register_blueprint(price_converter_blueprint, url_prefix='/api/v1/price_converter')
  app.register_blueprint(contributor_blueprint, url_prefix='/api/v1/contributor')
  app.register_blueprint(api_key_blueprint, url_prefix='/api/v1/api_key')

  @app.route('/', methods=['GET'])
  def index():
    message = {'About': 'Welcome to the Etho Boost backend', 
              'All Campaigns': 'GET: /api/v1/campaigns/', 
              'Create Campaign': 'POST: /api/v1/campaigns/', 
              'Update Campaign': 'PUT: /api/v1/campaigns/<campaign_id>',
              'Campaign by ID': 'GET: /api/v1/campaigns/<campaign_id>',
              'All Requests': 'GET: /api/v1/requests/', 
              'Create Request': 'POST: /api/v1/requests/', 
              'Update Request': 'PUT: /api/v1/requests/<request_id>',
              'Request by ID': 'GET: /api/v1/requests/<request_id>',
              'Create Contributor': 'POST: /api/v1/contributor/', 
              'Update Contributor': 'PUT: /api/v1/contributor/<contributor_id>', 
              'Contributor by contributor id': 'GET: /api/v1/contributor/<contributor_id>', 
              'Price Conversion': 'GET: /api/v1/price_converter_api/?wei=<wei_amount>`',
              }
    return message

  return app
