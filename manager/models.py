from django.db import models
from user.models import user_info, appscategory
# Create your models here.
class managerrole(models.Model):
    managerid = models.AutoField(primary_key=True)
    managername = models.CharField(max_length=200, unique=True, default="")

class hotelinfo(models.Model):

    app_id = models.ForeignKey(appscategory, on_delete=models.CASCADE, default="")
    hotel_id = models.AutoField(primary_key=True)
    email = models.ForeignKey(user_info, on_delete=models.CASCADE, default="")
    hotel_status = models.BooleanField(default=False)
    hotel_name = models.CharField(max_length=50, default="")
    hotel_city = models.CharField(max_length=100, default="")
    hotel_image = models.ImageField(upload_to='hotel_image/', null=True)
    hotel_address = models.CharField(max_length=100, default="")
    hotel_no_rooms = models.CharField(max_length=100, default="")
    hotel_room_price = models.CharField(max_length=100, default="")
    hotel_helpline_no = models.CharField(max_length=100, default="")
    room_with_meal_or_without_meal = models.BooleanField(default=False)


class hotelguestinfo(models.Model):

    hotel_id = models.ForeignKey(hotelinfo, on_delete=models.CASCADE, default="")
    guest_id = models.AutoField(primary_key=True)
    guest_check_in_date = models.CharField(max_length=50, default="")
    guest_checkout_in_date = models.CharField(max_length=50, default="")
    guest_no_adult = models.CharField(max_length=100, default="")
    guest_no_children = models.CharField(max_length=100, default="")
    email = models.ForeignKey(user_info, on_delete=models.CASCADE, default="")

class hotelrooms(models.Model):

    hotel_id = models.ForeignKey(hotelinfo, on_delete=models.CASCADE, default="")
    room_id = models.AutoField(primary_key=True)
    room_occupied = models.BooleanField(default=False)
    room_no = models.CharField(max_length=100, default="")
    isactive = models.BooleanField(default=False)

class room_type(models.Model):
    room_id = models.ForeignKey(hotelrooms, on_delete=models.CASCADE, default="")
    room_type_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=100, default="")
    room_type_price = models.CharField(max_length=100, default="")

class hotelroomimages(models.Model):

    room_id = models.ForeignKey(hotelrooms, on_delete=models.CASCADE, default="")
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='rooms_image/', null=True)
    isactive = models.BooleanField(default=False)



