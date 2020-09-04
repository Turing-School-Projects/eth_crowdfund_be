# Etherium Crowdfund

## Setup

1. Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [Postgres](https://www.postgresql.org/) on your machine, if you do not have them already
  * To install Pipenv on a Mac, you can run `$ brew install pipenv`
1. Fork and clone down the repository
1. Change into the directory `$ cd eth_crowdfund_be/eth_crowdfund_api`
1. Run `$ pipenv shell` to activate the project virtual environment
1. Run `$ pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt` to install all dependencies
1. Run `$ createdb eth_crowdfund_api_db` to create the app database
1. Run
```
$ export FLASK_ENV=development
$ export JWT_SECRET_KEY=hhgaghhgsdhdhdd
```
 to set the system environment variables  

 You should now be able to run the app:
 1. Run `$ python run.py`
 1. In your browser, navigate to http://localhost:3000/ and you should see `Etherium 4 life`

 ### Database Setup
 1. Delete the `/migrations` directory
 1. Run
 ```
 $ python manage.py db init
 $ python manage.py db migrate
 $ python manage.py db upgrade
 ```
 1. You can check the database by running
 ```
 $ psql eth_crowdfund_api_db
 $ \dt
 ```  
 and you should see `campaigns` and `requests` tables listed.
