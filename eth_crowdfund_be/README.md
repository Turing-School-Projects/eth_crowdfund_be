# Etherium Crowdfund

## Setup

1. Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [Postgres](https://www.postgresql.org/) on your machine, if you do not have them already
  * To install Pipenv on a Mac, you can run `$ brew install pipenv`
1. You should have Python 3.8.5
  ```
  $ python3 --version
  => Python 3.8.5
  ```
1. You should have Postgres
  ```
  $ which psql
  => /Applications/Postgres.app/Contents/Versions/latest/bin/psql
  ```
1. You should have pipenv
  ```
  $ pipenv --version
  => pipenv, version 2020.8.13
  ```
1. Fork and clone down the repository
1. Change into the directory `$ cd eth_crowdfund_be/eth_crowdfund_api`
1. You will need to work in a virtual environment. Why? Using a virtual environment for Python projects allows us to have an isolated working copy of Python so we can work on a specific project without worrying about affecting other projects.
  1. Within the `/eth_crowdfund_api` directory:
    1. Run `# pipenv --three` to create the virtual environment
    1. Run `$ pipenv shell` to activate the project virtual environment. When you are done working on the project, you should execute `$ exit` to exit the virtual environment
    1. Run `$ pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt` to install all dependencies
    1. Run `$ createdb eth_crowdfund_api_db` to create the app database
    1. Run
    ```
    $ export FLASK_ENV=development
    $ export JWT_SECRET_KEY=hhgaghhgsdhdhdd
    ```
    to set the system environment variables.
    You should now be able to run the app:
    1. Run
    ```
    $ python3 run.py
    =>  * Serving Flask app "src.app" (lazy loading)
        * Environment: development
        * Debug mode: on
        * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
        * Restarting with stat
        /Users/username/.local/share/virtualenvs/eth_crowdfund_be-TvIDdz62/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py:833: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
        warnings.warn(FSADeprecationWarning(
          * Debugger is active!
          * Debugger PIN: 312-766-617
    ```

    1. In your browser, navigate to http://localhost:3000/ and you should see `Etherium for life`
    1. To stop the server, `ctrl + c`

### Database Setup
Path: `eth_crowdfund_be/eth_crowdfund_api`

 1. Delete the `/migrations` directory
 1. Run
 ```
 $ python3 manage.py db init
 $ python3 manage.py db migrate
 $ python3 manage.py db upgrade
 ```
 1. You can check the database by running
 ```
 $ psql eth_crowdfund_api_db
 $ \dt
 => List of relations
    Schema |      Name       | Type  |  Owner
    --------+-----------------+-------+----------
    public | alembic_version | table | postgres
    public | campaigns       | table | postgres
    public | requests        | table | postgres

 $ SELECT * FROM campaigns;
 => id | name | description | image | manager | contributors | upvote | min_contribution | address | expiration | created_at | updated_at
    ----+------+-------------+-------+---------+--------------+--------+------------------+---------+------------+------------+------------

 $ SELECT * FROM requests;
 => id | campaign_id | description | image | value | recipient | approved | finalized | approvals | created_at | updated_at
    ----+-------------+-------------+-------+-------+-----------+----------+-----------+-----------+------------+------------
 ```
 and you should see `campaigns` and `requests` tables listed.
 1. To exit the database, `$ exit`

### Database Updates
Path: `eth_crowdfund_be/eth_crowdfund_api`  
To make updates to the database and run a new migration, do the following:

1. `$ python3 manage.py db downgrade`
1. You should delete the migration if you are making a change.
1. `$ python3 manage.py db migrate`
1. `$ python3 manage.py db upgrade`
