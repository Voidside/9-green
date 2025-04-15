from django.db import models

# Create your models here.


class Chek_in(models.Model):
    """ """

    full_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    grade = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)

    created_on = models.DateTimeField(auto_now_add=True)