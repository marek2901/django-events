web: cd events_crm && newrelic-admin run-program gunicorn crm.wsgi --log-file -
release: python events_crm/manage.py migrate
