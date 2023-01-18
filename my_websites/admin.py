from django.contrib import admin

from .models import Certification, Education, Job, Language, Project, Skill, SocialMedia


admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Certification)
admin.site.register(SocialMedia)
admin.site.register(Skill)
admin.site.register(Language)
