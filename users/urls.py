from django.conf.urls import url

from .views import ExtraData

urlpatterns = [
    url(r'^extra-data/', ExtraData, name='extra-data'),
]
