from django.db import models
from datetime import datetime

class Repository(models.Model):
    """A model representing programming projects"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    pushed_at = models.DateTimeField(null=True)
    is_public = models.BooleanField()
    is_listed = models.BooleanField(default=True)

    class Meta:

        verbose_name_plural = 'Repositories'

    def __str__(self):
        """Return a string representation of the model"""
        return self.name
