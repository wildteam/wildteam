from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    tel = models.CharField(max_length=11, default='')

    def __str__(self):
        return self.username
    pass

