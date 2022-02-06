release: kolibri manage collectstatic --noinput; ln -ls .kolibri/static static; kolibri start &
web: gunicorn kolibri.deployment.default.wsgi --max-requests 1000 --log-file=-g
