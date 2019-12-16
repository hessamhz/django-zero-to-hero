## Models Modifications
After each modifications on our models we will use these commands
```
python manage.py makemigrations
python manage.py migrate
```
We can also specify an app to migrate
```
python manage.py makemigrations ourappname
python manage.py migrate ourappname
```

## Creating Super User
Simple as this
```
python manage.py createsuperuser
```

## Running The Server
```
python manage.py runserver
```
We can Also specify the port and address that we want to run our django website
```
python manage.py runserver localhost:8215
```