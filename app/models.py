from django.db import models

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=55)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

class Product(models.Model):
    class ChoiceSize(models.TextChoices):
        XS = 'XS'
        X = 'X'
        M = 'M'
        L = 'L'
        XL = 'XL'

    class ChoiceColor(models.TextChoices):
        BLACK = 'Black'
        WHITE = 'White'
        RED = 'Red'
        BLUE = 'Blue'
        GREEN = 'Green'
        GREY = 'GREY'
        YELLOW = 'YELLOW'
        BROWN = 'BROWN'


    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='product')
    text = models.TextField()
    size = models.CharField(max_length=155, choices=ChoiceSize.choices, default=ChoiceSize.M)
    color = models.CharField(max_length=155, choices=ChoiceColor.choices, default=ChoiceColor.WHITE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)

