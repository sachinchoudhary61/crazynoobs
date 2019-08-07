from django.contrib import admin
from manager.models import managerrole,  hotelinfo, hotelguestinfo, room_type, hotelroomimages, hotelrooms

# Register your models here.
admin.site.register(managerrole)
#admin.site.register(appscategory)
admin.site.register(hotelinfo)
admin.site.register(hotelguestinfo)
admin.site.register(room_type)
admin.site.register(hotelroomimages)
admin.site.register(hotelrooms)

