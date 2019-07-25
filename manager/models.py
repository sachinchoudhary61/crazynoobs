from django.db import models

# Create your models here.
class managerrole(models.Model):
    managerid = models.AutoField(primary_key=True)
    managername = models.CharField(max_length=200, unique=True, default="")