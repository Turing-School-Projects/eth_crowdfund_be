# Etherium Crowdfund
## Setup
<details><summary> Setup </summary>

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
6. Change into the directory `$ cd eth_crowdfund_be`
7. You will need to work in a virtual environment. Why? Using a virtual environment for Python projects allows us to have an isolated working copy of Python so we can work on a specific project without worrying about affecting other projects.
8. Within the `/eth_crowdfund_be` directory:  
 a. Run `# pipenv --three` to create the virtual environment  
 b. Run `$ pipenv shell` to activate the project virtual environment. When you are done working on the project, you should execute `$ exit` to exit the virtual environment  
 c. Run `$ pipenv install` to install all dependencies from pipfile
 d. Run `$ createdb eth_crowdfund_api_db` to create the app database  
 e. Add a .env file inside of src containing 
 ```
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI="postgresql://postgres:password@localhost/eth_crowdfund_api_db"
SQLALCHEMY_TEST_DATABASE_URI="postgresql://postgres:password@localhost/eth_crowdfund_api_db_test"
PORT=3000
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
</details> 

<details><summary> Database Setup </summary> 
 
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
 
 ### Seeding the Database
 Within the `pipenv shell` virtual environment, do the following:
 1. Ensure you are at `/eth_crowdfund_be`
 2. Run `$ python3 run.py --seed=True`
 3. Visit `localhost:3000/api/v1/campaigns` and `localhost:3000/api/v1/requests` and you should see seeded Campaigns and Requests.

### Database Updates
Path: `eth_crowdfund_be/eth_crowdfund_api`  
To make updates to the database and run a new migration, do the following:

1. `$ python3 manage.py db downgrade`
1. You should delete the migration if you are making a change.
1. `$ python3 manage.py db migrate`
1. `$ python3 manage.py db upgrade`

* Note: If you encounter any root errors, such as `ERROR [root] Error: Target database is not up to date.` or `ERROR [root] Error: Relative revision -1 didn't produce 1 migrations`, run `$ python3 manage.py db stamp head` to reset the target database to your current database head.

</details> 

## API Endpoints

<details><summary> Campaigns </summary> 

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
#### Get all Campaigns
* Path: `GET http://localhost:3000/api/v1/campaigns`
* No body required
* Example response body
```
[
    {
        "address": "4",
        "contributors": 1,
        "created_at": "2020-09-05T20:31:17.196051",
        "description": "test description",
        "expiration": null,
        "id": 1,
        "image": "test.jpg",
        "manager": "3",
        "min_contribution": 5.0,
        "name": "Test Campaign",
        "requests": [
            {
                "approvals": 1,
                "approved": false,
                "campaign_id": 1,
                "created_at": "2020-09-05T20:41:47.774790",
                "description": "test description",
                "finalized": false,
                "id": 1,
                "image": "test.jpg",
                "recipient": "1",
                "updated_at": "2020-09-05T20:41:47.774800",
                "value": 1.0
            }
        ],
        "updated_at": "2020-09-05T20:31:17.196090",
        "upvote": 2
    },
    {
        "address": "2",
        "contributors": 2,
        "created_at": "2020-09-06T16:59:05.367795",
        "description": "test description b",
        "expiration": null,
        "id": 5,
        "image": "test_b.jpg",
        "manager": "1",
        "min_contribution": 5.0,
        "name": "Test Campaign B",
        "requests": [],
        "updated_at": "2020-09-06T16:59:05.367801",
        "upvote": 5
    }
]
```
#### Update a Campaign by ID number
* Path: `PUT http://localhost:3000/api/v1/campaigns/<insert campaign id here>`
* Example JSON put body
```
{
    "description": "test description updated",
    "name": "Better Name Campaign",
    "upvote": 4
}
```
* Example response body
```
{
    "address": "1",
    "contributors": 1,
    "created_at": "2020-09-06T15:49:49.445152",
    "description": "test description updated",
    "expiration": null,
    "id": 4,
    "image": "test.jpg",
    "manager": "3",
    "min_contribution": 5.0,
    "name": "Better Name Campaign",
    "requests": [],
    "updated_at": "2020-09-06T16:48:19.902997",
    "upvote": 4
}
```
#### Delete a Campaign by ID number
* Path: `DELETE http://localhost:3000/api/v1/campaigns/<insert campaign id here>`
* No body required
* Example response body
```
{
    "address": "1",
    "contributors": 1,
    "created_at": "2020-09-06T15:49:49.445152",
    "description": "test description updated",
    "expiration": null,
    "id": 4,
    "image": "test.jpg",
    "manager": "3",
    "min_contribution": 5.0,
    "name": "Better Name Campaign",
    "requests": [],
    "updated_at": "2020-09-06T16:48:19.902997",
    "upvote": 4
}
```
</details> 

