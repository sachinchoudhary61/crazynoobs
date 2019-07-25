from django.db import models

# Create your models here.
class userrole(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=200, unique=True, default="")

