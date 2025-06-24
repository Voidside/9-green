from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    """ """

    name = models.CharField(max_length=50, verbose_name="Name", unique=True)

    status = models.BooleanField(verbose_name="State")
    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    """ """

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", related_name='sub_categories')
    name = models.CharField(max_length=50, verbose_name="Name", unique=True)
    photo = models.ImageField(verbose_name="Photo", upload_to="sub_category_photos/")

    status = models.BooleanField(verbose_name="State")
    def __str__(self):
        return self.name


class Product(models.Model):
    """ """

    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, verbose_name="Sub category", related_name='products')
    name = models.CharField(max_length=50, verbose_name="Name", unique=True)
    photo = models.ImageField(verbose_name="Photo", upload_to="product_photos/")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    price = models.BigIntegerField(verbose_name="Price")

    status = models.BooleanField(verbose_name="State")
    def __str__(self):
        return self.name

class Branch(models.Model):
    """ """
    PHONE_REGEX = RegexValidator(
        regex = r"^[\+]998[0-9](9)$",
    )

    
    name = models.CharField(max_length=50, verbose_name="Name", unique=True)
    address = models.CharField(max_length=100, verbose_name="Address")
    phone = models.CharField(max_length=20, verbose_name="Phone",unique=True, validators=[PHONE_REGEX])
    work_time = models.CharField(max_length=50, verbose_name="Work time")
    info = models.TextField(verbose_name="Information", null=True, blank=True)
    map_address = models.URLField(verbose_name="Map address")

    status = models.BooleanField(verbose_name="State")

    def __str__(self):
        return self.name