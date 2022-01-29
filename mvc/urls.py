from __future__ import absolute_import, unicode_literals
from unicodedata import name
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_post, name="add")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
