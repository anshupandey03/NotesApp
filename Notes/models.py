from django.db import models
from datetime import date

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length =100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateField(default= date.today)


    def __str__(self):
        return self.title