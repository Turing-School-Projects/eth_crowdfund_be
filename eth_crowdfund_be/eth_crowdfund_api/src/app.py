from flask import Flask

from .config import app_config
from .models import db

from .views.CampaignView import campaign_api as campaign_blueprint
from .views.RequestView import request_api as request_blueprint


def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  db.init_app(app)

  app.register_blueprint(campaign_blueprint, url_prefix='/api/v1/campaigns')
  app.register_blueprint(request_blueprint, url_prefix='/api/v1/requests')


  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Etherium for life'

  return app
