from django.contrib import admin

from .models import Certification, Education, Job, Language, Project, Category, Proficiency, Skill, Interest, SocialMedia


admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Certification)
admin.site.register(SocialMedia)
admin.site.register(Category)
admin.site.register(Proficiency)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Language)
