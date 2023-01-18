from django.db import models


class Education(models.Model):
    """Model representing university degrees"""
    title = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    university_url = models.URLField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Education'

    def __str__(self):
        """Return a string representation of the model"""
        return self.title


class Project(models.Model):
    """A model representing programming projects"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_published = models.CharField(max_length=50)
    is_opensource = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Job(models.Model):
    """A model representing job experience"""
    job_title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_employee = models.BooleanField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.job_title


class Certification(models.Model):
    """A model representing certifications earned"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    cert_url = models.URLField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_published = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class SocialMedia(models.Model):
    """A model representing social media accounts"""
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    is_public = models.BooleanField()
    date_added = models.DateField()
    date_updated = models.DateField()

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
