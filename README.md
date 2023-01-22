# django_spa_comments_backend

Here is the backend part of my fullstack single page application

Try it https://bogdannoff.github.io/react_spa_comments/

# Description
The application is designed to allow the user to leave comments. 
All comments and information about users are stored in the database. 
The user can edit and delete their own comments

# Technologies
- Djando
- WebSockets (Django Channels)
- Docker

# Launch
- clone this repo
- setup your PostgreSQL database
- set environment variables: DB_HOST; POSTGRES_DB; POSTGRES_PASSWORD; POSTGRES_USER; SECRET_KEY
- run `pip install requirements.txt`
- run `python manage.py makemigrations`
- run `python manage.py migrate`
- run `python manage.py runserver 127.0.0.1:8080`

# Learn More

Frontend source code https://github.com/bogdannoff/react_spa_comments
