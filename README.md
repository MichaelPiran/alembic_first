## Create postgres db
docker run --rm -d --name postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -p 5432:5432 postgres

docker exec -it postgres psql -U myuser -c 'CREATE DATABASE mydb;'

## Install python dep
pip install psycopg2-binary sqlalchemy

pip install alembic

## Init alembic
alembic init alembic

### Autogenerate migrations
alembic revision --autogenerate -m "Create a baseline migrations"
#modify the version files
alembic upgrade head

### Manual migrations
alembic revision -m "Create trigger on students table"
alembic upgrade head


## Usefull command
Display the current revision for a database:
    alembic current
View migrations history:
    alembic history --verbose.
Revert all migrations:
    alembic downgrade base.
Revert migrations one by one:
    alembic downgrade -1.
Apply all migrations:
    alembic upgrade head.
Apply migrations one by one:
    alembic upgrade +1.
Display all raw SQL:
    alembic upgrade head --sql.
Reset the database:
    alembic downgrade base && alembic upgrade head.