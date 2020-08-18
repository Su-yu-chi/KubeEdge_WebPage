# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:35:35 2020

@author: suyuchi
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recognition, name='recognition'),
    url(r'^control.html', views.user),
]