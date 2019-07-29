from django.conf.urls import url
from user import views
app_name = "user"

urlpatterns = [

    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login),
    url(r'^activeuser/$', views.verifyuser),
    url(r'^forgetpasswordpage/$', views.update_password),
    url(r'^forgetpassword2page/$', views.resetpassword),
    url(r'^index/$', views.admin_index),
    url(r'^logout/$', views.logout),



]
