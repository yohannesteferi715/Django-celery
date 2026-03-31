import os 

from celery  import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
 

app=Celery('dcelery')

#Celery method used to load configuration settings
app.conf.from_object('django.conf:settings',namespace="CELERY")

@app.task
def add_numbers():
    return 



app.autodiscover_tasks()