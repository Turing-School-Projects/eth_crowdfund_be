import os
from src.seeds.seed import add_seeds
from src.app import create_app

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
  port = os.getenv('PORT')
  # run app
  app.run(host='0.0.0.0', port=port)

  with app.app_context():
    add_seeds()
