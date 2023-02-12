"""Defines URL patterns for my_websites"""

from django.urls import path

from . import views


urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
]
