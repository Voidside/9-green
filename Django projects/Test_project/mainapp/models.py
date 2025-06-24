from django.db import models

# Create your models here.


STATUS = (
    ('archive',"Arxiv"),
    ("active","Faol"),
)


class Category(models.Model):
    """  """
    
    name = models.CharField(max_length=250, verbose_name="Nomi", unique=True)
    photo = models.ImageField(upload_to="category_photos/", verbose_name="Rasm")
    description = models.TextField(verbose_name="Batafsil", null=True, blank=True) 

    status = models.CharField(max_length=50, verbose_name="Holati", choices=STATUS)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    """  """

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tests")
    question = models.CharField(max_length=255, verbose_name="Savol")
    answer1 = models.CharField(max_length=255, verbose_name="1-javob")
    answer2 = models.CharField(max_length=255, verbose_name="2-javob")
    answer3 = models.CharField(max_length=255, verbose_name="3-javob")
    
    TRUE_ANSWER = (
        ('answer1',answer1),
        ('answer2',answer2),
        ('answer3',answer3),
    )

    true_answer = models.CharField(max_length=50, choices=TRUE_ANSWER , verbose_name="Javob")

    status = models.CharField(max_length=50, verbose_name="Holati", choices=STATUS)
    created_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.question



