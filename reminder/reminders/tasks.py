from celery.task import PeriodicTask
from datetime import date, timedelta
from views import send_a_reminder
from models import Reminder
from django.core.mail import send_mail

class MailReminderTask(PeriodicTask):
    run_every = timedelta(seconds=30)

    def run(self, **kwargs):
        send_a_reminder()
        logger = self.get_logger(**kwargs)
        logger.info("Running mail reminder task.")
        return True
