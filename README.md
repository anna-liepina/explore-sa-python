[ci.tests-master-badge]: https://circleci.com/gh/anna-liepina/explore-sa-python/tree/master.svg?style=svg
[ci.tests-master]: https://circleci.com/gh/anna-liepina/explore-sa-python/tree/master
[ci.coverage-master-badge]: https://codecov.io/gh/anna-liepina/explore-sa-python/branch/master/graph/badge.svg
[ci.coverage-master]: https://codecov.io/gh/anna-liepina/explore-sa-python/branch/master

[ci.tests-heroku-badge]: https://circleci.com/gh/anna-liepina/explore-sa-python/tree/heroku.svg?style=svg
[ci.tests-heroku]: https://circleci.com/gh/anna-liepina/explore-sa-python/tree/heroku
[ci.coverage-heroku-badge]: https://codecov.io/gh/anna-liepina/explore-sa-python/branch/heroku/graph/badge.svg
[ci.coverage-heroku]: https://codecov.io/gh/anna-liepina/explore-sa-python/branch/heroku

|               | master                                                        | heroku
| ---           | ---                                                           | ---
| __tests__     | [![tests][ci.tests-master-badge]][ci.tests-master]            | [![tests][ci.tests-heroku-badge]][ci.tests-heroku]
| __coverage__  | [![coverage][ci.coverage-master-badge]][ci.coverage-master]   | [![coverage][ci.coverage-heroku-badge]][ci.coverage-heroku]

# 'Data Explorer' GraphQL back-end (Python)

This project is done to demonstrate my knowledge, which I learned recently as I try to get into the software development industry, I had a mentor to help me out.
The project aims to parse UK government data on property sales, and perform statistical analysis, as well as link it with geology data, like addresses and latitude and longitude.

the aim is to build a scalable GraphQL backend, which can quickly return requested results
to demonstrate complex cases of GraphQL use, such as N+1 problem, scaling where more than one database is required [write/read nodes]
complex automated QA, anonymized data seeding for QA purposes, and some limits of JavaScript, where for example by default objects in V8 object can have ~8.4mil of fields, but Map can handle way more. Queue system for data processing.

