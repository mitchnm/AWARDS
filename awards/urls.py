from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$',views.welcome,name='welcome'),
  url(r'^profile/(\d+)',views.profile,name='profile'),
  url(r'^update_profile/(\d+)',views.update_profile,name='update_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)