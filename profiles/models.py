from django.db import models

from users.models import User


class Profile(models.Model):
    """
    Politician Profile
    """
    handle = models.SlugField(unique=True)
    full_name = models.CharField(max_length=30)
    description = models.TextField()
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.handle


class InfoField(models.Model):
    """
    Field with a label and its value
    """
    label = models.CharField(max_length=30)
    value = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}, {}'.format(self.label, self.value[:40], self.profile)


class Promise(models.Model):
    """
    Promise made by Politician
    """
    title = models.CharField(max_length=300)
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:80]
