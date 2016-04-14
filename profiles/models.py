from django.db import models


class Profile(models.Model):
    """
    Politician Profile
    """
    handle = models.SlugField(unique=True)
    full_name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.handle


class Promise(models.Model):
    """
    Promise made by Politician
    """
    title = models.CharField(max_length=300)
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:80]
