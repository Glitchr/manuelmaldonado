from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.response import TemplateResponse
from decouple import config

from .models import Education, Job, Certification, Interest, SocialMedia, Skill
from .forms import ContactForm


def index(request):
    """The home page for the website"""
    social_media = SocialMedia.objects.all()

    # Log how many times the website has been visited
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'social_media': social_media, 'num_visits': num_visits}

    return render(request, 'my_websites/index.html', context)


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


def contactme(request):
    """Handles the contact form on the website"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # To name the sender in the email body
            message = f'You have received a new message from {from_email}:\n\n{message}'

            try:
                send_mail(subject, message, from_email, [config('MY_EMAIL')])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')               
            return redirect('success')
    
    return render(request, 'my_websites/contact.html', {'form': form})


def success(request):
    """Returns a success message after sending an email""" 
    return TemplateResponse(request, 'my_websites/success.html',)
            