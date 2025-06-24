from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Category(models.Model):
    ''' '''

    name = models.CharField(max_length=100, verbose_name='Name')
    photo = models.ImageField(verbose_name='Photo', upload_to='category_photos')
    about = models.TextField(verbose_name='About', null=True, blank=True)

    state = models.BooleanField(verbose_name='State')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created on')


class Product(models.Model):
    ''' '''

    WEIGHT_MARK = (
        ('kg', 'kg'),
        ('piece', 'dona'),
        ('litr', 'litr'),
        ('box', 'quti'),
    )

    SERIAL_NUMBER = RegexValidator(
        regex= r'^[0-9]{8}$'
    )


    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Name')
    made_by = models.CharField(max_length=150, verbose_name='Made by')
    weight_mark = models.CharField(max_length=20, choices=WEIGHT_MARK)
    weight = models.BigIntegerField(verbose_name='Weight')
    photo = models.ImageField(verbose_name='Photo', upload_to='category_photos')
    serial_number = models.CharField(unique=True, validators=[SERIAL_NUMBER])
    made_on = models.DateField(verbose_name='Made on')
    expiration_date = models.DateField(verbose_name='Expiration date')
    about = models.TextField(verbose_name='About', null=True, blank=True)

    state = models.BooleanField(verbose_name='State')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created on')

    def __str__(self):
        return self.name
