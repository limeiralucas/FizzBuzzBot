from celery import Celery
from celery.schedules import crontab

from fizzbuzz_core import create_app
from fizzbuzz_core.tasks import answer_mentions


def create_celery(app):
    celery = Celery(
        app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['BROKER_URL'])
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


flask_app = create_app()
celery = create_celery(flask_app)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60, answer_mentions, name='answers mentions')
