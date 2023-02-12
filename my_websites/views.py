from django.shortcuts import render, get_object_or_404

from .models import Education, Job, Certification, Project, SocialMedia, Skill


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


def project(request, project_id):
    """Display detailed information for each project"""
    project = get_object_or_404(Project, id=project_id)
    context = {'project': project}

    return render(request, 'my_websites/project.html', context)


def about(request):
    """The page about me"""
    educations = Education.objects.all().order_by('start_date')
    jobs = Job.objects.all().order_by('start_date')
    certifications = Certification.objects.all().order_by('start_date')
    skills = Skill.objects.all()
    context = {
        'education': educations,
        'job': jobs,
        'certification': certifications,
        'skill': skills,
    }

    return render(request, 'my_websites/about.html', context)