<details><summary> Requests </summary>
 
#### Create a Request
* Path `POST http://localhost:3000/api/v1/requests/`
* Example JSON post body. `campaign_id`, `value`, and `recipient` are required.
```
{
    "campaign_id": "1",
    "description": "test description a",
    "image": "request.jpg",
    "value": 1.0,
    "recipient": "1"
}
```
* Example response body
```
{
    "approvals": null,
    "approved": false,
    "campaign_id": 1,
    "created_at": "2020-09-06T17:11:23.639004",
    "description": "test description a",
    "finalized": false,
    "id": 2,
    "image": "request.jpg",
    "recipient": "1",
    "updated_at": "2020-09-06T17:11:23.639042",
    "value": 1.0
}
```
#### Get a Request by ID number
* Path: `GET http://localhost:3000/api/v1/requests/<insert request id here>`
* No body required
* Example response body
```
{
    "approvals": null,
    "approved": false,
    "campaign_id": 1,
    "created_at": "2020-09-06T17:11:23.639004",
    "description": "test description a",
    "finalized": false,
    "id": 2,
    "image": "request.jpg",
    "recipient": "1",
    "updated_at": "2020-09-06T17:11:23.639042",
    "value": 1.0
}
```
#### Get all Requests
* Path `GET http://localhost:3000/api/v1/requests`
* No body required
* Example response body
```
[
    {
        "approvals": 1,
        "approved": false,
        "campaign_id": 1,
        "created_at": "2020-09-05T20:41:47.774790",
        "description": "test description",
        "finalized": false,
        "id": 1,
        "image": "test.jpg",
        "recipient": "1",
        "updated_at": "2020-09-05T20:41:47.774800",
        "value": 1.0
    },
    {
        "approvals": null,
        "approved": false,
        "campaign_id": 1,
        "created_at": "2020-09-06T17:11:23.639004",
        "description": "test description a",
        "finalized": false,
        "id": 2,
        "image": "request.jpg",
        "recipient": "1",
        "updated_at": "2020-09-06T17:11:23.639042",
        "value": 1.0
    }
]
```
#### Update a Request by ID number
* Path: `PUT http://localhost:3000/api/v1/requests/<insert request id here>`
* Example JSON put body
```
{
    "description": "better description",
    "image": "better_image.jpg",
    "approvals": "5"
}
```
* Example response body
```
{
    "approvals": "5",
    "approved": false,
    "campaign_id": 1,
    "created_at": "2020-09-06T17:11:23.639004",
    "description": "better description",
    "finalized": false,
    "id": 2,
    "image": "better_image.jpg",
    "recipient": "1",
    "updated_at": "2020-09-06T17:11:47.639042",
    "value": 1.0
}
```
#### Delete a Request by ID number
* Path: `DELETE http://localhost:3000/api/v1/requests/<insert request id here>`
* No body required
* Example response body
```
{
    "approvals": null,
    "approved": false,
    "campaign_id": 1,
    "created_at": "2020-09-06T18:05:01.891894",
    "description": "test description b",
    "finalized": false,
    "id": 3,
    "image": "request_b.jpg",
    "recipient": "1",
    "updated_at": "2020-09-06T18:05:01.891901",
    "value": 2.0
}
```

</details> 

<details><summary> Business Endpoints </summary> 

#### Convert Wei to USD
* Path: `GET http://localhost:3000/api/v1/price_converter?wei={wei_amount}`
* Requires query params with a key of 'wei' and value of the amount of wei to be converter
* No body required
* Example response
```
{ 
    "USD": 357
}
```
</details> 
