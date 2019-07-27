from django.contrib import admin
from user.models import userrole, user_info
# Register your models here.
admin.site.register(userrole)
admin.site.register(user_info)