* GraphQL live [demo](https://strawberry.exploreme.co.uk/graphql) [currently unavailable]
* Web Application [example](https://github.com/anna-liepina/explore-cwa-react) of how data can be consumed
  * Web Application live [demo](https://mirror.exploreme.co.uk/) [currently unavailable]

### software requirements

* Python v3.11+

<!-- if you're using `make` commands, __[docker](https://docs.docker.com/install/)__ and __[docker-compose](https://docs.docker.com/compose/install/)__ are required, and local __[node.js](https://nodejs.org/)__ with __[npm](https://www.npmjs.com/)__ are optional
* [node.js](https://nodejs.org/) v18+
* [npm](https://www.npmjs.com/) v5+ or [yarn](https://yarnpkg.com/)
* __optional__ [makefile](https://en.wikipedia.org/wiki/Makefile) comes out of the box in *unix* enviroments
* __optional__ [docker](https://www.docker.com/) v18.09+
* __optional__ [sqlite3](https://www.sqlite.org/index.html) v3+ *for 'integration' tests only* -->

### used technologies

* [fast API](https://fastapi.tiangolo.com/)
* [strawberry](https://strawberry.rocks/)
* [peewee](https://docs.peewee-orm.com/)
* [graphql](https://graphql.org/)

<!-- ### used services

* [circle ci](https://circleci.com/dashboard) - WIP
* [codecov](https://codecov.io/) - WIP
* [code climate](https://codeclimate.com/) - WIP
* [snyk](https://snyk.io/) - WIP -->

### where to get data-sets
 * [UK postcodes](https://www.getthedata.com/open-postcode-geo)
 * [UK house sales data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)
 * [UK LSOA & Postcode data](https://geoportal.statistics.gov.uk/datasets/ons::postcode-to-output-area-to-lower-layer-super-output-area-to-middle-layer-super-output-area-to-local-authority-district-november-2018-lookup-in-the-uk-2/about)
 * [Police Records Data](https://data.police.uk/data/archive/)

### how to install

* `pip install -r requirements.txt`
<!-- * with `make` commands no steps additional are required, otherwise you need to execute `$ npm i` -->

<!-- ### how to run tests  - WIP

* `$ make test` or `$ npm test`
  * __optional__ [ 'jest' CLI params](https://facebook.github.io/jest/docs/en/cli.html), examples:
    * to collect coverage, example: `$ npm test -- --coverage`, report will be located in __./coverage__ directory
    * to execute tests __only__ in a specific file, for example: `$ npm test src/graphql/user.test.js` -->

<!-- ### how to set up a database  - WIP

* database configuration is located in the file __src/orm-config.js__
* to get database schema up to date: `$ npm run sql db:migrate`, you can also create a database via ORM `npm run sql db:create`
* to seed the database with 'test' data: `$ npm run sql db:seed:all` -->

### how to run in 'development' mode

* `uvicorn main:app --reload`
<!-- * `$ make` or `$ npm start` -->

### how to run in 'production' mode

* `gunicorn --worker-class uvicorn.workers.UvicornWorker main:app`
  * to run on different port example: `PORT=18080 gunicorn --worker-class uvicorn.workers.UvicornWorker main:app`
<!-- * `$ make serve`, there is no *npm* equivalent
* if you __only__ need to generate static assets
  * `$ make build` or `$ npm run build` - generated assets will be located in __./build__ directory -->

<!-- ### how to run containers with different variables using 'make' - WIP

* `make PORT=18081` -->

### gitflow

* *heroku* -> current __production__, contains *production specific changes*, trigger production deploment on *every push*
* *master* -> most upto date __production ready__, all pull requests in to this branch got mandatory check 'ci/circleci: jest'
* *feature branches* -> get merged into the master branch when they are ready and mandatory checks passed
* *CI executes tests in an isolated environment*

### used environment variables

| variable            | default value | used as   | purpose
| ---                 | ---           | ---       | ---
| PORT                | 8081          | number    | port on which application will be made available
| ***                 | ***           | ***       | 
| DB_HOSTNAME         | 127.0.0.1     | string    | host on which database can be reached
| DB_USERNAME         | root          | string    | database user
| DB_PASSWORD         | password      | string    | database user's password
| DB_PORT             | 3306          | number    | port on which database can be reached
| DB_NAME             | explore       | string    | database [schema] name
| DB_DIALECT          | mysql         | string    | database's dialect: one of mysql / sqlite / postgres
<!-- | DB_REPLICA_HOSTNAME | 127.0.0.1     | string    | database replica's host for read-only
| DB_REPLICA_USERNAME | root          | string    | database replica's user for read-only
| DB_REPLICA_PASSWORD | password      | string    | database replica's user's password for read-only -->
<!--
| SSL_KEY             |               | string    | absolute path to the SSL key, example: `/home/ubuntu/private.key`
| SSL_CERT            |               | string    | absolute path to the SSL certificate, example: `/home/ubuntu/certificate.crt`
| ***                 | ***           | ***       | if replica's config specified then non-replica connections are used only writes -->

### supported databases

| database      | version   | adapter                                           | main purpose
| ---           | ---       | ---                                               | ---
| MySQL         | 8         | [mysql2](https://pypi.org/project/pymysql/)       | production
<!-- | PostgreSQL    | 11        | [pg](https://www.npmjs.com/package/pg)            | production - WIP
| SQLite        | 4         | [sqlite3](https://www.npmjs.com/package/sqlite3)  | QA Automation & CI - WIP -->

* if you use MySQL 5.7+ you need to make sure it can work with [mysql native password](https://medium.com/@crmcmullen/how-to-run-mysql-8-0-with-native-password-authentication-502de5bac661)

* PostrgeSQL and SQLite are partially supported because some of the queries are not fully engine-agnostic, and some functions do not exist in SQLite for example
