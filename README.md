# foodgram-project

ip = 84.201.164.156

## Installation

1. clone repository and enable virtual environment
For Windows:
```
python -m venv venv
./venv/Scripts/activate.bin
```
For Linux:
```
python3 -m venv venv
. /venv/Scripts/activate
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Make and run migrations
```
python manage.py makemigrations
python manage.py migrate
```
4. Collect static
```
python manage.py collectstatic
```
5. Run server
```
python manage.py runserver
```
## Optional
You can create a superuser
```
python manage.py createsuperuser
```
## Technology stack

1. Python 3.8
2. Django 3.0.11
3. DRF 3.11.0
4. Docker
5. Docker-Compose 3.8
