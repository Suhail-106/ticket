from django.core.management.base import BaseCommand
from tickets.models import Ticket

class Command(BaseCommand):
    help = 'Generate tickets'

    def handle(self, *args, **kwargs):
        for _ in range(2000):
            Ticket.objects.create()
        self.stdout.write("2000 Tickets Generated")