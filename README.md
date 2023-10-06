# MY DJANGO WEBSITE

## Getting started

Clone this repository and enter the project containing folder

```bash
git clone <repo-url>
cd repo-dir
```

Create your pyenv

```bash
python3 -m venv venv 
```

Activate your pyenv

```bash
source venv/bin/activate
```

Install all required dependencies

```bash
pip3 install -r requirements.txt
```

Run migrations

```bash
python3 manage.py migrate
```

## Running

Run the Django web server locally

```bash
python3 manage.py runserver
```

Check out your first website on [http://localhost:8000](http://localhost:8000)

## Admin

Create superuser to manage your database information

```bash
python manage.py createsuperuser
```

Check out your admin page on [http://localhost:8000/MeuApp](http://localhost:8000/MeuApp)

## Running with docker + docker-compose

```bash
docker-compose up --build
```

Check out your admin page on [http://localhost:8000/MeuApp](http://localhost:8000/MeuApp)

You can also create a superuser inside running with docker:

```bash
docker exec -it your_container_name /bin/bash
python manage.py createsuperuser
```
