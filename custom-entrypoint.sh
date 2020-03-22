#!/bin/sh

set -e

wait_for_postgres() {
    until pg_isready -U farmhelden -q -h db; do
        >&2 echo "Postgres is unavailable - sleeping 5 seconds"
        sleep 5
    done
    echo "\nPostgres is available"
}

run_development() {
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
}

start_server() {
  python manage.py migrate
  gunicorn -w 3 -b 0.0.0.0:8000 farmhelden.wsgi
}

if [ "$1" = 'production' ]; then
    wait_for_postgres
    start_server
fi

if [ "$1" = 'development' ]; then
    wait_for_postgres
    run_development
fi

exec "$@"
