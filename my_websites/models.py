from django.db import models


class Education(models.Model):
    """Model representing university degrees"""
    title = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    university_url = models.URLField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_completed = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        """Return a string representation of the model"""
        return self.title


class Project(models.Model):
    """A model representing programming projects"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    repository_link = models.URLField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_opensource = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Job(models.Model):
    """A model representing job experience"""
    job_title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    company = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_employee = models.BooleanField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.job_title


class Certification(models.Model):
    """A model representing certifications earned"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True, null=True)
    cert_url = models.URLField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class SocialMedia(models.Model):
    """A model representing social media accounts"""
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    is_public = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Social Media"

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Skill(models.Model):
    """A model representing programming skills"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Language(models.Model):
    """A model representing natural languages"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name
