release: python deploy.py; pip install -e ./kolibri
web: gunicorn kolibri.deployment.default.wsgi --max-requests 1000 --log-file=-g
