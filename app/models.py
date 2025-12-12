from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    