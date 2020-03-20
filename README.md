## setup postgres

```sql
CREATE DATABASE farmhelden;

CREATE USER farmhelden WITH PASSWORD 'password';

ALTER ROLE farmheldenuser SET client_encoding TO 'utf8';
ALTER ROLE farmheldenuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE farmheldenuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE farmhelden TO farmheldenUser;
``` 

## create superuser
```bash
python manage.py createsuperuser --email admin@example.com --username admin
``` 

## create and run migrations from model changes
```bash
python farmhelden/manage.py makemigrations
python farmhelden/manage.py migrate
``` 

## build and start dev server with local postgres

docker build -t farmhelden .
docker run --network="host" farmhelden
