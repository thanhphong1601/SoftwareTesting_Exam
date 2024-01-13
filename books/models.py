from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

#models
class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishedYear = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_query_name='books')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True)
