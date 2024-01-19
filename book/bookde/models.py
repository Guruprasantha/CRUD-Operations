from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    overview=models.CharField(max_length=100)
    date_of_publication=models.DateField(max_length=20)
    language=models.CharField(max_length=100)
