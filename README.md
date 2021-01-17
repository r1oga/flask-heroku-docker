## Config postgres
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

## Deploy on Heroku

1. ```
    heroku create appname
    heroku addons:create heroku-postgresql:hobby-dev --app appname
    ```
2. Add `?sslmode=require` to DB URI
3. 