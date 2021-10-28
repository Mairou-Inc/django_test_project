# django_test_project



● Миронов Сергей 
● Тестовое задание на Python
● API для поиска/создания магазинов с фильтрацией

Instalation Guide:


```
sudo apt update 
sudo apt install postgresql python3 python3-venv python3-pip

sudo -u postgres psql
create database test_db;
create user test_user with password 'cienbythgetx';
grant all privileges on database test_db to test_user;
exit


python3 -m venv env
source env/bin/activate
pip3 intall -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```


