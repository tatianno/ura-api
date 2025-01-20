#!/bin/bash
apt update && apt upgrade -y
apt install python3 python3-pip python3-venv git nginx -y

source venv/bin/activate
python3 -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser

deactivate

cp confs/system/gunicorn.service /etc/systemd/system/
systemctl daemon-reload
systemctl start gunicorn
systemctl enable gunicorn

cp confs/nginx/default.conf /etc/nginx/conf.d/
/etc/init.d/nginx restart