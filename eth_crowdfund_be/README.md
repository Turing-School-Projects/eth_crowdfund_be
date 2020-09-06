# Etherium Crowdfund

## Setup

1. Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [Postgres](https://www.postgresql.org/) on your machine, if you do not have them already
  * To install Pipenv on a Mac, you can run `$ brew install pipenv`
2. You should have Python 3.8.5
  ```
  $ python3 --version
  => Python 3.8.5
  ```
3. You should have Postgres
  ```
  $ which psql
  => /Applications/Postgres.app/Contents/Versions/latest/bin/psql
  ```
4. You should have pipenv
  ```
  $ pipenv --version
  => pipenv, version 2020.8.13
  ```
5. Fork and clone down the repository
6. Change into the directory `$ cd eth_crowdfund_be/eth_crowdfund_api`
7. You will need to work in a virtual environment. Why? Using a virtual environment for Python projects allows us to have an isolated working copy of Python so we can work on a specific project without worrying about affecting other projects.
8. Within the `/eth_crowdfund_api` directory:  
 a. Run `# pipenv --three` to create the virtual environment  
 b. Run `$ pipenv shell` to activate the project virtual environment. When you are done working on the project, you should execute `$ exit` to exit the virtual environment  
 c. Run `$ pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt` to install all dependencies  
 d. Run `$ createdb eth_crowdfund_api_db` to create the app database  
 e. Run
 ```
 $ export FLASK_ENV=development  
 $ export JWT_SECRET_KEY=hhgaghhgsdhdhdd
 ```
 to set the system environment variables.
 You should now be able to run the app:  
 9. Run
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
 10. In your browser, navigate to http://localhost:3000/ and you should see `Etherium for life`  
 11. To stop the server, `ctrl + c`

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
 $ psql
 $ \c eth_crowdfund_api_db
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

* Note: If you encounter any root errors, such as `ERROR [root] Error: Target database is not up to date.` or `ERROR [root] Error: Relative revision -1 didn't produce 1 migrations`, run `$ python3 manage.py db stamp head` to reset the target database to your current database head.

## API Endpoints

### Campaigns

#### Create a campaign

* Path: `POST http://localhost:3000/api/v1/campaigns/`
* Example JSON post body:
```
{
    "name": "Test Campaign",
    "description": "test description",
    "image": "test.jpg",
    "contributors": "1",
    "upvote": "2",
    "manager": "3",
    "address": "1",
    "min_contribution": 5.0
}
```
* Example response body:
```
{
    "address": "1",
    "contributors": 1,
    "created_at": "2020-09-06T15:49:49.445152",
    "description": "test description",
    "expiration": null,
    "id": 1,
    "image": "test.jpg",
    "manager": "3",
    "min_contribution": 5.0,
    "name": "Test Campaign",
    "requests": [],
    "updated_at": "2020-09-06T15:49:49.445158",
    "upvote": 2
}
```
#### Get a Campaign by ID number
* Path: `GET http://localhost:3000/api/v1/campaigns/<insert campaign id here>`
* No body required
* Example response body
```
{
    "address": "1",
    "contributors": 1,
    "created_at": "2020-09-06T15:49:49.445152",
    "description": "test description",
    "expiration": null,
    "id": 4,
    "image": "test.jpg",
    "manager": "3",
    "min_contribution": 5.0,
    "name": "Test Campaign",
    "requests": [],
    "updated_at": "2020-09-06T15:49:49.445158",
    "upvote": 2
}
```
