from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Очистка БД и загрузка тестовых данных из фикстур'

    def handle(self, *args, **options):
        self.stdout.write('Удаление существующих продуктов...')
        Product.objects.all().delete()

        self.stdout.write('Удаление существующих категорий...')
        Category.objects.all().delete()

        self.stdout.write('Загрузка фикстур...')
        call_command('loaddata', 'initial_data.json')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))