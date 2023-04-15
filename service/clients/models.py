from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    # PROTECT когда удаляем user'а, проверяет нет ли связанного client, если есть, то не даст удалить.

    company_name = models.CharField(max_length=100)
    full_address = models.CharField(max_length=100)

    def __str__(self):
        return f'Cleint: {self.company_name}'