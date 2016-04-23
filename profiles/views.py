from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import CreateProfileForm
from users.models import User


@login_required
def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    elif request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            profile = form.save(commit=False)
            profile.creator = user
            profile.save()
            return HttpResponseRedirect(reverse('view_profile',
                                                args=(profile.handle,)))

    return render(request, 'profiles/create.html', {'form': form})


def view_profile(request, handle):
    return render(request, 'profiles/view.html', {
        'profile': Profile.objects.get(handle=handle),
    })
