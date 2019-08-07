
from django.conf.urls import url
from manager import views
app_name = "manager"

urlpatterns = [
    url(r'^managerindex/$', views.managerindex),
    url(r'^hoteldatainsertion/$', views.hotelinfofn),
    url(r'^businessuserpage/$', views.businessusermainpage),
    url(r'^businessuserpage1/$', views.businessusercontactpage),
    url(r'^businessuserpage1/$', views.businessusercontactpage),
    url(r'^fetchinghotelinfo/$', views.fetchinghotelinfo),
    # url(r'^edithotelprofileinfo/$', views.edithotelprofile),

    url(r'^edithotelprofileinfo/$', views.edithoteldata)
]
