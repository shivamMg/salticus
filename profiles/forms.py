from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.files.images import get_image_dimensions

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'handle',
            'full_name',
            'short_description',
            'long_description',
            'profile_photo',
            'header_photo',
        )
        labels = {
            'handle': _('Handle'),
            'full_name': _('Full Name'),
            'short_description': _('Short Description'),
            'long_description': _('Long Description'),
            'profile_photo': _('Profile Photo'),
            'header_photo': _('Header Photo'),
        }

    def clean_profile_photo(self):
        photo = self.cleaned_data.get('profile_photo')
        w, h = get_image_dimensions(photo)
        min_width, min_height = 300, 300

        if w != h:
            raise forms.ValidationError('Image should be square')
        if w < min_width or h < min_height:
            raise forms.ValidationError(('Image should be at least {}x{}' \
                ' pixels').format(min_width, min_height))
        return photo
