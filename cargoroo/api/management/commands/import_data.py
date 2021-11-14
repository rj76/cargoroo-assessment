from django.core.management.base import BaseCommand

from api.batch import Batch


class Command(BaseCommand):
    help = """
    Import datasets
    """

    def handle(self, *args, **options):
        batch = Batch()
        batch.run()
