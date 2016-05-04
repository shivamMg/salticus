from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profiles.models import Profile
from .forms import PromiseForm


@login_required
def create_promise(request, handle):
    if request.method == 'GET':
        form = PromiseForm()
    elif request.method == 'POST':
        form = PromiseForm(request.POST, request.FILES)
        if form.is_valid():
            promise = form.save(commit=False)
            promise.profile = Profile.objects.get(handle=handle)
            promise.save()
            # return HttpResponseRedirect(reverse(ViewProfile.as_view(),
            #                                     args=(profile.handle,)))

    return render(request, 'promises/create.html', {'form': form})
