from django.db import models


class Customers(models.Model):
    fristName = models.CharField(max_length=100)
    email     = models.CharField(max_length=20)
    def __str__(self):
        return self.fristName   
    
class Posts(models.Model):
    author = models.CharField(max_length=100)
    tag    = models.CharField(max_length=15)
    def __str__(self):
        return self.author + '   ' + self.tag       