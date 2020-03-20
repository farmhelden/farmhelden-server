setup postgres

CREATE DATABASE farmhelden;

CREATE USER farmhelden WITH PASSWORD 'password';

ALTER ROLE farmheldenUser SET client_encoding TO 'utf8';
ALTER ROLE farmheldenUser SET default_transaction_isolation TO 'read committed';
ALTER ROLE farmheldenUser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE farmhelden TO farmheldenUser;


create superuser

python manage.py createsuperuser --email admin@example.com --username admin



start dev server

source env/bin/activate

cd farmhelden

python manage.py runserver
