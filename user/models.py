from django.db import models

# Create your models here
class userrole(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=200, unique=True, default="")

class appscategory(models.Model):
      app_id = models.AutoField(primary_key=True)
      app_name = models.CharField(max_length=200, unique=True, default="")
class user_info(models.Model):

    roleid = models.ForeignKey(userrole, on_delete=models.CASCADE, default="")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(primary_key=True, default="", max_length=200)
    password = models.CharField(max_length=50)
    mobile_no = models.CharField(default="", max_length=50)
    image = models.CharField(max_length=250, default="", null=True)
    address = models.CharField(max_length=250, default="", null=True)
    otp = models.CharField(max_length=200, null=True)
    otp_gen_time = models.CharField(max_length=200, null=True)
    isactive = models.BooleanField(default=False)
    token = models.CharField(max_length=200, default="")
    business_user_business_info = models.TextField(default="")
    #business_id = models.CharField(max_length=200, default="")
    app_id = models.ForeignKey(appscategory, on_delete=models.CASCADE, default="")


