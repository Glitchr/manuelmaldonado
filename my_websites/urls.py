"""Defines URL patterns for my_websites"""

from django.urls import path

from . import views


urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # The resume page
    path('resume/', views.resume, name='resume'),
    # Contact Me page
    path('contact/', views.contactme, name='contact'),
    # Email sent successfully page
    path('contact/success/', views.success, name='success'),
    # Cookie policy page
    path('cookie-policy/', views.cookie_policy, name='cookie-policy'),
]
