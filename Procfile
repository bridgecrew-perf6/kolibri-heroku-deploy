release: kolibri start --foreground
web: gunicorn kolibri.deployment.default.wsgi --max-requests 1000 --log-file=-g
