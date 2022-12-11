import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leopard.settings')

# backend='redis://localhost:6379/1', broker='redis://localhost:6379/0'
app = Celery('leopard')

app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现 tasks.py 这些模块的方法
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
