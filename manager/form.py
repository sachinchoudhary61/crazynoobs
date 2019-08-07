from django import forms
from manager.models import hotelinfo, hotelroomimages,hotelrooms,room_type

class hotelinfoForm(forms.ModelForm):
    class Meta():
        model = hotelinfo
        #fields = '__all_' # automatically

        exclude = ["hotel_status", "hotel_name", "hotel_city", "hotel_image",
                   "hotel_address", "hotel_no_rooms", "hotel_room_price",
                   'hotel_helpline_no',  "app_id",
                   "room_with_meal_or_without_meal", 'hotel_id', 'email']

class hotelroomsForm(forms.ModelForm):
    class Meta():
        model = hotelrooms
        #fields = '__all_' # automatically

        exclude = ["hotel_id","room_id","room_occupied",
                   "room_no", " isactive"]

class room_typeForm(forms.ModelForm):
    class Meta():
        model = room_type
        #fields = '__all_' # automatically

        exclude = ["room_id", "room_type_id", "room_type", "room_type_price"]

class hotelroomimageForm(forms.ModelForm):
    class Meta():
        model = hotelroomimages
        #fields = '__all_' # automatically

        exclude = ["room_id", "image_id", "image", "isactive"]
