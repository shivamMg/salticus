from django.db import models
from django.utils.http import int_to_base36

from profiles.models import Profile
from users.models import User


class Promise(models.Model):
    """
    Promise bound to a Profile
    """
    title = models.CharField(max_length=300)
    description = models.TextField()
    source_link = models.URLField(blank=True)
    source_file = models.FileField(upload_to='promise_source_files', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    creator = models.ForeignKey(User)

    def get_absolute_url(self):
        base36_id = int_to_base36(self.id)
        return '/p/{}/promises/{}'.format(self.profile.handle, base36_id)

    def __str__(self):
        return self.title[:80]
