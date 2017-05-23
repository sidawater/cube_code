from django.conf.urls import url, include
from django.contrib import admin

from . import views
from .api import v1_api as codemap_api


urlpatterns = [
    url(r'^$', views.codemap_view),
    url(r'^api/', include(codemap_api.urls)),
    url(r'^build_map/', views.build_map),
]
