release: kolibri manage collectstatic; kolibri start &
web: gunicorn kolibri.deployment.default.wsgi --max-requests 1000 --log-file=-g
