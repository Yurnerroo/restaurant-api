# restaurant-api
## How to install
Beforehands, you need to install Python3.9.7:
```
git clone https://github.com/Yurnerroo/restaurant-api.git
python3 -m venv venv
venv/Scripts/activate
pip install -r requirments.txt
export/set DB_HOST=<host name>
export/set DB_NAME=<db name>
export/set DB_USER=<user name>
export/set DB_PASSWORD=<db password>
python manage.py migrate
python manage.py runserver
```
## For Docker:
```
docker-compose build
docker-compose up
```
## For authorization:
```
create user on /api/employee/register/
get token on /api/employee/token/
```
## Features
- Swagger documentation
- JWT authentication
- Docker usage
- Tests + flake8
