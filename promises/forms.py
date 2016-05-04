from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Promise


class PromiseForm(forms.ModelForm):
    class Meta:
        model = Promise
        fields = ('title', 'description', 'source_link', 'source_file')
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'source_link': _('Source Link'),
            'source_file': _('Source Document'),
        }
