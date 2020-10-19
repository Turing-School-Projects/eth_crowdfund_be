# Etho Boost - A crowdfund app built on Etherium
- [About](#About)
- [Team](#Team)
- [Demo](#Demo)
- [Why?](#Why)
- [Tech](#Tech)
- [Future Iterations](#Future-Iterations)
- [Setup](#setup)
- [Database Setup](#database-setup)
- [Seeding The Database](#seeding-the-database)
- [Updating The Database](#database-updates)
- [API Endpoints](#api-endpoints)

## About  
[Etho-Boost](https://etho-boost-crowdfund.herokuapp.com/) is a crowdfunding platform that runs on the Ethereum blockchain. It the capstone/cross-pollination project built by 6 students at Turing School of Software and Design in their 4th and final module. Powered by smart-contracts deployed to the Ethereum Virtual Machine(EVM), Etho-Boost gives donors the power to review and approve withdrawal requests from the Boosters(campaigns) they have donated to, ensuring that donations are used as advertised.

## Team

### Blockchain/Front End

[Jack Cullen](https://github.com/jpc20)

### [Front-End](https://github.com/Turing-School-Projects/eth-crowdfund-fe)

[Andy Tom](https://github.com/attom2)

[Edwin Montealvo](https://github.com/edmdc89)

### Back-End

[Antonio Jackson](https://github.com/AntonioJacksonII)

[Ross Perry](https://github.com/perryr16)

[Taylor Keller](https://github.com/takeller)

## Demo

[![](http://img.youtube.com/vi/0h1UFCdixyE/0.jpg)](https://www.youtube.com/embed/Fkq_CC_XmZI "Etho-Boost Demo")

## Why? 

#### Trust  
 The untrustworthy nature of crowdfunding websites deters potential donors because there is no accountability. Fundraisers are not expected to publish honest, detailed information about where a donated dollar goes, and EthoBoost demands more transparency. 
EthoBoost gives donors the power to review and approve requests to withdraw funds before a manager can complete a withdrawal, ensuring that donations are used as advertised. Fund managers set a minimum value that a donor must contribute in order to have approval rights for that fund. A fund manager must create a request to withdraw donations, and the request must be approved by over 50% of ‘approvers’ for the campaign.

#### Borderless and Bankless  
 Today’s financial system makes it extremely difficult to send and receive money across borders, forcing crowdfunding platforms to restrict transactions by imposing fees on international donations. EthoBoost is built on the Ethereum blockchain, granting donors and fundraisers the freedom to exchange funds without the constraints of a traditional bank account from any specific country. 
 
 #### Transactions(Fees and time) 
 Crowdfunding platforms generally charge a 5% transaction fee, and transactions take at least 3-5 business days to complete. Facilitated by the Ethereum blockchain, EthoBoosts transactions cost just a few cents and finalize in 30 seconds.


## Tech

### [Front-End](https://github.com/Turing-School-Projects/eth-crowdfund-fe)
  - Vue.js
  - Jest
  - TravisCI
  - Heroku 
  - HTML/SCSS
### Blockchain
  - Solidity
  - Truffle
  - Ganache
  - Metamask
  - Web3
### Back-End 
  - Python 
  - Flask
  - pytest
  - PostgreSQL
  - SQLAlchemy

## Future Iterations
  * Transition to a stable coin(DAI, USDC, USDT, etc.)
  * Mobile App/PWA
  * Deploy to the Main Ethereum Network
  * Increase functionality around requests


## Setup <a name="setup"></a>
<details>
  <summary> App Setup Instructions </summary>

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
 8. Within the root directory:  
  a. Run `# pipenv --three` to create the virtual environment  
  c. Run `$ pipenv install` to install all dependencies  
  d. Run `$ createdb eth_crowdfund_api_db` to create the app database  
  e. Run `$ createdb eth_crowdfund_api_db_test` to create the testing database  
  f. Run `$ touch .env` to create an enviornment file 
  e. Within the `.env` file add appropriate environment values for flask enviornment, database URLs, and localhost port
  ```
   FLASK_ENV=development
   SQLALCHEMY_DATABASE_URI="postgresql://postgres:password@localhost/eth_crowdfund_api_db"
   SQLALCHEMY_TEST_DATABASE_URI="postgresql://postgres:password@localhost/eth_crowdfund_api_db_test"
   PORT=3000
  ```

 9. Run the following to activate the project virtual environment. When you are done working on the project, you should execute `$ exit` to exit the virtual environment
 ``` 
 $ pipenv shell   
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

### Database Setup <a name="database-setup"></a>
<details>
  <summary> Database Setup Instructions </summary>
Path: `eth_crowdfund_be`

 1. Run
 ```
 $ python3 manage.py db stamp head
 $ python3 manage.py db init
 $ python3 manage.py db upgrade
 => INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
    INFO  [alembic.runtime.migration] Will assume transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade  -> 96a8d065e5ea, empty message
 ```
 *if you do not recieve:* `INFO  [alembic.runtime.migration] Running upgrade  -> 96a8d065e5ea, empty message`
 *you may need to delete the alembic_version*
 Run 
 ```
 $ psql 
 =# \c eth_crowdfund_api_db
 =# DELETE FROM alembic_version
 DELTETE 1 
 =# \q
 $ python3 manage.py db stamp head 
 $ python3 manage.py db downgrade 
 $ python3 manage.py db upgrade 
 ```
 2. You can check the database by running
 ```
 $ psql
 $ \c eth_crowdfund_api_db
 $ \dt
 => List of relations
    Schema |         Name         | Type  |     Owner      
    --------+----------------------+-------+----------------
    public | alembic_version      | table | postgres
    public | campaign_contributor | table | postgres
    public | campaigns            | table | postgres
    public | contributor          | table | postgres
    public | requests             | table | postgres

 $ SELECT * FROM campaigns;
 => id | name | description | image | manager | contributors | upvote | min_contribution | address | expiration | created_at | updated_at
   ----+------+-------------+-------+---------+--------------+--------+------------------+---------+------------+------------+------------

 $ SELECT * FROM requests;
 => id | campaign_id | description | image | value | recipient | approved | finalized | approvals | created_at | updated_at
   ----+-------------+-------------+-------+-------+-----------+----------+-----------+-----------+------------+------------
 ```
 3. To exit the database, `exit` or `\q`
 </details>
 
 ### Seeding the Database <a name="seeding-the-database"></a>
 <details>
  <summary> Database Seeding Instructions </summary>
 Within the `pipenv shell` virtual environment, run the following:

 1. Ensure you are at `/eth_crowdfund_be`
 2. Run `$ python3 manage.py seed`
 3. Start server with `$ python3 run.py`
 4. Visit `localhost:3000/api/v1/campaigns` and `localhost:3000/api/v1/requests` and you should see seeded Campaigns and Requests.
</details>

### Database Updates <a name="database-updates"></a>
<details>
  <summary> Updating the Database Instructions </summary>

Path: `/eth_crowdfund_be`  
To make updates to the database and run a new migration, run the following:
```
 $ python3 manage.py db stamp head
 $ python3 manage.py db init
 $ python3 manage.py db migrate
 $ python3 manage.py db upgrade
```
* Note: If you encounter any root errors, such as `ERROR [root] Error: Target database is not up to date.` or `ERROR [root] Error: Relative revision -1 didn't produce 1 migrations`, run `$ python3 manage.py db stamp head` to reset the target database to your current database head.
</details>

## API Endpoints <a name="api-endpoints"></a>

### Campaigns

<details>
  <summary>Create a campaign </summary>

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
</details>

<details>
  <summary> Get a Campaign by ID number </summary>

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
</details>


<details>
  <summary> Get all Campaigns </summary>

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
</details>

<details>
  <summary> Update a Campaign by ID number </summary>

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
</details>

<details>
  <summary> Delete a Campaign by ID number </summary>

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

### Requests

<details>
  <summary> Create a Request </summary>

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
</details>

<details>
  <summary> Get a Request by ID number </summary>

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
</details>

<details>
  <summary> Get all Requests </summary>

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
</details>

<details>
  <summary> Update a Request by ID number </summary>

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
</details>

<details>
  <summary> Delete a Request by ID number </summary>

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

### Contributors

<details>
  <summary> Add a Contributor to a Campaign </summary>

* Path: `POST http://localhost:3000/api/v1/campaigns/<campaign_address>/contributor/<contributor_address>`
* No body required
* Example response body
```
{
    "address": "Hf84jhGE9fdjF9ehfdse45",
    "created_at": "2020-09-06T18:41:57.156262",
    "description": "Need help serving community",
    "expiration": "2020-10-25T00:00:00",
    "id": 16,
    "image": "https://picsum.photos/200/300",
    "manager": "LJHhf82u3hr0d9uhUg4g",
    "min_contribution": 1.5,
    "name": "Market St. Soup Kitchen",
    "requests": [
        {
            "approvals": 0,
            "approved": false,
            "campaign_id": 16,
            "created_at": "2020-09-06T18:41:57.238755",
            "description": "Cleaning supplies",
            "eth_id": null,
            "finalized": false,
            "id": 15,
            "image": "https://picsum.photos/200/300",
            "recipient": "jhF97hdfha97",
            "updated_at": "2020-09-06T18:41:57.238757",
            "value": 25.0
        }
    ],
    "updated_at": "2020-09-06T18:41:57.156266",
    "upvote": 50,
    "value": null
}
```
</details>

<details>
  <summary> View Campaigns by Contributor Address </summary>

* Path: `GET http://localhost:3000/api/v1/contributor/<contributor_address>/campaigns`
* No body required
* Example response body
```
[
    {
        "address": "Hf84jhGE9fdjF9ehfdse45",
        "created_at": "2020-09-06T18:41:57.156262",
        "description": "Need help serving community",
        "expiration": "2020-10-25T00:00:00",
        "id": 16,
        "image": "https://picsum.photos/200/300",
        "manager": "LJHhf82u3hr0d9uhUg4g",
        "min_contribution": 1.5,
        "name": "Market St. Soup Kitchen",
        "requests": [
            {
                "approvals": 0,
                "approved": false,
                "campaign_id": 16,
                "created_at": "2020-09-06T18:41:57.238755",
                "description": "Cleaning supplies",
                "eth_id": null,
                "finalized": false,
                "id": 15,
                "image": "https://picsum.photos/200/300",
                "recipient": "jhF97hdfha97",
                "updated_at": "2020-09-06T18:41:57.238757",
                "value": 25.0
            }
        ],
        "updated_at": "2020-09-06T18:41:57.156266",
        "upvote": 50,
        "value": null
    },
    {
        "address": "DFjh489GD74hgls8",
        "created_at": "2020-09-06T18:41:57.156312",
        "description": "Serving communities hit hard by Covid19",
        "expiration": "2020-10-25T00:00:00",
        "id": 17,
        "image": "https://picsum.photos/200/300",
        "manager": "jhF8dfh4jjgfdkjs45",
        "min_contribution": 1.5,
        "name": "Arc Thrift",
        "requests": [],
        "updated_at": "2020-09-06T18:41:57.156322",
        "upvote": 50,
        "value": null
    }
]
```
</details>

## Currency Conversion

<details>
  <summary> Convert Wei to USD </summary>

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
