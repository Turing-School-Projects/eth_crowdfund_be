import os 
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand 
from src.models import Campaign, Request

from src.app import create_app, db 
from src.seeds.seed import add_seeds

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
  add_seeds()

if __name__ == '__main__':
  manager.run()