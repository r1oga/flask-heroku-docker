# Height Stats Collector
Minimal python flask web application.
![app screenshot](assets/screenshot.png)
## Features
- Collect user inputs: mail & height
- Store inputs in postgres DB
- Send email to user after submission that includes stats

## Built with
- [Flask](https://palletsprojects.com/p/flask/)
- postgresql: [psycopg](https://www.psycopg.org/docs/index.html) & [sqlalchemy](https://www.sqlalchemy.org/)

## Set up
### Postgres config for local development
1. Install postgres
    ```
    docker run -p 5432:5432 --name pg -e POSTGRES_PASSWORD=pwd -d postgres

    # reach into postgres inside container:
    docker exec -it pg psql -U postgres
    ```
2. Create database
    ```
    postgres=# CREATE DB dbname;
    ```
3. Connection URI: `postgresql://postgres:pwd@localhost/dbname`
4. Create table:
    ```
    python
    from app import db
    db.create_all()
    ```

## [Deployment with Docker & Heroku](https://devcenter.heroku.com/categories/deploying-with-docker)

1. ```
    heroku login
    heroku create appname
    heroku addons:create heroku-postgresql:hobby-dev --app appname
    ```
2. Add `?sslmode=require` to DB URI
3. Create DB:
    ```
    heroku run python
    >>> 
    from app import db
    db.create_all()
    exit()
    ```
3. Push: `heroku container:push web`
4. Release: `heroku container:release web`
5. Access DB with CLI: `heroku pg:psql`

## Resources
- [Miniconda on Heroku Example App](https://github.com/heroku-examples/python-miniconda)