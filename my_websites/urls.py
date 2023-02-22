"""Defines URL patterns for my_websites"""

from django.urls import path

from . import views


urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # The page for the portfolio
    path('projects/', views.projects, name='projects'),
    # Detail page for each project
    path('projects/<int:project_id>', views.project, name='project'),
    # The resume page
    path('resume/', views.resume, name='resume'),
]
