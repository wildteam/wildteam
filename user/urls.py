from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login$', views.login, name='login'),
    # url(r'^deal_login$', views.deal_login, name='deal_login'),
    # url(r'^register$', views.register),
    url(r'^deal_register$', views.deal_register, name='deal_register'),
]