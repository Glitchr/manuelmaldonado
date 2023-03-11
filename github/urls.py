"""Defines URL patterns for github"""

from django.urls import path

from . import views


urlpatterns = [
    # The page for the portfolio
    path('projects/', views.repos, name='projects'),
    # Error page
    path('projects/error', views.repos, name='error'),
]