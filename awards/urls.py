from django.conf.urls import url
from . import views
from django.contrib.auth import views

urlpatterns = [
  url(r'^$',views.welcome,name='welcome'),
  url(r'^logout/$', views.logout, {"next_page": '/'}),
]