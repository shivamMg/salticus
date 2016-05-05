from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.utils.http import base36_to_int

from profiles.models import Profile
from .models import Promise
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
            promise.creator = request.user
            promise.save()
            return HttpResponseRedirect(promise.get_absolute_url())

    return render(request, 'promises/create.html', {'form': form})


class ViewPromise(DetailView):
    model = Promise
    template_name = 'promises/view.html'

    def get_object(self):
        promise_id = base36_to_int(self.kwargs.get('base36_id', None))
        promise = get_object_or_404(Promise, pk=promise_id)
        return promise


class EditPromise(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Promise
    template_name = 'promises/edit.html'
    form_class = PromiseForm

    def get_object(self):
        promise_id = base36_to_int(self.kwargs.get('base36_id', None))
        promise = get_object_or_404(Promise, pk=promise_id)
        return promise

    def test_func(self):
        """User must be the creator of the promise"""
        promise_creator = self.get_object().creator
        user = self.request.user
        return user == promise_creator
