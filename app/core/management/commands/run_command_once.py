from django.core.management.base import BaseCommand
from core.tasks import say_hello, add

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        say_hello.delay()
        add.delay(2, 3)
        self.stdout.write("Tasks queued.")