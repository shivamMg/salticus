from django.db import models

from countries.models import Country
from users.models import User


class Profile(models.Model):
    """
    Politician Profile
    """
    handle = models.SlugField(unique=True)
    full_name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos')
    header_photo= models.ImageField(upload_to='header_photos', blank=True)

    creator = models.ForeignKey(User)
    country = models.ForeignKey(Country)

    def get_absolute_url(self):
        return '/p/{}/about'.format(self.handle)

    def __str__(self):
        return self.handle
