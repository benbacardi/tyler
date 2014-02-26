'''Tyler URLs'''
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tyler.views.get_image'),
)
