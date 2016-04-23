from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('handle', 'full_name', 'description',)
        labels = {
            'handle': _('Handle'),
            'full_name': _('Full Name'),
            'description': _('Description'),
        }
