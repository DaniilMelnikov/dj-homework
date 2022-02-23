from django.db import models
from django.forms import SlugField


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=60)
    price = models.FloatField()
    image = models.FilePathField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug =  models.SlugField(verbose_name=name, unique=True)

    def __str__(self):
        return self.name
