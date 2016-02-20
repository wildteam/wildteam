from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    # uid = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username
    pass