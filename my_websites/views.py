from django.shortcuts import render, get_object_or_404

from .models import Education, Job, Certification, Project, Interest, SocialMedia, Skill


def index(request):
    """The home page for the website"""
    social_media = SocialMedia.objects.all()
    context = {'social_media': social_media}

    return render(request, 'my_websites/index.html', context)


def projects(request):
    """The page for my projects"""
    projects = Project.objects.all().order_by('-date_added')
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


def resume(request):
    """Display my resume in HTML form"""
    educations = Education.objects.all().order_by('-start_date')
    jobs = Job.objects.all().order_by('-start_date')
    certifications = Certification.objects.all().order_by('-start_date')
    # Proficiency=1 is Expert, 2 is Proficient
    # Category=1 is Frameworks/Library/Tools, 2 is Coding
    expert_skills = Skill.objects.filter(proficiency=1, category=2)
    proficient_skills = Skill.objects.filter(proficiency=2, category=2)
    flt_skills = Skill.objects.filter(category=1)
    coding_skills = Skill.objects.filter(category=2)
    interests = Interest.objects.all()
    socialmedia = SocialMedia.objects.get(name='GitHub')
    context = {
        'educations': educations,
        'jobs': jobs,
        'certifications': certifications,
        'expert_skills': expert_skills,
        'proficient_skills': proficient_skills,
        'flt_skills': flt_skills,
        'coding_skills': coding_skills,
        'interests': interests,
        'socialmedia': socialmedia,
    }

    return render(request, 'my_websites/resume.html', context)
