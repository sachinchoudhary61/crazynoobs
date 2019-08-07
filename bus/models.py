from django.db import models
from user.models import user_info,appscategory

class bus_category(models.Model):
    bus_type_id = models.AutoField(primary_key=True)
    bus_type = models.CharField(max_length=200, unique=True, default="")

class route(models.Model):
    route_id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=200, unique=True, default="")
    destination = models.CharField(max_length=200, unique=True, default="")
    route_isactive = models.BooleanField(default=False)

class bus_time(models.Model):
    departure_time = models.CharField(max_length=200, unique=True, default="")
    arival_time = models.CharField(max_length=200, unique=True, default="")
    bus_id = models.ForeignKey(route, on_delete=models.CASCADE, default="")

class bus_seats(models.Model):
    seats = models.BooleanField(default=False)

class bus_info(models.Model):
    app_id = models.ForeignKey(appscategory, on_delete=models.CASCADE, default="")
    bus_id = models.AutoField(primary_key=True)
    bus_type_id = models.ForeignKey(bus_category, on_delete=models.CASCADE, default="")
    route_id = models.ForeignKey(route, on_delete=models.CASCADE, default="")
    bus_image = models.CharField(max_length=200, unique=True, default="")
    bus_status = models.BooleanField(default=False)
    bus_fare = models.CharField(max_length=200, unique=True, default="")


class booking_details(models.Model):
    date_time = models.CharField(max_length=200, unique=True, default="")





