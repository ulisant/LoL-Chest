from django.conf.urls import url

from .views import Menu

urlpatterns = [
    url(r'^', Menu, name='menu'),
]
