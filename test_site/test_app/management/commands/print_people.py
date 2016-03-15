from django.core.management.base import BaseCommand, CommandError
from test_app.models import Document, People

class Command(BaseCommand):
    help = 'Select from people data by education'

    def handle(self, *args, **options):
        education = raw_input('Enter education: ')
        filtered_docs = Document.objects.filter(education = education)
        if not education:
            education = '[Empty]'

        if len(filtered_docs) > 0:
            self.stdout.write(self.style.SUCCESS('Found {0} people with {1} education:')
                              .format(len(filtered_docs), education))
            self.stdout.write(self.style.SUCCESS('Id\t\tName'))
            self.stdout.write(self.style.SUCCESS('--\t\t----'))

            for doc in filtered_docs:
                self.stdout.write(self.style.SUCCESS('{0}\t\t{1}')
                                  .format(doc.people.id, doc.people.name))
        else:
            self.stdout.write(self.style.ERROR('No people were found with {0} education')
                              .format(education))
