from django import forms
from user.models import user_info

class user_info_form(forms.ModelForm):
    class Meta():
        model = user_info
        #fields = '__all_' # automatically

        exclude = ["roleid", "first_name", "last_name", "email", "password", "mobile_no", "address", "image", "otp", "otp_gen_time", "isactive", "token"]
