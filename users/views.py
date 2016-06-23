from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserCreationForm, UserChangeForm


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'users/signup.html', {
        'form': form,}
    )



class AccountInfo(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/account.html'
    form_class = UserChangeForm

    def get_object(self):
        return self.request.user
