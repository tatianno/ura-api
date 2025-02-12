#!/bin/bash
apt update
apt install python3 python3-pip python3-venv git nginx -y


python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput
python scripts/configuracoes_iniciais/main.py

chown www-data:www-data /usr/src/ura-api/backend/ -R

deactivate

cp confs/system/gunicorn.service /etc/systemd/system/
systemctl daemon-reload
systemctl start gunicorn
systemctl enable gunicorn

cp confs/nginx/default /etc/nginx/sites-available/
/etc/init.d/nginx restart