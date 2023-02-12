from django.shortcuts import render

from .models import Project, SocialMedia


def index(request):
    """The home page for the website"""
    social_media = SocialMedia.objects.all()
    context = {'social_media': social_media}

    return render(request, 'my_websites/index.html', context)


def projects(request):
    """The page for my projects"""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'my_websites/projects.html', context)