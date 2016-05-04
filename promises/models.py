from django.db import models

from profiles.models import Profile


class Promise(models.Model):
    """
    Promise bound to a Profile
    """
    title = models.CharField(max_length=300)
    description = models.TextField()
    source_link = models.URLField(blank=True)
    source_file = models.FileField(upload_to='promise_source_files', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:80]
