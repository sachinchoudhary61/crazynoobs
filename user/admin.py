from django.contrib import admin
from user.models import userrole, user_info,appscategory
# Register your models here.
admin.site.register(userrole)
admin.site.register(user_info)
admin.site.register(appscategory)

