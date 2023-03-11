from django.db import models


class Repository(models.Model):
    """A model representing programming projects"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_public = models.BooleanField()
    is_opensource = models.BooleanField(default=False)

    class Meta:

        verbose_name_plural = 'Repositories'

    def __str__(self):
        """Return a string representation of the model"""
        return self.name
