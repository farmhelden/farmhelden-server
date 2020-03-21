 #!/bin/bash

until PGPASSWORD="password" psql -h "postgres-farmhelden" -U "farmheldenuser" -w -d "farmhelden" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - booting application"

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000