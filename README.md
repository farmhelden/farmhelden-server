## Prerequisites
docker-compose

## Install & Run
```bash
docker-compose up
```

## Use Django Management Commands:
Use this while `docker-compose up` is running. Open a second terminal tab and execute:
```bash
./manage
```

## Useful Django Management Commands
# create and run migrations from model changes
```bash
python farmhelden/manage.py makemigrations
python farmhelden/manage.py migrate
```

# create superuser
```bash
python manage.py createsuperuser --email admin@example.com --username admin
``` 
