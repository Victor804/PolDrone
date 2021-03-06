"""poldrone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from gps.views import *
from django.contrib import admin
from django.conf import settings
from django.views.static import serve



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^add_flight/$', add_flight, name='add_flight'),
    url(r'delete_flight/(?P<id>\d+)/$', delete_flight),
    url(r'choose_maps/(?P<id>\d+)/$', choose_maps),
    url(r'waypoint/(?P<id>\d+)/$', waypoint),
    url(r'heatmap_co2/(?P<id>\d+)/$', heatmap_co2),
    url(r'heatmap_nh3/(?P<id>\d+)/$', heatmap_nh3),
    url(r'heatmap_nox/(?P<id>\d+)/$', heatmap_nox),
    url(r'analyse/(?P<id>\d+)/$', analyse),
    url(r'^add_project/$', add_project, name='add_project'),
    url(r'delete_project/(?P<id>\d+)/$', delete_project),
    url(r'point/(?P<id>\d+)/$', point, name="point"),
    url(r'table/(?P<id>\d+)/$', table, name="table"),
    url(r'^about/$', about, name="about"),
]

if settings.DEBUG:
    urlpatterns+= [
            url(r'media/(?P<path>.*)$',
            serve, {'document_root':
                    settings.MEDIA_ROOT,}), ]