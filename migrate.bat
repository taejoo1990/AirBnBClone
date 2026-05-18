@echo off
echo make migrations....
python manage.py makemigrations

echo migrate....
python manage.py migrate

echo Done!