pip install -r requirements.txt
python core/manage.py collectstatic --no-input
python core/manage.py migrate