#from __future__ import absolute_import, unicode_literals

#from celery.schedules import crontab
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

app = Celery('proyecto', broker='pyamqp://', backend='rpc://') 


#app = Celery('proyecto') 

app.config_from_object('django.conf:settings', namespace='CELERY')


#app.conf.beat_schedule = {
#    'add-every-5-seconds': {
#        'task': 'web.tasks.subirBoleta',
#        'schedule': crontab(minute='*/4'),
#        'args': (16, 16)
#    }
#}

app.conf.timezone = 'America/Santiago'

app.autodiscover_tasks()

#@app.task(bind=True)

#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))
