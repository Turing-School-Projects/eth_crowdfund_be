import os
from src.seeds.seed import add_seeds
from src.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  app = create_app(env_name)
  # run app
  app.run(port=3000)

  with app.app_context():
    add_seeds()