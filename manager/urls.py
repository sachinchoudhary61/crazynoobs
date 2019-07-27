
from django.conf.urls import url
from manager import views
app_name = "manager"

urlpatterns = [
    url(r'^managerindex/$', views.managerindex),

]