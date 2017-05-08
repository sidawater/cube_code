from django.conf.urls import url, include
from django.contrib import admin

from .api import v1_api as codemap_api


urlpatterns = [
    url(r'^api/', include(codemap_api.urls)),
]
