from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from .models import Profile
from .forms import ProfileForm
from users.models import User


def index(request, handle):
    return render(request, 'profiles/index.html', {
        'profile': Profile.objects.get(handle=handle),
    })


@login_required
# Only Admins can create a Profile
@user_passes_test(lambda u: u.is_admin)
def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
    elif request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            profile = form.save(commit=False)
            profile.creator = user
            profile.save()
            return HttpResponseRedirect(reverse(ViewProfile.as_view(),
                                                args=(profile.handle,)))

    return render(request, 'profiles/create.html', {'form': form})


class ViewProfile(DetailView):
    model = Profile
    template_name = 'profiles/view.html'
    slug_field = 'handle'
    slug_url_kwarg = 'handle'


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'profiles/edit.html'
    slug_field = 'handle'
    slug_url_kwarg = 'handle'
    form_class = ProfileForm

    def test_func(self):
        """User must be a staff member"""
        return self.request.user.is_staff
