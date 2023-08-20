import statistics
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from gujrati_recognition import settings
from . import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls'),name = 'homepage'),
    path('scan',include('recognition_app.urls')),
    path('report',include('report.urls'),name='report'),
    path('contact',include('contact.urls'),name='contact'),
   
    # path('history',include('history.urls')),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
