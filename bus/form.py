from django import forms
from bus.models import bus_category , route , bus_time , bus_info , bus_seats , booking_details

class bus_category_form (forms.ModelForm):
    class Meta():
        model =bus_category
        exclude = ["bus_type_id", "bus_type"]

class route_form():
    class Meta():
        model =route

        exclude = ["route_id", "origin","destination", "route_isactive"]

class bus_time_form():
    class Meta():
        model =bus_time
        exclude = ["time_id", "departure_time","arrival_time", "route_id"]

class bus_info_form():
    class Meta():
        model =bus_info
        #fields = '__all_' # automatically

        exclude = ["app_id", "bus_id","bus_type_id", "time_id", "bus_image","bus_status", "bus_fare","seats"]

class bus_seats_form():
    class Meta():
        model = bus_seats
        #fields = '__all_' # automatically

        exclude = ["seats_id", "seats_no","seats_isoccupied", "bus_id"]

class booking_details_form():
    class Meta():
        model = booking_details
        #fields = '__all_' # automatically

        exclude = ["booking_id", "date_time","bus_id", "is_booked","email"]