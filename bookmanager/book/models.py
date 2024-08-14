from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=10)
    pass
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
