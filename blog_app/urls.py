from django.conf.urls import patterns, url
from blog_app import views


urlpatterns = patterns('',
                       url(r'^', views.BlogIndex.as_view(), name='index'),

                       )